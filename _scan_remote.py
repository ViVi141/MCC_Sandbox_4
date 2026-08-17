# -*- coding: utf-8 -*-
import sys, io, re, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
root = r"addons\mcc_sandbox_mod"
# 1. Find mode setting
for dirpath, dirs, files in os.walk(root):
    for fn in files:
        if fn.lower() == 'cfgsqfc' or 'remoteexec' in fn.lower():
            p = os.path.join(dirpath, fn)
            with open(p, 'r', encoding='utf-8', errors='replace') as f:
                c = f.read()
            if 'mode' in c or 'class' in c.lower():
                print("=== %s ===" % p[len(root)+1:])
                for m in re.finditer(r'mode\s*=\s*\d+', c):
                    print("  mode:", m.group(0))
# 2. All remoteExec / remoteExecCall function names in code
called = set()
for dirpath, dirs, files in os.walk(root):
    for fn in files:
        if not fn.endswith('.sqf'): continue
        p = os.path.join(dirpath, fn)
        try:
            with open(p, 'r', encoding='utf-8', errors='replace') as f:
                c = f.read()
        except Exception: continue
        for m in re.finditer(r'remoteExec(?:Call)?\s*\[\s*"([^"]+)"', c):
            called.add(m.group(1))
        for m in re.finditer(r'remoteExec(?:Call)?\s*\[\s*([A-Za-z_][A-Za-z0-9_]*)\b', c):
            called.add(m.group(1))
# 3. whitelisted functions
whitelist = set()
for dirpath, dirs, files in os.walk(root):
    for fn in files:
        if fn.lower() != 'cfgremoteexec.hpp': continue
        p = os.path.join(dirpath, fn)
        with open(p, 'r', encoding='utf-8', errors='replace') as f:
            c = f.read()
        for m in re.finditer(r'class\s+(\S+)\s*\{', c):
            whitelist.add(m.group(1))
print("remoteExec called functions:", len(called))
print("whitelisted:", len(whitelist))
# functions called but NOT whitelisted (potential issue if mode>0)
not_whitelisted = sorted(called - whitelist)
print("called but NOT whitelisted:", len(not_whitelisted))
for f in not_whitelisted[:40]:
    print("  ", f)
