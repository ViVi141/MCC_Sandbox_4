# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
p = r"addons\mcc_sandbox_mod\mcc\dialogs\mcc_boxGen_change.sqf"
with open(p, 'r', encoding='utf-8', errors='replace') as f:
    lines = f.readlines()
for i in range(214, min(225, len(lines))):
    print(i+1, repr(lines[i]))
