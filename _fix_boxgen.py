# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
p = r"addons\mcc_sandbox_mod\mcc\dialogs\mcc_boxGen_change.sqf"
with open(p, 'r', encoding='utf-8', errors='replace') as f:
    lines = f.readlines()

new_block = [
'\twhile {MCC3DRuning} do\n',
'\t\t{\n',
'\t\tMCC3DgotValue = false; \n',
'\t\twhile {!MCC3DgotValue && MCC3DRuning} do {sleep 0.2};\n',
'\t\tif (MCC3DRuning) then \n',
'\t\t\t{\n',
'\t\t\t mcc_safe = mcc_safe + FORMAT ["[[%1, %2, %3, %4,%5,%6],\'MCC_fnc_boxGenerator\',true,false] spawn BIS_fnc_MP;\n',
'\t\t\t\t\tsleep 1;"\t\t\t\t\t\t\t\t \n',
'\t\t\t\t\t\t,MCC3DValue select 0\n',
'\t\t\t\t\t\t,MCC3DValue select 1\n',
'\t\t\t\t\t\t,tempBoxWeapons\n',
'\t\t\t\t\t\t,tempBoxMagazine\n',
'\t\t\t\t\t\t,tempBoxItems\n',
'\t\t\t\t\t\t,tempBoxRucks\n',
'\t\t\t\t\t\t];\t\n',
'\t\t\t[[MCC3DValue select 0, MCC3DValue select 1, tempBoxWeapons, tempBoxMagazine,tempBoxItems,tempBoxRucks],"MCC_fnc_boxGenerator",true,false] spawn BIS_fnc_MP;\n',
'\t\t\tMCC_3Dterminate = true;  \n',
'\t\t\t};\n',
'\t\tsleep 0.1;\n',
'\t\t};\n',
]

# sanity: current lines 200-217
cur = ''.join(lines[200:218])
assert 'while {MCC3DRuning} do' in cur and 'MCC_3Dterminate' in cur, "region mismatch"
lines[200:218] = new_block
with open(p, 'w', encoding='utf-8', errors='replace') as f:
    f.writelines(lines)
print("boxGen fixed")
# verify braces
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
