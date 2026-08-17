# -*- coding: utf-8 -*-
import sys, io, re, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
root = r"addons\mcc_sandbox_mod"
# Re-scan after fixing extras handler: functions still called via remoteExec not in whitelist
wl = set()
for rel in [r"mcc\cfg\cfgRemoteExec.hpp", r"mcc\radio\cfgRemoteExec.hpp", r"mcc\AAS\cfgRemoteExec.hpp"]:
    with open(os.path.join(root, rel), 'r', encoding='utf-8', errors='replace') as fh:
        c = fh.read()
    for m in re.finditer(r'class\s+([A-Za-z0-9_]+)\s*\{', c):
        wl.add(m.group(1))
called = set()
sites = {}
for dirpath, dirs, files in os.walk(root):
    for f in files:
        if not f.endswith('.sqf'): continue
        p = os.path.join(dirpath, f)
        try:
            with open(p, 'r', encoding='utf-8', errors='replace') as fh:
                lines = fh.readlines()
        except Exception: continue
        for i, line in enumerate(lines, 1):
            for m in re.finditer(r'remoteExec(?:Call)?\s*\[\s*"([^"]+)"', line):
                called.add(m.group(1))
                sites.setdefault(m.group(1), []).append((p[len(root)+1:], i))
not_wl = sorted(called - wl)
print("called:", len(called), "whitelisted:", len(wl))
print("called but NOT whitelisted:", len(not_wl))
for fn in not_wl:
    print("  %-30s %d sites" % (fn, len(sites[fn])))
