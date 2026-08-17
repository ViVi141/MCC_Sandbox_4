# -*- coding: utf-8 -*-
import sys, io, re, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
root = r"addons\mcc_sandbox_mod"
# find where CfgRemoteExec class is defined (config.cpp?)
for dirpath, dirs, files in os.walk(root):
    for fn in files:
        if not fn.endswith(('.cpp', '.hpp', '.ext')): continue
        p = os.path.join(dirpath, fn)
        try:
            with open(p, 'r', encoding='utf-8', errors='replace') as f:
                c = f.read()
        except Exception: continue
        if 'CfgRemoteExec' in c:
            # check for mode
            modes = re.findall(r'mode\s*=\s*\d+', c)
            print("%-55s modes: %s" % (p[len(root)+1:], modes))
        if 'class CfgRemoteExec' in c and 'mode' in c:
            m = re.search(r'class CfgRemoteExec\s*\{[^}]*mode\s*=\s*\d+', c)
            if m: print("  FOUND:", p[len(root)+1:], m.group(0)[:80])
