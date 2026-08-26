//==================================================================MCC_fnc_FPS======================================================================================
// Start / stop the FPS benchmark overlay on the server or Headless Client.
//==============================================================================================================================================================================
params [
	["_mode", 1, [0]]
];

if (!(isServer || {missionNamespace getVariable ["MCC_isLocalHC", false]})) exitWith {};

if (isNil "mcc_fps_running") then {
	mcc_fps_running = false;
};

private _path = missionNamespace getVariable ["MCC_path", ""];
if (_path == "") then {
	if (isClass (configFile >> "CfgPatches" >> "mcc_sandbox")) then {
		_path = "\mcc_sandbox_mod\";
	};
};

[_mode] execVM (_path + "mcc\pop_menu\fps_benchmark.sqf");
