# -*- coding: utf-8 -*-
import sys, io, re, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
root = r"addons\mcc_sandbox_mod"
# For each potentially-missing function, search the whole tree for the fn file case-insensitively
missing = [
('garrisonBehavior', r"mcc\ai\fnc"),
('ambientInit', r"mcc\ambient\fnc"),
('pre_init', r"mcc\fnc\general"),
('IedFakeExplosion', r"mcc\fnc\ied"),
('CreateAmmoDrop', r"mcc\fnc\cas"),
('CBU', r"mcc\fnc\artillery"),
('groupGenRefresh', r"mcc\fnc\groupGen"),
('consoleClickGroupIcon', r"mcc\fnc\console"),
('vote', r"mcc\fnc\mp"),
('ilsChilds', r"mcc\fnc\actions"),
('evacDelete', r"mcc\fnc\evac"),
('initDynamicDialog', r"mcc\fnc\dynamicDialog"),
('addToZeus', r"mcc\cfg\curator\fnc"),
('moduleSector', r"mcc\cfg\modules\fnc"),
('compositionsGrab', r"mcc\compositions\fnc"),
('heliOpenCloseDoor', r"mcc\helicopters\fnc"),
('helpersInit', r"mcc\helpers\fnc"),
('interaction', r"mcc\interaction\fnc"),
('LHDspawn', r"mcc\lhd\fnc"),
('loadTruckUI', r"mcc\logistics\fnc"),
('initMedic', r"mcc\medic\fnc"),
('MWFindMissionCenter', r"mcc\missionWizard\fnc"),
('vonRadio', r"mcc\radio\fnc"),
('roadNetworkFind', r"mcc\roads\fnc"),
('unlock', r"mcc\roleSelection\fnc"),
('rtsScanResourcesBasic', r"mcc\rts\fnc\missions"),
('surviveInit', r"mcc\survive\fnc"),
('countDownLine', r"mcc\ui\fnc"),
('BISGarage', r"mcc\vehicles\fnc"),
]
for name, fdir in missing:
    # search case-insensitive for fn_<name>.sqf anywhere
    found = []
    target_dir = os.path.join(root, fdir.replace('\\', os.sep))
    if os.path.isdir(target_dir):
        for fn in os.listdir(target_dir):
            if fn.lower() == ('fn_' + name + '.sqf').lower():
                found.append(fn)
    print("%-28s in %-35s -> %s" % (name, fdir, found if found else "**MISSING**"))
