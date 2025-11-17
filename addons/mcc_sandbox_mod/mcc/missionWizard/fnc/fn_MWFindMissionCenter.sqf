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

// Validate input parameters
if (isNil "_this" || {count _this < 4}) exitWith {
	diag_log "MCC: MWFindMissionCenter - Invalid parameters";
	[[0,0,0], ""];
};

_pos 				= _this param [0, [0,0,0], [[]]];
_minRadius 			= _this param [1, 100, [0]];
_isCQB 				= _this param [2, false, [true]];
_isBasedLocations 	= _this param [3, false, [true]];

// Validate position
if (count _pos < 3 || {_pos isEqualTo [0,0,0]}) then {
	diag_log "MCC: MWFindMissionCenter - Invalid position parameter";
	_pos = [0,0,0];
};

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
		_location = _locations call BIS_fnc_selectRandom;
		// Validate _location before using
		if (!isNil "_location" && {typeName _location == typeName []} && {count _location >= 1}) then {
			private ["_locationObj"];
			_locationObj = _location param [0, objNull, [objNull]];
			if (!isNull _locationObj) then {
				_newPos = getpos _locationObj;
				if (count _newPos >= 3 && {!_newPos isEqualTo [0,0,0]}) then {
					_centerFound = true;
				} else {
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
			_newPos = [[[_pos,_radius]],["water"]] call BIS_fnc_randomPos;
			if (isNil "_newPos" || {typeName _newPos != typeName []}) then {
				_newPos = [0,0,0];
			};
			// Ensure position has 3 elements
			if (count _newPos < 3) then {
				_newPos set [2, 0];
			};
			_radius = _radius + 50;
		};
		
		// Ensure we have a valid position
		if (isNil "_newPos" || {typeName _newPos != typeName []}) then {
			_newPos = [0,0,0];
		};
		if (count _newPos < 3) then {_newPos set [2, 0]};



		if (_isCQB) then
			{
				_buildingsArray	= nearestObjects  [_newPos,["House","Ruins","Church","FuelStation","Strategic"],_minRadius];	//Let's find the buildings in the area
				if ((count _buildingsArray > 0) && (!surfaceIsWater _newPos)) then
					{
						_buildingIndex = min [5, count _buildingsArray - 1];
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

// Initialize _location if not set
if (isnil "_location" || {typeName _location != typeName []} || {count _location < 2}) then {
	_location = [0,""];
};

// Ensure _location has at least 2 elements
if (count _location < 2) then {
	_location set [1, ""];
};

// Validate _newPos
if (isnil "_newPos" || {typeName _newPos != typeName []}) then {
	_newPos = [0,0,0];
};

// Ensure _newPos is a valid position array with 3 elements
if (count _newPos < 3) then {
	_newPos set [2, 0];
};

// If we couldn't find a valid center, return [0,0,0] as position (caller should check for this)
if (!_centerFound && _newPos isEqualTo [0,0,0]) then {
	diag_log "MCC: MWFindMissionCenter - Failed to find valid mission center position";
};

// Safely get location name
private ["_locationName"];
_locationName = if (count _location >= 2) then {
	_location param [1, "", [""]]
} else {
	""
};

// Always return array format: [position, locationName]
[_newPos, _locationName];