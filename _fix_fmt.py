# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# 1. mcc_factions.sqf L24: 6 placeholders, 5 args -> add missing or fix placeholder
p = r"addons\mcc_sandbox_mod\mcc\pop_menu\mcc_factions.sqf"
with open(p, 'r', encoding='utf-8', errors='replace') as f:
    c = f.read()
old = 'diag_log format ["factions: [%1] - [%2] - [%3] - [%4] - [%5] - [%6]", _unitCfg, _cfgname, _cfgdisplayname, _side, _sidename];  //DEBUG'
new = 'diag_log format ["factions: [%1] - [%2] - [%3] - [%4] - [%5]", _unitCfg, _cfgname, _cfgdisplayname, _side, _sidename];  //DEBUG'
if old in c:
    c = c.replace(old, new, 1)
    with open(p, 'w', encoding='utf-8', errors='replace') as f:
        f.write(c)
    print("mcc_factions fixed (removed stray %6)")
else:
    print("mcc_factions pattern not found")

# 2. fn_initCuratorAttribute.sqf L16: %1_%2 but 1 arg
p2 = r"addons\mcc_sandbox_mod\mcc\UI\fnc\fn_initCuratorAttribute.sqf"
with open(p2, 'r', encoding='utf-8', errors='replace') as f:
    c2 = f.read()
old2 = '_fncFile = format ["scriptname \'%1_%2\'; _fnc_scriptName = \'%1\';",_fncName] + _fncFile;'
new2 = '_fncFile = format ["scriptname \'%1\'; _fnc_scriptName = \'%1\';",_fncName] + _fncFile;'
if old2 in c2:
    c2 = c2.replace(old2, new2, 1)
    with open(p2, 'w', encoding='utf-8', errors='replace') as f:
        f.write(c2)
    print("fn_initCuratorAttribute fixed (removed %2)")
else:
    print("initCuratorAttribute pattern not found - showing:")
    for i, l in enumerate(c2.split('\n')[:18], 1):
        print("  ", i, repr(l))
