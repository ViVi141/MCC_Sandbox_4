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
# called functions
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
# SQF commands & keywords to exclude (not functions)
sqf_cmds = {'call','spawn','remoteExec','setDamage','setFuel','playSound','playSound3D','setOwner','setPylonLoadOut',
'setTimeMultiplier','setVehicleAmmo','setfriend','switchMove','hideObjectGlobal','lockDriver','flyInHeight','fire',
'enableEngineArtillery','say3D','addRating','addCuratorEditableObjects','removeCuratorEditableObjects','addAction'}
to_add = sorted(f for f in called - wl if f not in sqf_cmds)
print("functions to add to whitelist:", len(to_add))
for f in to_add:
    print("  class %s {allowedTargets=0;};" % f)
