//==================================================================MCC_fnc_globalSay3D======================================================================================
// Say sound on 3d on all clients
if (!(isNull _unit)) then {
    [[[netid _unit,_unit], _sound] remoteExec ["MCC_fnc_globalSay3D", 0, false]];
};
// Params: 
//	_unit: object, sound's source
// 	_sound: string, sound define in config
//==============================================================================================================================================================================	
private ["_object","_sound"];

_sound = _this select 1;
_object = if(((_this select 0) select 0) == "") then {(_this select 0) select 1} else {objectFromNetID ((_this select 0) select 0)};
_object say3D _sound;
