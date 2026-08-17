# -*- coding: utf-8 -*-
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
p = r"addons\mcc_sandbox_mod\mcc\cfg\cfgRemoteExec.hpp"
with open(p, 'r', encoding='utf-8', errors='replace') as f:
    lines = f.readlines()
print("total lines:", len(lines))
print("=== head ===")
for i in range(0, 5):
    print("%d: %s" % (i+1, lines[i].rstrip()))
print("=== tail ===")
for i in range(len(lines)-5, len(lines)):
    print("%d: %s" % (i+1, lines[i].rstrip()))
# check if wrapped in class CfgRemoteExec
print("has 'class CfgRemoteExec':", any('class CfgRemoteExec' in l for l in lines))
# brace balance of the file itself
depth = 0
for l in lines:
    depth += l.count('{') - l.count('}')
print("file brace depth:", depth)
