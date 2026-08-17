# -*- coding: utf-8 -*-
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
p = r"addons\mcc_sandbox_mod\definesMod.hpp"
with open(p, 'r', encoding='utf-8', errors='replace') as f:
    lines = f.readlines()
# show first 20 lines and locate the class structure
print("=== head ===")
for i in range(0, min(20, len(lines))):
    print("%d: %s" % (i+1, lines[i].rstrip()[:90]))
# find what class contains the remoteexec includes - track brace depth & class names
print("=== class tracking around remoteexec includes ===")
depth = 0
class_stack = []
for i, l in enumerate(lines):
    cm = re.match(r'\s*class\s+(\w+)', l)
    if cm and '{' in l:
        class_stack.append((cm.group(1), depth, i+1))
    depth += l.count('{') - l.count('}')
    if 'cfgRemoteExec' in l.lower():
        print("  include at line %d, depth %d, class stack: %s" % (i+1, depth, class_stack[-3:]))
