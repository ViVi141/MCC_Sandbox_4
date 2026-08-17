# -*- coding: utf-8 -*-
import sys, io, re, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
root = r"addons\mcc_sandbox_mod"
# search all files for include of CfgRemoteExec or definition of class CfgRemoteExec
for dirpath, dirs, files in os.walk(root):
    for fn in files:
        if not fn.endswith(('.cpp', '.hpp', '.ext')): continue
        p = os.path.join(dirpath, fn)
        try:
            with open(p, 'r', encoding='utf-8', errors='replace') as f:
                c = f.read()
        except Exception: continue
        for m in re.finditer(r'#include\s+"[^"]*CfgRemoteExec[^"]*"', c):
            print("INCLUDE: %s -> %s" % (p[len(root)+1:], m.group(0)))
        if 'class CfgRemoteExec' in c:
            print("DEFINE: %s" % p[len(root)+1:])
# check config.cpp includes at all
p = os.path.join(root, 'config.cpp')
with open(p, 'r', encoding='utf-8', errors='replace') as f:
    c = f.read()
print("=== config.cpp includes ===")
for m in re.finditer(r'#include\s+"([^"]+)"', c):
    print("  ", m.group(1))
