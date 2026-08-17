# -*- coding: utf-8 -*-
import sys, io, re, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
root = r"addons\mcc_sandbox_mod"
# Check each not-whitelisted function has a fn file somewhere
funcs = ['MCC_fnc_AAS_drawLine','MCC_fnc_AASmarkers','MCC_fnc_AIHeal','MCC_fnc_LHDspawn','MCC_fnc_MWObjectiveLogistics',
'MCC_fnc_MusicTrigger','MCC_fnc_aas_AIspawn','MCC_fnc_addVelocity','MCC_fnc_ambientBirdsSpawnInit','MCC_fnc_ambientFireClientSide',
'MCC_fnc_ambientFirePlayerFiredEH','MCC_fnc_ambientFireStart','MCC_fnc_boxGenerator','MCC_fnc_cas','MCC_fnc_clearPersistentData',
'MCC_fnc_fastRopeLocal','MCC_fnc_groupchat','MCC_fnc_halt','MCC_fnc_highCommand','MCC_fnc_loadPlayer','MCC_fnc_loadServer',
'MCC_fnc_placeConvoy','MCC_fnc_savePlayer','MCC_fnc_spawnCratesInHouses','MCC_fnc_startConvoy','MCC_fnc_vehicleEngine',
'MCC_fnc_vehicleLights','MCC_fnc_wakeUp']
for fn in funcs:
    short = fn.replace('MCC_fnc_', '')
    found = []
    for dirpath, dirs, files in os.walk(root):
        for f in files:
            if f.lower() == ('fn_' + short + '.sqf').lower():
                found.append(os.path.join(dirpath, f)[len(root)+1:])
    if not found:
        # search for function definition "X = {" or fn_X = compile
        print("%-35s -> FILE MISSING! (searching defs...)" % fn)
    else:
        print("%-35s -> %s" % (fn, found[0]))
