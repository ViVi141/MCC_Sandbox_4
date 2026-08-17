# -*- coding: utf-8 -*-
import sys, io, re, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
root = r"addons\mcc_sandbox_mod"
wl = set()
for rel in [r"mcc\cfg\cfgRemoteExec.hpp", r"mcc\radio\cfgRemoteExec.hpp", r"mcc\AAS\cfgRemoteExec.hpp"]:
    with open(os.path.join(root, rel), 'r', encoding='utf-8', errors='replace') as fh:
        c = fh.read()
    for m in re.finditer(r'class\s+([A-Za-z0-9_]+)\s*\{', c):
        wl.add(m.group(1))
# check if BIS_fnc variants already there in any case
for fn in ['BIS_fnc_spawn','bis_fnc_spawn','BIS_fnc_showNotification','bis_fnc_showNotification','BIS_fnc_holdActionAdd','bis_fnc_holdActionAdd','BIS_fnc_markerCreate','BIS_fnc_endMissionServer']:
    lower = fn.lower()
    in_wl = [w for w in wl if w.lower() == lower]
    print("%-30s in whitelist (case-insens): %s" % (fn, in_wl))
