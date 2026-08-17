# -*- coding: utf-8 -*-
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# 1. spawn_group3d.sqf L33: inside format string
p = r"addons\mcc_sandbox_mod\mcc\pop_menu\spawn_group3d.sqf"
with open(p, 'r', encoding='utf-8', errors='replace') as f:
    c = f.read()
old = "if (!(isNull MCC3DValue select 0)) then { [%1, %2, '%3', '%4', '%5', %6, '%7', '%8', %9] remoteExec ['MCC_fnc_simpleSpawn', 0, false]; };"
new = "if (!(isNull MCC3DValue)) then { [%1, %2, '%3', '%4', '%5', %6, '%7', '%8', %9] remoteExec ['MCC_fnc_simpleSpawn', 0, false]; };"
if old in c:
    c = c.replace(old, new, 1)
    with open(p, 'w', encoding='utf-8', errors='replace') as f:
        f.write(c)
    print("spawn_group3d L33 fixed")
else:
    print("spawn_group3d NOT FOUND")

# 2. fn_MWSpawnInZone.sqf L100/L109: _ar select 0 is string - remove isNull
p2 = r"addons\mcc_sandbox_mod\mcc\missionWizard\fnc\fn_MWSpawnInZone.sqf"
with open(p2, 'r', encoding='utf-8', errors='replace') as f:
    c2 = f.read()
old2 = "if (!(isNull _ar select 0)) then {\n[_ar, \"mcc_setup\", false, false] remoteExec [\"mcc_setup\", 2, false];\n};\n"
new2 = "[_ar, \"mcc_setup\", false, false] remoteExec [\"mcc_setup\", 2, false];\n"
n = c2.count(old2)
if n:
    c2 = c2.replace(old2, new2)
    with open(p2, 'w', encoding='utf-8', errors='replace') as f:
        f.write(c2)
    print("fn_MWSpawnInZone fixed x", n)
else:
    print("fn_MWSpawnInZone NOT FOUND")

# 3. fn_buildSpawnPoint.sqf L3: _this select 0 is pos array
p3 = r"addons\mcc_sandbox_mod\mcc\roleSelection\fnc\fn_buildSpawnPoint.sqf"
with open(p3, 'r', encoding='utf-8', errors='replace') as f:
    c3 = f.read()
old3 = "if (!(isNull _this select 0)) then {\n[[pos, dir, side, size, destructable], \"MCC_fnc_buildSpawnPoint\", false, false] remoteExec [\"MCC_fnc_buildSpawnPoint\", 2, false];\n};\n"
new3 = "[[pos, dir, side, size, destructable], \"MCC_fnc_buildSpawnPoint\", false, false] remoteExec [\"MCC_fnc_buildSpawnPoint\", 2, false];\n"
if old3 in c3:
    c3 = c3.replace(old3, new3, 1)
    with open(p3, 'w', encoding='utf-8', errors='replace') as f:
        f.write(c3)
    print("fn_buildSpawnPoint fixed")
else:
    print("fn_buildSpawnPoint NOT FOUND - showing L1-8")
    for i, l in enumerate(c3.split('\n')[:8], 1):
        print("  ", i, repr(l))
