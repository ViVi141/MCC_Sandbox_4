# -*- coding: utf-8 -*-
import sys, io, re, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
root = r"addons\mcc_sandbox_mod"
for fn in ['MCC_fnc_MWObjectiveLogistics','MCC_fnc_boxGenerator','MCC_fnc_highCommand','MCC_fnc_placeConvoy','MCC_fnc_startConvoy']:
    short = fn.replace('MCC_fnc_', '')
    print("=== %s ===" % fn)
    found = []
    for dirpath, dirs, files in os.walk(root):
        for f in files:
            if not f.endswith('.sqf'): continue
            p = os.path.join(dirpath, f)
            try:
                with open(p, 'r', encoding='utf-8', errors='replace') as fh:
                    c = fh.read()
            except Exception: continue
            # definition patterns: "fn_X = {" or "X = {" or "MCC_fnc_X = "
            if re.search(r'\b' + fn + r'\s*=', c) or re.search(r'\bfn_' + short + r'\s*=\s*\{', c):
                # find line
                for i, l in enumerate(c.split('\n'), 1):
                    if re.search(r'\b' + fn + r'\s*=', l) or re.search(r'\bfn_' + short + r'\s*=', l):
                        found.append((p[len(root)+1:], i, l.strip()[:70]))
                        break
    if found:
        for f in found[:3]:
            print("  ", f)
    else:
        print("   NOT DEFINED ANYWHERE - potential missing function!")
