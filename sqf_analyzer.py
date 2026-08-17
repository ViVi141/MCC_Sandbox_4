#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sqf_analyzer.py - MCC/SQF 调用关系分析器（调用树 · 类型推断 · 依赖检查）

思想：把整个模组看成一张"调用图"（有向图）。
  - 节点 = 文件 / 函数 / 配置类 / 对话框
  - 边   = 调用关系（"谁调用了谁"）
从入口递归展开，像树一样逐层下钻，给出：
  1) 调用树（缩进树，标注每个节点的类型）
  2) 逆向引用（每个节点被谁调用）
  3) 问题报告（缺失文件 / 未定义函数 / 循环依赖 / 孤立节点）

用法:
  python sqf_analyzer.py [--root ADDON] [--entry FILE] [--depth N] [--target NAME] [--json] [--problems]
"""

import os, re, sys, json, argparse
from collections import defaultdict

BS = chr(92)  # backslash

# ---------- 1) 基础工具 ----------
def strip_comment(line):
    """去掉 // 与 /* */ 注释（字符串内保留）。"""
    out = []; i = 0; n = len(line); instr = None
    while i < n:
        c = line[i]
        if instr:
            out.append(c)
            if c == instr:
                if i + 1 < n and line[i+1] == instr:
                    out.append(line[i+1]); i += 2; continue
                instr = None
            i += 1; continue
        if c in ('"', "'"):
            instr = c; out.append(c); i += 1; continue
        if c == '/' and i + 1 < n and line[i+1] == '/':
            break
        if c == '/' and i + 1 < n and line[i+1] == '*':
            j = line.find('*/', i + 2)
            i = n if j == -1 else j + 2
            continue
        out.append(c); i += 1
    return ''.join(out)


def resolve_addon_path(p):
    """把配置里的 \\mcc_sandbox_mod\\xxx 解析为 addon 根下的相对路径。"""
    p = p.replace('\\\\', '/').replace('\\', '/').replace('\\', '/')
    p = p.lstrip('/')
    if p.startswith('mcc_sandbox_mod/'):
        p = p[len('mcc_sandbox_mod/'):]
    return p


T_SCRIPT, T_FUNCTION, T_CONFIG, T_DIALOG, T_EVENT = 'script', 'function', 'config', 'dialog', 'event'
KIND_ZH = {T_SCRIPT: '脚本', T_FUNCTION: '函数', T_CONFIG: '配置', T_DIALOG: '对话框', T_EVENT: '事件'}

# ---------- 2) 文件解析器 ----------
class FileParser:
    """解析一个 SQF 文件，提取所有调用关系。"""
    def __init__(self, path, root):
        self.path = path
        self.rel = os.path.relpath(path, root)
        self.root = root
        self.includes = []   # #include "path"
        self.execvm = []     # execVM "path" / execVM MCC_path+"path" / format["%1path"]
        self.preproc = []    # preprocessFile(LineNumbers)
        self.calls = []      # (funcName, kind) kind in call/spawn
        self.remote = []     # remoteExec ["fnc"]
        self.defines = []    # 本文件定义的函数 X = {...}
        self.dialogs = []    # createDialog "X"
        self.events = []     # addEventHandler "name"

    def parse(self):
        with open(self.path, 'r', encoding='utf-8', errors='replace') as f:
            src = f.read()
        for raw in src.split('\n'):
            line = strip_comment(raw)
            s = line.strip()
            # #include
            m = re.match(r'#include' + BS + r's+"([^"]+)"', s)
            if m:
                self.includes.append(m.group(1)); continue
            # execVM "path"
            for m in re.finditer(BS + r'bexecVM' + BS + r's*[("]?' + BS + r's*"([^"]+)"', line):
                self.execvm.append(m.group(1))
            # execVM format ["%1path", ...]
            for m in re.finditer(BS + r'bexecVM' + BS + r's+format' + BS + r's*\[.*?"%1([^"]*)"', line):
                self.execvm.append('%' + m.group(1))
            # execVM MCC_path + "path"
            for m in re.finditer(r'MCC_path' + BS + r's*' + BS + chr(43) + BS + r's*"([^"]+)"', line):
                self.execvm.append(m.group(1))
            # preprocessFile(LineNumbers)
            for m in re.finditer(BS + r'bpreprocessFile(?:LineNumbers)?' + BS + r's*[("]?' + BS + r's*"([^"]+)"', line):
                self.preproc.append(m.group(1))
            # call / spawn FNC
            for m in re.finditer(BS + r'b(?:call|spawn)' + BS + r's+(MCC_fnc_[A-Za-z0-9_]+|GAIA_fnc_[A-Za-z0-9_]+|BIS_fnc_[A-Za-z0-9_]+|bis_fnc_[A-Za-z0-9_]+)', line):
                self.calls.append((m.group(1), m.group(0).split()[0]))
            for m in re.finditer(BS + r']' + BS + r's*(?:call|spawn)' + BS + r's+([A-Za-z_][A-Za-z0-9_]*)', line):
                fn = m.group(1)
                if fn.startswith(('MCC_fnc_', 'GAIA_fnc_', 'BIS_fnc_', 'bis_fnc_')):
                    self.calls.append((fn, 'call' if 'call' in m.group(0) else 'spawn'))
            # remoteExec ["fnc", ...]
            for m in re.finditer(BS + r'bremoteExec(?:Call)?' + BS + r's*\[.*?"([^"]+)"', line):
                self.remote.append(m.group(1))
            # 函数定义
            for m in re.finditer(BS + r'b(MCC_fnc_[A-Za-z0-9_]+|GAIA_fnc_[A-Za-z0-9_]+|fn_[A-Za-z0-9_]+)' + BS + r's*=', line):
                self.defines.append(m.group(1))
            # createDialog
            for m in re.finditer(BS + r'bcreateDialog' + BS + r's+"([^"]+)"', line):
                self.dialogs.append(m.group(1))
            # 事件处理器
            for m in re.finditer(BS + r'badd(?:Mission)?EventHandler' + BS + r's*\[.*?"([A-Za-z0-9_]+)"', line):
                self.events.append(m.group(1))


# ---------- 3) 调用图 ----------
class CallGraph:
    def __init__(self):
        self.nodes = {}                    # id -> {name, kind, path}
        self.edges = defaultdict(list)     # id -> [(target_id, edge_kind)]
        self._ids = {}
        self.name2id = defaultdict(list)

    def add_node(self, name, kind, path=None):
        key = (name.lower(), kind)
        if key in self._ids:
            return self._ids[key]
        nid = len(self.nodes)
        self._ids[key] = nid
        self.nodes[nid] = {'name': name, 'kind': kind, 'path': path}
        self.name2id[name.lower()].append(nid)
        return nid

    def add_edge(self, s, d, k):
        if s != d and d not in [e[0] for e in self.edges[s]]:
            self.edges[s].append((d, k))

    def find(self, name):
        return self.name2id.get(name.lower(), [])


def load_cfgfn(root):
    """扫描所有 cfgFunctions.hpp：class fncName -> file="path"。"""
    reg = {}
    reg2 = {}
    for dp, dn, fns in os.walk(root):
        for fn in fns:
            if fn.lower() != 'cfgfunctions.hpp':
                continue
            p = os.path.join(dp, fn)
            with open(p, 'r', encoding='utf-8', errors='replace') as f:
                lines = f.readlines()
            cur = None
            for raw in lines:
                line = strip_comment(raw); s = line.strip()
                fm = re.search(r'file' + BS + r's*=' + BS + r's*"([^"]+)"', s)
                if fm:
                    cur = fm.group(1)
                cm = re.match(r'class' + BS + r's+(\w+)', s)
                if cm and '{' in s:
                    reg2[cm.group(1).lower()] = (cur, os.path.relpath(p, root).lower())
    return reg2


def build_graph(root):
    g = CallGraph()
    parsers = {}
    sqf_files = {}
    for dp, dn, fns in os.walk(root):
        for fn in fns:
            if fn.lower().endswith('.sqf'):
                p = os.path.join(dp, fn)
                rel = os.path.relpath(p, root).lower().replace('\\', '/')
                sqf_files[rel] = p
    for rel, p in sqf_files.items():
        pr = FileParser(p, root)
        try:
            pr.parse()
        except Exception as e:
            print('[warn] parse error:', p, e)
        parsers[rel] = pr
        g.add_node(rel, T_SCRIPT, rel)

    reg = load_cfgfn(root)
    for fname, (fpath, cfgpath) in reg.items():
        fullname = fname
        src = (fpath or cfgpath or '')
        if 'gaia' in src.lower():
            fullname = 'gaia_fnc_' + fname
        else:
            fullname = 'mcc_fnc_' + fname
        g.add_node(fullname, T_FUNCTION, fpath or cfgpath)

    for rel, pr in parsers.items():
        src = g.find(rel)[0]
        for inc in pr.includes:
            t = resolve_addon_path(inc).lower()
            tid = g.find(t)
            if not tid:
                g.add_node(t, T_CONFIG, t); tid = g.find(t)
            g.add_edge(src, tid[0], 'include')
        for t in pr.execvm + pr.preproc:
            if t.startswith("'+") or t.startswith('+'):
                continue
            t = resolve_addon_path(t).replace('%1', '').lower()
            if not t.strip():
                continue
            tid = g.find(t)
            if not tid:
                g.add_node(t, T_SCRIPT, t); tid = g.find(t)
            g.add_edge(src, tid[0], 'execvm')
        for fn, kind in pr.calls:
            tid = g.find(fn)
            if not tid:
                g.add_node(fn, T_FUNCTION, None); tid = g.find(fn)
            g.add_edge(src, tid[0], kind)
        for fn in pr.remote:
            if fn.lower() in ('call', 'spawn', 'execvm', 'remoteexec'):
                continue
            tid = g.find(fn)
            if not tid:
                g.add_node(fn, T_FUNCTION, None); tid = g.find(fn)
            g.add_edge(src, tid[0], 'remote')
        for d in pr.dialogs:
            tid = g.find(d)
            if not tid:
                g.add_node(d, T_DIALOG, None); tid = g.find(d)
            g.add_edge(src, tid[0], 'dialog')
        for fn in pr.defines:
            fid = g.find(fn)
            if not fid:
                fid = [g.add_node(fn, T_FUNCTION, pr.rel)]
            else:
                g.nodes[fid[0]]['path'] = pr.rel
            g.add_edge(src, fid[0], 'defines')
    return g, parsers

# ---------- 4) 分析 ----------
def call_tree(g, start_id, max_depth=0, visited=None, depth=0):
    """DFS 展开调用树（缩进文本）。"""
    lines = []
    visited = visited or set()
    node = g.nodes[start_id]
    indent = '  ' * depth
    label = node['name']
    if node['kind'] == T_SCRIPT:
        label = os.path.basename(label)
    zh = KIND_ZH.get(node['kind'], node['kind'])
    lines.append('%s%s [%s]' % (indent, label, zh))
    if max_depth and depth >= max_depth:
        return lines
    if start_id in visited:
        return lines
    visited = visited | {start_id}
    for dst, ek in sorted(g.edges[start_id], key=lambda e: g.nodes[e[0]]['name']):
        sub = call_tree(g, dst, max_depth, visited, depth + 1)
        if sub:
            sub[0] = sub[0] + '  <- ' + ek
            lines.extend(sub)
    return lines


def reverse_refs(g):
    """逆向引用：target_name -> [(caller_name, edge_kind, caller_id, target_id)]"""
    rev = defaultdict(list)
    for src, edges in g.edges.items():
        for dst, ek in edges:
            rev[g.nodes[dst]['name']].append((g.nodes[src]['name'], ek, src, dst))
    return rev


def detect_cycles(g):
    """Tarjan SCC 找循环依赖。"""
    index = 0
    indices, lowlink, on_stack, stack, cycles = {}, {}, set(), [], []

    def strong(v):
        nonlocal index
        indices[v] = lowlink[v] = index
        index += 1
        stack.append(v); on_stack.add(v)
        for w, _ in g.edges[v]:
            if w not in indices:
                strong(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif w in on_stack:
                lowlink[v] = min(lowlink[v], indices[w])
        if lowlink[v] == indices[v]:
            comp = []
            while True:
                w = stack.pop(); on_stack.discard(w); comp.append(w)
                if w == v: break
            if len(comp) > 1:
                cycles.append(comp)

    for v in g.nodes:
        if v not in indices:
            strong(v)
    return cycles


def find_missing(g, parsers, root):
    """缺失目标：execVM/preprocess 文件不存在，或调用函数未定义。"""
    problems = []
    existing = set()
    for dp, dn, fns in os.walk(root):
        for fn in fns:
            if fn.lower().endswith('.sqf'):
                r = os.path.relpath(os.path.join(dp, fn), root).lower().replace('\\', '/')
                existing.add(r)
    defined = set()
    for nid, node in g.nodes.items():
        if node['kind'] == T_FUNCTION and node['path']:
            defined.add(node['name'].lower())
    for rel, pr in parsers.items():
        for t in pr.execvm + pr.preproc:
            target = resolve_addon_path(t).replace('%1', '')
            if target.startswith("'") or target.startswith('+'):
                continue
            tl = target.lower()
            if tl.startswith(('%', 'a3/', 'lv/')) or re.match(r'^\d+mcc', tl):
                continue
            if not target.strip() or not target.lower().endswith('.sqf'):
                continue
            if target.lower() not in existing:
                problems.append(('missing-file', rel, target, 'execVM/preprocess 目标不存在'))
        DOC_ONLY = ('mcc_fnc_ambientfiresclientside', 'mcc_fnc_ambientambientfirepropagation',
                     'mcc_fnc_ambientfiresclientside', 'gaia_fnc_knowsabout', 'gaia_fnc_spawngroup')
        for fn, kind in pr.calls:
            if fn.lower() in DOC_ONLY:
                continue
            if fn.lower().startswith(('bis_fnc_', 'bis_')) or fn.lower().startswith(('mcc_fnc_', 'gaia_fnc_')) and fn.lower() not in defined:
                if fn.lower().startswith(('mcc_fnc_', 'gaia_fnc_')):
                    problems.append(('undefined-func', rel, fn, '%s 目标函数未定义' % kind))
        for fn in pr.remote:
            if fn.lower() in ('call', 'spawn', 'execvm', 'remoteexec'):
                continue
            if fn.lower().startswith(('mcc_fnc_', 'gaia_fnc_')) and fn.lower() not in defined:
                problems.append(('undefined-func', rel, fn, 'remoteExec 目标函数未定义'))
    return problems


def find_orphans(g, entry_ids):
    has_in = set()
    for src, edges in g.edges.items():
        for dst, _ in edges:
            has_in.add(dst)
    orphans = []
    for nid, node in g.nodes.items():
        if node['kind'] == T_SCRIPT and nid not in has_in and nid not in entry_ids:
            orphans.append(node['name'])
    return orphans


def detect_entries(root):
    out = []
    for cand in ['config.cpp', 'init.sqf', 'XEH_preInit.sqf']:
        if os.path.exists(os.path.join(root, cand)):
            out.append(cand)
    return out


# ---------- 5) CLI ----------
def main():
    ap = argparse.ArgumentParser(description='SQF 调用关系分析器')
    ap.add_argument('--root', default='addons/mcc_sandbox_mod', help='addon 根目录')
    ap.add_argument('--entry', default=None, help='入口文件（相对 addon 根）')
    ap.add_argument('--depth', type=int, default=0, help='调用树最大深度（0=无限）')
    ap.add_argument('--target', default=None, help='查看某个文件/函数的调用关系')
    ap.add_argument('--json', action='store_true', help='输出 JSON')
    ap.add_argument('--problems', action='store_true', help='只输出问题报告')
    args = ap.parse_args()

    root = args.root
    if not os.path.isdir(root):
        print('错误: %s 不是有效目录' % root)
        sys.exit(1)

    print('==== 构建调用图: %s ====' % root)
    g, parsers = build_graph(root)
    print('节点数: %d  边数: %d' % (len(g.nodes), sum(len(e) for e in g.edges.values())))

    entries = [args.entry] if args.entry else detect_entries(root)
    print('入口: %s' % ', '.join(entries))
    entry_ids = []
    for e in entries:
        eid = g.find(e.lower())
        if eid:
            entry_ids.append(eid[0])
        else:
            entry_ids.append(g.add_node(e.lower(), T_SCRIPT, e))

    if args.target:
        tids = g.find(args.target.lower())
        if not tids:
            print('未找到目标: %s' % args.target)
            return
        for tid in tids:
            node = g.nodes[tid]
            print()
            print('==== %s [%s] ====' % (node['name'], KIND_ZH.get(node['kind'], node['kind'])))
            print('-- 它调用了谁 (out) --')
            for dst, ek in sorted(g.edges[tid], key=lambda e: g.nodes[e[0]]['name']):
                print('   %-8s -> %s [%s]' % (ek, g.nodes[dst]['name'], KIND_ZH.get(g.nodes[dst]['kind'], g.nodes[dst]['kind'])))
            print('-- 谁调用了它 (in) --')
            rev = reverse_refs(g)
            for caller, ek, cs, cd in rev.get(node['name'], []):
                if cd == tid:
                    print('   %-8s <- %s [%s]' % (ek, caller, KIND_ZH.get(g.nodes[cs]['kind'], g.nodes[cs]['kind'])))
        return

    if args.problems:
        problems = find_missing(g, parsers, root)
        print()
        print('==== 问题报告 (%d) ====' % len(problems))
        for typ, src, target, msg in problems[:80]:
            print('  [%s] %s -> %s  (%s)' % (typ, src, target, msg))
        cycles = detect_cycles(g)
        print()
        print('循环依赖: %d 个' % len(cycles))
        for c in cycles[:10]:
            print('   ', ' -> '.join(g.nodes[n]['name'] for n in c))
        return

    print()
    print('==== 调用树 ====')
    for eid in entry_ids:
        tree = call_tree(g, eid, args.depth)
        print('\n'.join(tree))
        print()

    problems = find_missing(g, parsers, root)
    print('==== 问题报告 (%d) ====' % len(problems))
    for typ, src, target, msg in problems[:60]:
        print('  [%s] %s -> %s  (%s)' % (typ, src, target, msg))
    if len(problems) > 60:
        print('  ... 还有 %d 个' % (len(problems) - 60))

    cycles = detect_cycles(g)
    print()
    print('循环依赖: %d 个' % len(cycles))
    for c in cycles[:10]:
        print('   ', ' -> '.join(g.nodes[n]['name'] for n in c))

    if args.json:
        out = {
            'nodes': [{'id': nid, 'name': n['name'], 'kind': n['kind'], 'path': n['path']} for nid, n in g.nodes.items()],
            'edges': [{'src': s, 'dst': d, 'kind': k} for s, es in g.edges.items() for d, k in es],
            'problems': [{'type': t, 'src': s, 'target': tg, 'msg': m} for t, s, tg, m in problems],
            'cycles': [[g.nodes[n]['name'] for n in c] for c in cycles],
        }
        print(json.dumps(out, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
