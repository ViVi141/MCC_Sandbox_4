/*======================================================================= MCC_fnc_login =========================================================
	Server-side mission-maker login/logout. Do not trust client-supplied admin flags.
=================================================================================================================================================*/
#define MCCMISSIONMAKERNAME 1020
private ["_p_mcc_player","_p_mcc_player_name","_p_mcc_request","_isAdmin","_mccChat","_missionMaker","_array","_owner","_allowed","_uid","_listed"];

disableSerialization;

if (!isServer) exitWith {
	diag_log "MCC_fnc_login: rejected (server only)";
};

_p_mcc_player = _this select 0;
_p_mcc_player_name = _this select 1;
_p_mcc_request = _this select 2;
_mccChat = missionNamespace getVariable ["MCC_Chat",true];
_missionMaker = missionNamespace getVariable ["mcc_missionmaker",""];

if (isNil "_p_mcc_player" || {isNull _p_mcc_player}) exitWith {
	diag_log "MCC_fnc_login: rejected null player";
};

_owner = clientOwner;
if (isRemoteExecuted) then {
	_owner = remoteExecutedOwner;
};

if (isRemoteExecuted && {owner _p_mcc_player != _owner}) exitWith {
	diag_log "MCC_fnc_login: rejected identity mismatch";
};

_p_mcc_player_name = name _p_mcc_player;

_isAdmin = false;
if (!isMultiplayer) then {
	_isAdmin = true;
} else {
	if ((admin _owner) > 0) then {
		_isAdmin = true;
	};
	if (!isDedicated && {_owner <= 2}) then {
		_isAdmin = true;
	};
	if (!isDedicated && {!isRemoteExecuted}) then {
		_isAdmin = true;
	};
};

_allowed = missionNamespace getVariable ["MCC_allowedPlayers", ["all"]];
_uid = getPlayerUID _p_mcc_player;
_listed = true;
if (count _allowed > 0) then {
	if (!("all" in _allowed)) then {
		_listed = false;
		if (_uid in _allowed) then {
			_listed = true;
		};
		if (_p_mcc_player getVariable ["MCC_allowed", false]) then {
			_listed = true;
		};
	};
};

//MM is logging out
if (_missionMaker == _p_mcc_player_name) exitWith {
	if (_mccChat) then {
		[[if (isMultiplayer) then {netId _p_mcc_player} else {""},_p_mcc_player], format["MCC ID %1-> %2 Logged out as Misson Maker.",_p_mcc_request,mcc_missionMaker], false] remoteExec ["MCC_fnc_groupchat", 0, false];
	};
	missionNamespace setVariable ["mcc_missionmaker",""];
	unassignCurator MCC_curator;
	publicVariable "mcc_missionmaker";
	ctrlSetText [MCCMISSIONMAKERNAME, format["%1",""]];
};

//MM is logging in
if ((_missionMaker == "" && _listed) || _isAdmin) exitWith {
	missionNamespace setVariable ["mcc_missionmaker",_p_mcc_player_name];
	_missionMaker = missionNamespace getVariable ["mcc_missionmaker",""];
	if (_mccChat) then {
		[[if (isMultiplayer) then {netId _p_mcc_player} else {""},_p_mcc_player], format["MCC ID %1-> Access granted to: %2",_p_mcc_request,mcc_missionMaker], false] remoteExec ["MCC_fnc_groupchat", 0, true];
	};
	unassignCurator MCC_curator;
	sleep 0.1;
	if (!(isNil "_p_mcc_player")) then {
		_p_mcc_player assignCurator MCC_curator;
	};

	publicVariable "mcc_missionmaker";
	publicVariable "mcc_zone_pos";
	publicVariable "mcc_zone_size";
	publicVariable "mcc_zone_dir";
	publicVariable "mcc_zone_locations";
	publicVariable "MCC_zones_numbers";

	publicvariable (format ["MCC_evacVehicles_%1",playerside]);

	ctrlSetText [MCCMISSIONMAKERNAME, format["%1",_missionMaker]];

	_array = ["all","helicopterrtd","air"] call MCC_fnc_makeUnitsArray;
	_array = _array + (["all","helicopter","air"] call MCC_fnc_makeUnitsArray);

	missionNamespace setVariable ["MCC_vehicles_helicopters" ,_array];
	publicVariable "MCC_vehicles_helicopters";

	_array = ["all","airplanex","air"] call MCC_fnc_makeUnitsArray;
	_array = _array + (["all","airplane","air"] call MCC_fnc_makeUnitsArray);

	missionNamespace setVariable ["MCC_vehicles_airplanes" ,_array];
	publicVariable "MCC_vehicles_airplanes";

	_array = ["all","carx"] call MCC_fnc_makeUnitsArray;
	_array = _array + (["all","car"] call MCC_fnc_makeUnitsArray);

	missionNamespace setVariable ["MCC_vehicles_vehicles" ,_array];
	publicVariable "MCC_vehicles_vehicles";

	_array = ["all","tankx"] call MCC_fnc_makeUnitsArray;
	_array = _array + (["all","tank"] call MCC_fnc_makeUnitsArray);

	missionNamespace setVariable ["MCC_vehicles_tanks" ,_array];
	publicVariable "MCC_vehicles_tanks";

	_array = ["all","motorcyclex"] call MCC_fnc_makeUnitsArray;
	_array = _array + (["all","motorcycle"] call MCC_fnc_makeUnitsArray);

	missionNamespace setVariable ["MCC_vehicles_motorcycles" ,_array];
	publicVariable "MCC_vehicles_motorcycle";

	_array = ["all","shipx"] call MCC_fnc_makeUnitsArray;
	_array = _array + (["all","ship"] call MCC_fnc_makeUnitsArray);

	missionNamespace setVariable ["MCC_vehicles_ships" ,_array];
	publicVariable "MCC_vehicles_ships";
};
