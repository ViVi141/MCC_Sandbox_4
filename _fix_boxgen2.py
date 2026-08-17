# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
p = r"addons\mcc_sandbox_mod\mcc\dialogs\mcc_boxGen_change.sqf"
with open(p, 'r', encoding='utf-8', errors='replace') as f:
    lines = f.readlines()
# delete line 221 (0-based 220) - the extra '};'
if lines[220].strip() == '};':
    del lines[220]
    with open(p, 'w', encoding='utf-8', errors='replace') as f:
        f.writelines(lines)
    print("removed extra }; at old line 221")
else:
    print("line 221 is:", repr(lines[220]))
# verify
def check(content):
    stack = []; issues = []; i, line = 0, 1; n = len(content)
    in_str = None; in_comment = False
    pairs = {'(':')', '[':']', '{':'}'}
    closers = {')':'(', ']':'[', '}':'{'}
    while i < n:
        c = content[i]
        if c == '\n': line += 1; i += 1; continue
        if in_comment:
            if c == '*' and i+1 < n and content[i+1] == '/': in_comment = False; i += 2; continue
            i += 1; continue
        if in_str:
            if c == in_str:
                if i+1 < n and content[i+1] == in_str: i += 2; continue
                in_str = None
            i += 1; continue
        if c in ('"', "'"): in_str = c; i += 1; continue
        if c == '/' and i+1 < n and content[i+1] == '/':
            while i < n and content[i] != '\n': i += 1
            continue
        if c == '/' and i+1 < n and content[i+1] == '*':
            in_comment = True; i += 2; continue
        if c in pairs: stack.append((c, line)); i += 1; continue
        if c in closers:
            if not stack: issues.append((c, line, 'unexpected'))
            else:
                top, tline = stack.pop()
                if top != closers[c]: issues.append((top, tline, c, line, 'mismatch'))
            i += 1; continue
        i += 1
    for s, l in stack: issues.append((s, l, 'unclosed'))
    return issues
with open(p, 'r', encoding='utf-8', errors='replace') as f:
    print("boxGen check:", check(f.read()) or "CLEAN")
