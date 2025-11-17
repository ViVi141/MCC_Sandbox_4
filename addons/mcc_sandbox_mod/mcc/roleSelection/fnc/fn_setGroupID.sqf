//==================================================================MCC_fnc_setGroupID======================================================================================
//Set group ID - SERVER ONLY
[[group,groupID], "MCC_fnc_setGroupID", false, false] remoteExec ["MCC_fnc_setGroupID", 2, false];
// Params: 
//==============================================================================================================================================================================	
private ["_group","_groupID"];
	
_group 		= _this select 0;
_groupID 	= _this select 1;

_group setGroupId _groupID;

