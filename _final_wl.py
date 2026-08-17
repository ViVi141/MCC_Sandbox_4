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
sqf_cmds = {'call','spawn','remoteExec','setDamage','setFuel','playSound','playSound3D','setOwner','setPylonLoadOut',
'setTimeMultiplier','setVehicleAmmo','setfriend','switchMove','hideObjectGlobal','lockDriver','flyInHeight','fire',
'enableEngineArtillery','say3D','addRating','addCuratorEditableObjects','removeCuratorEditableObjects','addAction',
'detach','setVariable','setGroupId','setWaypointType','enableSimulation','setCaptive','setBehaviour','setCombatMode',
'setSpeedMode','setFormation','setWaypointSpeed','setWaypointBehaviour','setWaypointCombatMode','setWaypointFormation',
'createVehicle','createGroup','createUnit','addWeapon','addMagazine','addItem','addBackpack','removeAllWeapons',
'setUnitPos','setAnimSpeedCoef','switchCamera','addMPEventHandler','removeAllMPEventHandlers','setVehicleAmmoDef',
'selectWeapon','addPrimaryWeaponItem','addSecondaryWeaponItem','addHandgunItem','addHeadgear','addGoggles',
'setFace','setSpeaker','setIdentity','setName','setVehicleVarName','setPilotLight','setCollisionLight',
'setCustomLightControllerLightColor','setCustomLightControllerLightFlareSize','setCustomLightControllerLightIntensity',
'setCustomLightControllerLightAttenuation','setLightAttenuation','setLightBrightness','setLightColor',
'setLightFlareSize','setLightFlareMaxDistance','setLightIntensity','setLightUseFlare','setLightDayLight',
'forceWeaponFire','setMarkerPos','setMarkerType','setMarkerColor','setMarkerSize','setMarkerText','setMarkerShape',
'setMarkerDir','setMarkerAlpha','setMarkerBrush','setMarkerShadow','createMarker','deleteMarker','createMarkerLocal',
'setGroupOwner','groupOwner','setWaypointPosition','setWaypointCompletionRadius','setWaypointStatements',
'addWaypoint','waypoints','currentWaypoint','deleteWaypoint','setCurrentWaypoint','synchronizeObjectsA',
'synchronizeObjectsB','synchronizeTrigger','setTriggerStatements','setTriggerActivation','setTriggerArea',
'setTriggerInterval','setTriggerTimeout','setTriggerText','setTriggerType','setTriggerAmmo','setTriggerServerOnly',
'setTriggerStatementsRemote','removeAllEventHandlers','removeEventHandler','addEventHandler','setObjectTexture',
'setObjectMaterial','setObjectTextureGlobal','setObjectMaterialGlobal','setDamage','setFuel','setVehicleAmmo',
'lock','lockTurret','lockDriver','enableWeaponDisassembly','enableSimulationGlobal','allowDamage',
'setDammage','setVehicleLock','setUnloadInCombat','setAllowDamage','enableRopeAttach','enableVehicleCargo',
'disableCollisionWith','setSimpleTask','setTaskState','setTaskDescription','setTaskDestination','setCurrentTask',
'assignTask','taskComplete','taskHint','taskSetCurrent','terminate','setQueueRadio','radioChannelCreate',
'radioChannelAdd','radioChannelRemove','radioChannelSetLabel','radioChannelSetCallSign','setChannelAllowed',
'enableChannel','setRadioMsg','setBroadcastMsg','setGroupRadioMsg','setSideRadioMsg','setGlobalRadioMsg',
'customChat','sideChat','groupChat','globalChat','vehicleChat','systemChat','directSay','say','say2D','say3D',
'setRandomLip','setSpeaker','setPitch','setVolume','fadeMusic','playMusic','stopMusic','fadeSound','playSound',
'playSound3D','soundVolume','musicVolume','enableEnvironment','setViewDistance','setTerrainGrid','setObjectViewDistance',
'setShadowDistance','setPiPEffect','setPiPEffectToys','cameraEffect','camUseNVG','camTarget','camCommit',
'camSetPos','camSetDir','camSetTarget','camSetFov','camSetFovRange','camSetFocus','camSetDive','camSetRelPos',
'camSetRelDir','camSetRelTarget','camSetSpeed','camSetTime','camSetCommand','camDestroy','camCreate',
'attachTo','detach','setPos','setPosASL','setPosATL','setPosASLW','setDir','setVectorDir','setVectorUp',
'setVelocity','setVelocityTransformation','setVelocityModelSpace','setVelocityRandom','setSpeed','setPitchBank',
'setVectorDirAndUp','setCenterOfMass','setMass','setDensity','setBuoyancy','setThrustFactor','setDragCoef',
'setAngularDragCoef','setThrustVector','setBrakes','setBattery','setFuel','setAmmo','setDamage','setRepairCargo',
'createSimpleObject','createSimpleObject','createVehicle','createVehicleLocal','createVehicleCrew','createUnit',
'createGroup','createCenter','createMarker','createTrigger','createDiaryRecord','createDiarySubject',
'setSimpleTaskDestination','setSimpleTaskDescription','setSimpleTaskState','setSimpleTaskType','setSimpleTaskTarget',
'setTaskType','setTaskTarget','setTaskPriority','setTaskAlwaysVisible','setTaskAutoTargeting',
}
not_wl = sorted(f for f in called - wl if f not in sqf_cmds and not f[0].isdigit())
print("called:", len(called), "whitelisted:", len(wl))
print("still not whitelisted (functions):", len(not_wl))
for f in not_wl:
    print("  ", f)
