# -*- coding: utf-8 -*-
import sys, io, re, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
root = r"addons\mcc_sandbox_mod"
# MWObjectiveLogistics call site
print("=== MWObjectiveLogistics refs ===")
for dirpath, dirs, files in os.walk(root):
    for f in files:
        if not f.endswith('.sqf'): continue
        p = os.path.join(dirpath, f)
        try:
            with open(p, 'r', encoding='utf-8', errors='replace') as fh:
                c = fh.read()
        except Exception: continue
        if 'MWObjectiveLogistics' in c:
            for i, l in enumerate(c.split('\n'), 1):
                if 'MWObjectiveLogistics' in l:
                    print("  %s L%d: %s" % (p[len(root)+1:], i, l.strip()[:90]))
# Also verify the earlier "called but not whitelisted" list - check which are actually needed in whitelist
# The whitelist mode=1 means ONLY whitelisted functions can be remoteExec'd.
# Some called functions are BI functions (BIS_fnc_*) - these need whitelisting too if mode=1!
print("=== BIS_fnc_* called but not whitelisted (critical!) ===")
wl = set()
for rel in [r"mcc\cfg\cfgRemoteExec.hpp", r"mcc\radio\cfgRemoteExec.hpp", r"mcc\AAS\cfgRemoteExec.hpp"]:
    with open(os.path.join(root, rel), 'r', encoding='utf-8', errors='replace') as fh:
        c = fh.read()
    for m in re.finditer(r'class\s+([A-Za-z0-9_]+)\s*\{', c):
        wl.add(m.group(1))
called = set()
for dirpath, dirs, files in os.walk(root):
    for f in files:
        if not f.endswith('.sqf'): continue
        p = os.path.join(dirpath, f)
        try:
            with open(p, 'r', encoding='utf-8', errors='replace') as fh:
                c = fh.read()
        except Exception: continue
        for m in re.finditer(r'remoteExec(?:Call)?\s*\[\s*"([^"]+)"', c):
            called.add(m.group(1))
bis_called = sorted(f for f in called if f.startswith('BIS_'))
bis_not_wl = sorted(f for f in bis_called if f not in wl)
print("BIS called:", len(bis_called), "not whitelisted:", len(bis_not_wl))
for f in bis_not_wl:
    print("  ", f)
