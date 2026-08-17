# -*- coding: utf-8 -*-
import sys, io, re, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
root = r"addons\mcc_sandbox_mod"
# Whitelisted function names from all 3 cfgRemoteExec.hpp (inside class Functions)
whitelist = set()
for rel in [r"mcc\cfg\cfgRemoteExec.hpp", r"mcc\radio\cfgRemoteExec.hpp", r"mcc\AAS\cfgRemoteExec.hpp"]:
    p = os.path.join(root, rel)
    with open(p, 'r', encoding='utf-8', errors='replace') as f:
        c = f.read()
    for m in re.finditer(r'class\s+([A-Za-z0-9_]+)\s*\{', c):
        whitelist.add(m.group(1))
print("whitelist size:", len(whitelist))

# All remoteExec / remoteExecCall / spawn BIS_fnc_MP function names in code
called = set()
for dirpath, dirs, files in os.walk(root):
    for fn in files:
        if not fn.endswith('.sqf'): continue
        p = os.path.join(dirpath, fn)
        try:
            with open(p, 'r', encoding='utf-8', errors='replace') as f:
                c = f.read()
        except Exception: continue
        for m in re.finditer(r'remoteExec(?:Call)?\s*\[\s*"([^"]+)"', c):
            called.add(m.group(1))
        # function via variable: remoteExec [var, ...] - skip
print("called size:", len(called))

# MCC_fnc_* called but not whitelisted
mcc_called = sorted(f for f in called if f.startswith('MCC_') or f.startswith('GAIA_'))
mcc_not_wl = sorted(f for f in mcc_called if f not in whitelist)
print("MCC/GAIA called:", len(mcc_called))
print("MCC/GAIA called but NOT whitelisted:", len(mcc_not_wl))
for f in mcc_not_wl:
    print("  ", f)
