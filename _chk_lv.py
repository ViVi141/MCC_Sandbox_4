# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
for rel in [r"gaia\functions\ambient\fn_ambientCombat.sqf", r"gaia\functions\ambient\fn_ambientCombatServer.sqf"]:
    p = r"addons\mcc_sandbox_mod" + '\\' + rel
    with open(p, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()
    print("=== %s ===" % rel)
    for i in range(0, 14):
        if i < len(lines):
            print("  L%d: %s" % (i+1, lines[i].rstrip()[:100]))
