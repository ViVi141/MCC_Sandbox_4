# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
p = r"addons\mcc_sandbox_mod\mcc\cfg\cfgRemoteExec.hpp"
with open(p, 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

additions = """//BIS functions used via remoteExec
class BIS_fnc_BoatRack01Init {allowedTargets=0;};
class BIS_fnc_Carrier01Init {allowedTargets=0;};
class BIS_fnc_Destroyer01Init {allowedTargets=0;};
class BIS_fnc_endMissionServer {allowedTargets=0;};
class BIS_fnc_holdActionAdd {allowedTargets=0;};
class BIS_fnc_markerCreate {allowedTargets=0;};
class BIS_fnc_respawnTickets {allowedTargets=0;};
class BIS_fnc_showNotification {allowedTargets=0;};
class BIS_fnc_showSubtitle {allowedTargets=0;};
class BIS_fnc_spawn {allowedTargets=0;};
class bis_fnc_call {allowedTargets=0;};
class bis_fnc_counter {allowedTargets=0;};
class bis_fnc_dynamictext {allowedTargets=0;};
class bis_fnc_halt {allowedTargets=0;};
class bis_fnc_holdActionAdd {allowedTargets=0;};
class bis_fnc_initVehicle {allowedTargets=0;};
class bis_fnc_moduleMissionName {allowedTargets=0;};
class bis_fnc_sayMessage {allowedTargets=0;};
class bis_fnc_showNotification {allowedTargets=0;};
class bis_fnc_spawn {allowedTargets=0;};
class CUP_fnc_detachFromShip {allowedTargets=0;};
//MCC functions used via remoteExec
class MCC_fnc_AAS_drawLine {allowedTargets=0;};
class MCC_fnc_AASmarkers {allowedTargets=0;};
class MCC_fnc_AIHeal {allowedTargets=0;};
class MCC_fnc_LHDspawn {allowedTargets=0;};
class MCC_fnc_MWObjectiveLogistics {allowedTargets=0;};
class MCC_fnc_MusicTrigger {allowedTargets=0;};
class MCC_fnc_aas_AIspawn {allowedTargets=0;};
class MCC_fnc_addVelocity {allowedTargets=0;};
class MCC_fnc_ambientBirdsSpawnInit {allowedTargets=0;};
class MCC_fnc_ambientFireClientSide {allowedTargets=0;};
class MCC_fnc_ambientFirePlayerFiredEH {allowedTargets=0;};
class MCC_fnc_ambientFireStart {allowedTargets=0;};
class MCC_fnc_cas {allowedTargets=0;};
class MCC_fnc_clearPersistentData {allowedTargets=0;};
class MCC_fnc_fastRopeLocal {allowedTargets=0;};
class MCC_fnc_groupchat {allowedTargets=0;};
class MCC_fnc_halt {allowedTargets=0;};
class MCC_fnc_highCommand {allowedTargets=0;};
class MCC_fnc_loadPlayer {allowedTargets=0;};
class MCC_fnc_loadServer {allowedTargets=0;};
class MCC_fnc_placeConvoy {allowedTargets=0;};
class MCC_fnc_savePlayer {allowedTargets=0;};
class MCC_fnc_spawnCratesInHouses {allowedTargets=0;};
class MCC_fnc_startConvoy {allowedTargets=0;};
class MCC_fnc_vehicleEngine {allowedTargets=0;};
class MCC_fnc_vehicleLights {allowedTargets=0;};
class MCC_fnc_wakeUp {allowedTargets=0;};
class mcc_fnc_login {allowedTargets=0;};
class mcc_setup {allowedTargets=0;};
class mcc_setup_hc {allowedTargets=0;};
"""
content = content.rstrip() + '\n' + additions
with open(p, 'w', encoding='utf-8', errors='replace') as f:
    f.write(content)
print("added 51 whitelist entries")
