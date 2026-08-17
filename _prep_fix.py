# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
p = r"addons\mcc_sandbox_mod\mcc\dialogs\mcc_boxGen_change.sqf"
with open(p, 'r', encoding='utf-8', errors='replace') as f:
    lines = f.readlines()

# Replace lines 201-218 (0-based 200-217) with the original e2904c0 logic
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
# verify current lines 201-218 match expected broken content
print("current 201-218:")
for i in range(200, 218):
    print(" ", i+1, lines[i].rstrip()[:70])
