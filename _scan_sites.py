# -*- coding: utf-8 -*-
import sys, io, re, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
root = r"addons\mcc_sandbox_mod"
# Verify each not-whitelisted function: show its remoteExec call sites
funcs = ['MCC_fnc_cas','MCC_fnc_placeConvoy','MCC_fnc_LHDspawn','MCC_fnc_boxGenerator','MCC_fnc_loadPlayer','MCC_fnc_highCommand','MCC_fnc_halt','MCC_fnc_vehicleEngine']
for fn in funcs:
    print("=== %s ===" % fn)
    for dirpath, dirs, files in os.walk(root):
        for f in files:
            if not f.endswith('.sqf'): continue
            p = os.path.join(dirpath, f)
            try:
                with open(p, 'r', encoding='utf-8', errors='replace') as fh:
                    lines = fh.readlines()
            except Exception: continue
            for i, line in enumerate(lines, 1):
                if re.search(r'remoteExec(?:Call)?\s*\[\s*"' + fn + r'"', line):
                    print("  %s L%d: %s" % (p[len(root)+1:], i, line.strip()[:90]))
