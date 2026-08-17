# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
p = r"addons\mcc_sandbox_mod\mcc\pv_handling\mcc_extras_pv_handler.sqf"
with open(p, 'r', encoding='utf-8', errors='replace') as f:
    lines = f.readlines()
print("total:", len(lines))
# Show lines 13-66 with repr for exact fix
for i in range(12, min(66, len(lines))):
    print(i+1, repr(lines[i]))
