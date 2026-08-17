# -*- coding: utf-8 -*-
import sys, io, re, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
root = r"addons\mcc_sandbox_mod"
for rel in [r"definesMod.hpp", r"defines.hpp"]:
    p = os.path.join(root, rel)
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8', errors='replace') as f:
            c = f.read()
        print("=== %s (%d lines) ===" % (rel, c.count('\n')))
        for m in re.finditer(r'#include\s+"([^"]+)"', c):
            print("  include:", m.group(1))
        if 'CfgRemoteExec' in c:
            print("  HAS CfgRemoteExec!")
# Search entire repo for 'CfgRemoteExec' definition or include in any config-ish file
print("=== all files mentioning CfgRemoteExec ===")
for dirpath, dirs, files in os.walk(root):
    for fn in files:
        if not fn.endswith(('.cpp', '.hpp', '.ext')): continue
        p = os.path.join(dirpath, fn)
        try:
            with open(p, 'r', encoding='utf-8', errors='replace') as f:
                c = f.read()
        except Exception: continue
        if 'CfgRemoteExec' in c:
            print("  %s" % p[len(root)+1:])
