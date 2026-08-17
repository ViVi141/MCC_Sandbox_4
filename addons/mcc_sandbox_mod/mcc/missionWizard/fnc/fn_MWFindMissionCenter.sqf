/*============================================MCC_fnc_MWFindMissionCenter=========================================================================================================
	Find the mission Wizard's center
	Example: [_pos,_minRadius,_maxRadius,_isCQB] call MCC_fnc_MWFindMissionCenter;

	<IN>
		_pos				= position, from where to start looking.
		_minRadius 			= integer, minimum distance from _pos
		_maxRadius			= integer, Maximum distance from _pos
		_isCQB 			= Boolean, true - for CQB areay false if it doesn't matters.
		_isBasedLocations 	= Boolean, true if the map support locations

	<OUT>
 		Return - pos
//===========================================================================================================================================================================*/
private ["_pos","_minRadius","_centerFound","_buildingsArray","_newPos","_name","_type","_isBasedLocations","_locations","_location","_time","_radius"];

_pos 				= _this select 0;
_minRadius 			= _this select 1;
_isCQB 				= _this select 2;
_isBasedLocations 	= _this select 3;

_centerFound = false;
_newPos = [0,0,0];

if (_isBasedLocations) then {
	if (_isCQB) then
	{
		_locations = [];
		if (!isNil "MCC_MWcityLocations") then {_locations = _locations + MCC_MWcityLocations;};
		if (!isNil "MCC_MWmilitaryLocations") then {_locations = _locations + MCC_MWmilitaryLocations;};
	}
	else
	{
		_locations = [];
		if (!isNil "MCC_MWhillsLocations") then {_locations = _locations + MCC_MWhillsLocations;};
		if (!isNil "MCC_MWnatureLocations") then {_locations = _locations + MCC_MWnatureLocations;};
		if (!isNil "MCC_MWmarineLocations") then {_locations = _locations + MCC_MWmarineLocations;};
	};

	if (count _locations > 0) then {
		//Prefer locations near the search center (user zone) so the mission spawns where requested
		_locations = [_locations, {_pos distance2D (getpos (_x select 0)) < _minRadius}] call BIS_fnc_conditionalSelect;
		if (count _locations == 0) then {
			_locations = [_locations, [], {_pos distance2D (getpos (_x select 0))}, "ASCEND"] call BIS_fnc_sortBy;
		};
		if (count _locations > 0) then {
			_location = _locations call BIS_fnc_selectRandom;
			if (!isNil "_location" && {count _location >= 1}) then {
				_newPos = getpos (_location select 0);
				_newPos set [2, 0];
				_centerFound = true;
			} else {
				// Fall back to non-location based search
				_isBasedLocations = false;
			};
		} else {
			_isBasedLocations = false;
		};
	} else {
		// Fall back to non-location based search
		_isBasedLocations = false;
	};
} else {
	//Lets find a pice of land
	_time = time + 30;
	_newPos = [0,0,0];

	while {!_centerFound && time < _time} do {

		//first is whitelist second is blacklist, third is condition
		_radius = _minRadius;
		while {count _newPos <3 && time < _time} do
		{
			_newPos = [[_pos,_radius],["water"]] call BIS_fnc_randomPos;
			if (isNil "_newPos") then {_newPos = [0,0,0];};
			_radius = _radius + 50;
		};
		
		// Ensure we have a valid position
		if (count _newPos < 3) then {_newPos set [2, 0]};



		if (_isCQB) then
			{
				_buildingsArray	= nearestObjects  [_newPos,["House","Ruins","Church","FuelStation","Strategic"],_minRadius];	//Let's find the buildings in the area
				if ((count _buildingsArray > 0) && (!surfaceIsWater _newPos)) then
					{
						_buildingIndex = (count _buildingsArray - 1) min 5;
						if (_buildingIndex >= 0) then {
							_newPos = getpos (_buildingsArray select _buildingIndex);
							_centerFound = true;
						};
					};
			}
				else
			{
				if (!surfaceIsWater _newPos) then {_centerFound = true};
			};
	};
};

if (isnil "_location") then {_location = [0,""]};
if (isnil "_newPos") then {_newPos = [0,0,0]};

// Ensure _location has at least 2 elements
if (count _location < 2) then {_location set [1, ""];};

[_newPos,(_location select 1)];