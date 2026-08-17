# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
p = r"addons\mcc_sandbox_mod\mcc\missionWizard\fnc\fn_MWSpawnInZone.sqf"
with open(p, 'r', encoding='utf-8', errors='replace') as f:
    lines = f.readlines()
# fix L107 (0-based 106): isNull _ar select 0 -> remove
if 'isNull _ar select 0' in lines[106]:
    # replace the 3-line if block with single line
    lines[106] = '\t[_ar, "mcc_setup", false, false] remoteExec ["mcc_setup", 2, false];\n'
    # remove lines 108-109 (the closing };)  -- wait, careful
    # current: 106=if(...) then {, 107=remoteExec, 108=}; 
    # we want: 106=remoteExec line, remove 107 & 108? Let's just do text replace
with open(p, 'r', encoding='utf-8', errors='replace') as f:
    c = f.read()
old = '\tif (!(isNull _ar select 0)) then {\n\t[_ar, "mcc_setup", false, false] remoteExec ["mcc_setup", 2, false];\n};\n'
new = '\t[_ar, "mcc_setup", false, false] remoteExec ["mcc_setup", 2, false];\n'
if old in c:
    c = c.replace(old, new, 1)
    with open(p, 'w', encoding='utf-8', errors='replace') as f:
        f.write(c)
    print("L107 fixed")
else:
    print("L107 pattern not found - showing repr:")
    print(repr(lines[105]), repr(lines[106]), repr(lines[107]), repr(lines[108]))
