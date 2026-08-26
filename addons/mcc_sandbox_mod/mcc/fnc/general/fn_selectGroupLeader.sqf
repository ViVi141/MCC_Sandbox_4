//==================================================================MCC_fnc_selectGroupLeader======================================================================================
// Set a group leader by netIds. Must run where the group is local.
// Example: [netId _group, netId _unit] remoteExec ["MCC_fnc_selectGroupLeader", _group];
//==============================================================================================================================================================================
params [
	["_groupNetId", "", [""]],
	["_unitNetId", "", [""]]
];

if (_groupNetId == "") exitWith {};
if (_unitNetId == "") exitWith {};

private _group = groupFromNetID _groupNetId;
private _unit = objectFromNetId _unitNetId;
if (isNull _group) exitWith {};
if (isNull _unit) exitWith {};
if (!(_unit in units _group)) exitWith {};

if (!local _group) exitWith {
	[_groupNetId, _unitNetId] remoteExec ["MCC_fnc_selectGroupLeader", _group, false];
};

_group selectLeader _unit;
