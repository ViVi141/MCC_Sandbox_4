# -*- coding: utf-8 -*-
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
# Check the include context in definesMod.hpp around cfgRemoteExec includes
p = r"addons\mcc_sandbox_mod\definesMod.hpp"
with open(p, 'r', encoding='utf-8', errors='replace') as f:
    lines = f.readlines()
# find the cfgRemoteExec includes and show surrounding context
for i, l in enumerate(lines):
    if 'cfgRemoteExec' in l.lower():
        print("=== context around line %d ===" % (i+1))
        for j in range(max(0, i-6), min(len(lines), i+4)):
            print("  %d: %s" % (j+1, lines[j].rstrip()[:80]))
        print()
