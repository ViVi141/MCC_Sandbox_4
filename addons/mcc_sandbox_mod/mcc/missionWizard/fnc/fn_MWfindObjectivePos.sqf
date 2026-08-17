/*================================================MCC_fnc_MWfindObjectivePos==============================================================================================
// Find the mission Wizard's center - IMPROVED VERSION
// Example:[_missionCenter,_isCQB,_minObjectivesDistance, _objFirstTime] call MCC_fnc_MWfindObjectivePos;
// _missionCenter 			= position, from where to start looking.
//_isCQB 				= Boolean, true - for CQB areay false if it doesn't matters.
//_minObjectivesDistance 	= integer, minimum distance between objectives
// Return - pos
//================================================================================================================================================================*/

private ["_missionCenter","_isCQB","_minObjectivesDistance","_buildingsArray","_farEnough","_range","_flatPos","_availablePos","_time","_radius","_markerName","_objectivesMarkers","_ambient","_maxAttempts","_attempts"];

_missionCenter 			= _this select 0;
_isCQB 					= _this select 1;
_minObjectivesDistance 	= _this select 2;
_maxObjectivesDistance 	= param [3,500,[500]];

_farEnough = false;
_range = 100;
_availablePos = [];
_maxAttempts = 50; // 增加最大尝试次数
_attempts = 0;

//Lets find a pice of land
_time = time + 30; // 增加超时时间到30秒

_objectivesMarkers = missionNamespace getVariable ["MCC_MWObjectiveMarkers",[]];

_ambient = if (_isCQB) then {"houses + meadow "} else {"meadow + houses + hills "};

//if it is the first time then find objective close to the center
while {(count _availablePos) == 0 && (_range < (_maxObjectivesDistance*3)) && (_attempts < _maxAttempts)} do {

	_availablePos = selectBestPlaces [_missionCenter, _range, _ambient, 10, 5];

	if (count _availablePos > 0) then {
		_availablePos = (_availablePos select 0) select 0;
		_availablePos set [2,0];

		//are we far enough from all other objectives
		_farEnough = {(getMarkerPos _x) distance2d _availablePos <= (_minObjectivesDistance*0.5)} count _objectivesMarkers == 0;

		//If we are not far enough and also too far from mission center
		if (!_farEnough) then {_availablePos = []};
	};

	_range = _range + 100;
	_attempts = _attempts + 1;
	sleep 0.1;
};

// 如果仍然找不到位置，使用备用方案
if ((count _availablePos) == 0) then {
	// 使用更宽松的条件重新搜索
	_range = 200;
	while {(count _availablePos) == 0 && (_range < 2000)} do {
		_availablePos = selectBestPlaces [_missionCenter, _range, "meadow", 5, 3];
		if (count _availablePos > 0) then {
			_availablePos = (_availablePos select 0) select 0;
			_availablePos set [2,0];
		};
		_range = _range + 200;
		sleep 0.1;
	};
};

if (missionNamespace getVariable ["MCC_debug",false]) then {
	systemChat format ["found position: %1, have time: %2, farenough: %3, attempts: %4",(count _availablePos) > 0, time < _time,_farEnough, _attempts];
	diag_log format ["MCC MW: Position search - found: %1, time remaining: %2, far enough: %3, attempts: %4",(count _availablePos) > 0, time < _time,_farEnough, _attempts];
};

if (count _availablePos == 0) exitWith {
	diag_log "MCC: Mission Wizard Error: No mission objective's postion found, make a bigger zone";
	// 使用备用位置
	_availablePos = [_missionCenter, 0, 1000, 10, 0, 0.3, 0] call BIS_fnc_findSafePos;
	if ((count _availablePos) == 0) then {
		_availablePos = _missionCenter;
	};
	diag_log "MCC MW: Using fallback position for objective";
	_availablePos
};

if (_farEnough || (count _objectivesMarkers == 0)) then {
	if (_isCQB) then {
		_buildingsArray = [];
		_radius = 200;

		while {count _buildingsArray <= 1} do
		{
			_buildingsArray	= [_availablePos,_radius] call MCC_fnc_MWFindbuildingPos;
			_radius = _radius + 100;
			sleep 0.1;
		};

		_availablePos = getpos ((_buildingsArray call BIS_fnc_selectRandom) select 0);
	};

	_markerName = format ["Objective_%1",count _objectivesMarkers];

	createmarkerlocal [_markerName,_availablePos];
	_markerName setmarkertypelocal "mil_box";
	_markerName setMarkerTextLocal _markerName;
	_markerName setmarkerColorlocal "ColorRed";
	_markerName setMarkerSizeLocal [0.3, 0.3];
	_markerName setMarkerAlphaLocal 0;

	_objectivesMarkers pushBack _markerName;
	missionNamespace setVariable ["MCC_MWObjectiveMarkers",_objectivesMarkers];
	publicVariable "MCC_MWObjectiveMarkers";
};

_availablePos;