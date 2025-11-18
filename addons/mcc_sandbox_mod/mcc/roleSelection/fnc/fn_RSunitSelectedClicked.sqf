/*==================================================================MCC_fnc_RSunitSelectedClicked===============================================================================
// Call from a listbox only
==============================================================================================================================================================================*/
disableSerialization;
params ["_ctrl","_index"];
private ["_data","_unit","_str"];

_data = _ctrl lbData _index;
_unit = player getVariable ["interactWith",objNull];

_ctrl ctrlShow false;
ctrlDelete _ctrl;

if (isNull _unit) exitWith {};

switch (toLower _data) do {
    case "kick": {
    	if (player == leader _unit && _unit != player) then {
			_str = "<t size='0.6' font = 'puristaLight' color='#FFFFFF'>" + format ["%1 kicked %2 from the squad",name player, name _unit] + "</t>";
if (!(isNull _unit)) then {
[[_str,0,0.2,5,1,0.0], "bis_fnc_dynamictext", group _unit, false] remoteExec ["bis_fnc_dynamictext", group _unit, false];
};
};
			[_unit] join grpNull;

            if ((missionNamespace getVariable ["CP_activated",false]) && isPlayer _unit) then {
if (!(isNull _unit)) then {
[[], "MCC_fnc_setGear", _unit, false] remoteExec ["MCC_fnc_setGear", _unit, false];
};
};
            };
		};
    

    case "commander": {
    	if (player == leader _unit && _unit != player) then {
if (!(isNull _unit)) then {
[[_unit, {(group (_this select 0)) selectLeader (_this select 0);}], "bis_fnc_spawn", group _unit, false] remoteExec ["bis_fnc_spawn", 0, false];
};
};
    	};
    

    case "teleport": {
    	if ((missionNamespace getVariable ["MCC_teleportToTeam",false]) && _unit in (units player) && _unit != player) then {
    		[_unit] execVM format ["%1mcc\general_scripts\mcc_SpawnToPosition.sqf",MCC_path];
    	};
    };
