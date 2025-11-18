#define MCC_BRIEFING_TEXT 3055
disableSerialization;
private ["_type","_dlg","_string"];
hint localize "STR_MCC_BRIEFING_DIARY_UPDATED";

_type = _this select 0;

_dlg = (uiNamespace getVariable "MCC_groupGen_Dialog");
_string = ctrlText (_dlg displayCtrl MCC_BRIEFING_TEXT);

if (!(isNull _string) && !(isNull _type)) then {
[_string, _type] remoteExec ["MCC_fnc_makeBriefing", 2];
};

