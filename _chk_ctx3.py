# -*- coding: utf-8 -*-
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
p = r"addons\mcc_sandbox_mod\definesMod.hpp"
with open(p, 'r', encoding='utf-8', errors='replace') as f:
    lines = f.readlines()
# find include lines and track depth properly
depth = 0
classes = []
for i, l in enumerate(lines):
    # update depth BEFORE this line's classes? include is a directive, no braces
    if 'cfgRemoteExec' in l.lower():
        print("line %d: depth before = %d, classes: %s" % (i+1, depth, [c for c, d in classes if d < depth][-4:]))
    depth += l.count('{') - l.count('}')
    cm = re.match(r'\s*class\s+(\w+)', l)
    if cm and '{' in l:
        classes.append((cm.group(1), depth))
