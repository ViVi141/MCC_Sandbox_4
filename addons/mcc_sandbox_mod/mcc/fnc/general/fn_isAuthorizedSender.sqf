//==================================================================MCC_fnc_isAuthorizedSender======================================================================================
// True if this invocation is local, came from the server, a logged-in admin, or the current mission maker.
//==============================================================================================================================================================================
if (!isRemoteExecuted) exitWith { true };

private _owner = remoteExecutedOwner;
if (_owner == 2) exitWith { true };
if (isServer && {(admin _owner) > 0}) exitWith { true };

private _mm = missionNamespace getVariable ["mcc_missionmaker", ""];
if (_mm == "") exitWith { false };

private _ok = false;
{
	if (owner _x == _owner) then {
		if (name _x == _mm) then {
			_ok = true;
		};
	};
} forEach allPlayers;

_ok
