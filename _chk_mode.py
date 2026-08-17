# -*- coding: utf-8 -*-
import sys, io, re, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
root = r"addons\mcc_sandbox_mod"
# check config.cpp for CfgRemoteExec include
p = os.path.join(root, 'config.cpp')
with open(p, 'r', encoding='utf-8', errors='replace') as f:
    c = f.read()
print("config.cpp has CfgRemoteExec:", 'CfgRemoteExec' in c)
for m in re.finditer(r'#include\s+"([^"]*CfgRemoteExec[^"]*)"', c):
    print("  include:", m.group(1))
# check aas and radio CfgRemoteExec heads
for rel in [r"mcc\aas\CfgRemoteExec.hpp", r"mcc\radio\CfgRemoteExec.hpp", r"mcc\cfg\CfgRemoteExec.hpp"]:
    p2 = os.path.join(root, rel)
    with open(p2, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()
    print("=== %s (%d lines) ===" % (rel, len(lines)))
    print("  head:", lines[0].strip()[:60] if lines else "")
    for l in lines[:8]:
        print("   ", l.strip()[:60])
