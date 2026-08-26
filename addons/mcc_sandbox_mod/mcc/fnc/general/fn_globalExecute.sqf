//==================================================================MCC_fnc_globalExecute======================================================================================
// Global execute a command on selected clients or server
// Example: [mode, code] remoteExec ["MCC_fnc_globalExecute", 0];
// Params:
//	mode: number, 0:clients only, 1: server only 2: all clients and server
//	code: code, code to be executed
// Only the server, logged-in admin, or current mission maker may invoke this remotely.
//==============================================================================================================================================================================
if !(call MCC_fnc_isAuthorizedSender) exitWith {
	diag_log "MCC_fnc_globalExecute: rejected unauthorized remoteExec";
};

private ["_code","_type"];

_type 	= _this select 0;
_code 	= _this select 1;

switch (_type) do {
	case 0:
	{
		if (!isServer) then {call _code};
	};

	case 1:
	{
		if (isServer) then {call _code};
	};

	case 2:
	{
		call _code;
	};
};
