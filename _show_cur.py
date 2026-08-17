# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
p = r"addons\mcc_sandbox_mod\mcc\dialogs\mcc_boxGen_change.sqf"
with open(p, 'r', encoding='utf-8', errors='replace') as f:
    lines = f.readlines()
print("total lines:", len(lines))
# show current 196-220 with repr
for i in range(195, min(220, len(lines))):
    print(i+1, repr(lines[i]))
