# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
p = r"addons\mcc_sandbox_mod\mcc\missionWizard\fnc\fn_MWSpawnInZone.sqf"
with open(p, 'r', encoding='utf-8', errors='replace') as f:
    lines = f.readlines()
# lines 107-109 (0-based 106-108): remove the isNull if, keep the remoteExec
# 107: 'if (!(isNull _ar select 0)) then {\n'
# 108: '\t[_ar, ...] remoteExec ...;\n'
# 109: '};\n'
assert 'isNull _ar select 0' in lines[106]
lines[106] = lines[107]  # keep the remoteExec line
del lines[107:109]       # remove the if line + closing
with open(p, 'w', encoding='utf-8', errors='replace') as f:
    f.writelines(lines)
print("fixed")
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
    print("MW check:", check(f.read()) or "CLEAN")
