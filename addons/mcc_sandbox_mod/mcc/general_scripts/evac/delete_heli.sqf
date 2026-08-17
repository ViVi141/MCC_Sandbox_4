#define MCC_EVAC_SELECTED 42
disableSerialization;
private ["_type","_evac","_evacVehicles"];
_type = _this select 0;
if ((lbCurSel MCC_EVAC_SELECTED) == -1) exitWith {};
_evacVehicles = missionNamespace getvariable [format ["MCC_evacVehicles_%1",playerside],[]];
_evac = _evacVehicles select (lbCurSel MCC_EVAC_SELECTED);

switch (_type) do
{
	case 0:
	{
		if (!alive driver _evac) exitWith {};
		hint (localize "STR_MCC_HINT_PILOT_DELETED");
	};
	case 1:
	{
		if (alive driver _evac) exitWith {};
		hint (localize "STR_MCC_HINT_PILOT_RESPAWNED");
	};
	case 2:
	{
		if (!alive _evac) exitWith {};
		hint (localize "STR_MCC_HINT_PILOT_CHOPPER_DELETED");
	};

};

if (MCC_capture_state) then
{
	MCC_capture_var = MCC_capture_var + FORMAT ['
if (!(isNull _evac)) then {
	[%1,[netid _evac,_evac]] remoteExec ["MCC_fnc_evacDelete", 0, false];
};
						'
						,_type
						,_evac
						];
}
else
{
if (!(isNull _evac)) then {
[_type,[netid _evac,_evac]] remoteExec ["MCC_fnc_evacDelete", 0, false];
};
};

;

