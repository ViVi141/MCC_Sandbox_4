//==================================================================MCC_fnc_setTime======================================================================================
// Setstime on all clients
if (!(isNull _time)) then {
    [_time] remoteExec ["MCC_fnc_setTime", 0, false];
};
//	year: number, YYYY
//	month: number, MM
//	day: number, DD
//	hour: number, HH
// 	minute: number, mm
//==============================================================================================================================================================================	

private ["_time"];

_time = _this select 0;
setDate _time;
