# -*- coding: utf-8 -*-
import sys, io, re, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
root = r"addons\mcc_sandbox_mod"
for fn in ['BIS_fnc_spawn', 'BIS_fnc_showNotification', 'BIS_fnc_holdActionAdd', 'BIS_fnc_markerCreate']:
    print("=== %s ===" % fn)
    cnt = 0
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
                    cnt += 1
                    if cnt <= 3:
                        print("  %s L%d: %s" % (p[len(root)+1:], i, line.strip()[:80]))
    print("  total calls:", cnt)
