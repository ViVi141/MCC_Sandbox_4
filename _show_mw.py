# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
p = r"addons\mcc_sandbox_mod\mcc\missionWizard\fnc\fn_MWSpawnInZone.sqf"
with open(p, 'r', encoding='utf-8', errors='replace') as f:
    lines = f.readlines()
print("total:", len(lines))
for i in range(97, 120):
    print(i+1, repr(lines[i]))
