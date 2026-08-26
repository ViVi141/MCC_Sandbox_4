/*============================================MCC_fnc_MWFindMissionCenter=========================================================================================================
	Find the mission Wizard's center
	Example: [_pos,_minRadius,_isCQB,_isBasedLocations] call MCC_fnc_MWFindMissionCenter;

	<IN>
		_pos				= position, from where to start looking (user zone / map center).
		_minRadius 			= integer, search radius around _pos (zone size, not a minimum distance).
		_isCQB 				= Boolean, true - for CQB area false if it doesn't matters.
		_isBasedLocations 	= Boolean, true if the map support locations

	<OUT>
 		Return - [pos, locationName]
//===========================================================================================================================================================================*/
private ["_pos","_minRadius","_isCQB","_centerFound","_buildingsArray","_newPos","_isBasedLocations","_locations","_location","_time","_radius","_inZone","_loc","_locPos","_dist","_buildingIndex"];

_pos 				= _this select 0;
_minRadius 			= _this select 1;
_isCQB 				= _this select 2;
_isBasedLocations 	= _this select 3;

_centerFound = false;
_newPos = [];
_location = [0, ""];
_locations = [];

if (isNil "_pos" || {typeName _pos != typeName []}) then {
	_pos = [0, 0, 0];
};
if (count _pos < 3) then {
	_pos set [2, 0];
};
if (isNil "_minRadius" || {_minRadius <= 0}) then {
	_minRadius = 200;
};

// Named locations MUST be inside the search radius. Never pick a map-wide random location —
// that was spawning missions kilometres away from the user zone.
if (_isBasedLocations) then {
	if (_isCQB) then {
		if (!isNil "MCC_MWcityLocations") then {
			_locations = _locations + MCC_MWcityLocations;
		};
		if (!isNil "MCC_MWmilitaryLocations") then {
			_locations = _locations + MCC_MWmilitaryLocations;
		};
	} else {
		if (!isNil "MCC_MWhillsLocations") then {
			_locations = _locations + MCC_MWhillsLocations;
		};
		if (!isNil "MCC_MWnatureLocations") then {
			_locations = _locations + MCC_MWnatureLocations;
		};
		if (!isNil "MCC_MWmarineLocations") then {
			_locations = _locations + MCC_MWmarineLocations;
		};
	};

	_inZone = [];
	{
		_loc = _x;
		if (!isNil "_loc" && {typeName _loc == typeName []} && {count _loc >= 1}) then {
			_locPos = getPos (_loc select 0);
			if (!isNil "_locPos" && {count _locPos >= 2}) then {
				_dist = _pos distance2D _locPos;
				if (_dist < _minRadius) then {
					_inZone pushBack _loc;
				};
			};
		};
	} forEach _locations;

	if (count _inZone > 0) then {
		_location = _inZone call BIS_fnc_selectRandom;
		if (!isNil "_location" && {count _location >= 1}) then {
			_newPos = getPos (_location select 0);
			if (!isNil "_newPos" && {count _newPos >= 2} && {!surfaceIsWater _newPos}) then {
				_newPos set [2, 0];
				_centerFound = true;
			};
		};
	};
};

// Random land inside the search circle (user zone, or 2 km around map center in whole-map mode)
if (!_centerFound) then {
	_time = time + 30;
	_location = [0, ""];

	while {!_centerFound && time < _time} do {
		_newPos = [];
		_radius = _minRadius;

		// BIS_fnc_randomPos whitelist is an ARRAY OF AREAS: [[[center, radius]], blacklist]
		while {count _newPos < 3 && time < _time} do {
			_newPos = [[[_pos, _radius]], ["water"]] call BIS_fnc_randomPos;
			if (isNil "_newPos") then {
				_newPos = [];
			};
			if (count _newPos == 2) then {
				if ((_newPos select 0) == 0 && {(_newPos select 1) == 0}) then {
					_newPos = [];
				};
			};
			_radius = _radius + 50;
		};

		if (count _newPos >= 2) then {
			_newPos set [2, 0];

			if (_pos distance2D _newPos > (_minRadius * 1.5)) then {
				_newPos = [];
			};
		};

		if (count _newPos >= 3) then {
			if (_isCQB) then {
				_buildingsArray = nearestObjects [_newPos, ["House", "Ruins", "Church", "FuelStation", "Strategic"], _minRadius];
				if ((count _buildingsArray > 0) && {!surfaceIsWater _newPos}) then {
					_buildingIndex = (count _buildingsArray - 1) min 5;
					if (_buildingIndex >= 0) then {
						_newPos = getPos (_buildingsArray select _buildingIndex);
						_newPos set [2, 0];
						if (_pos distance2D _newPos <= (_minRadius * 1.5)) then {
							_centerFound = true;
						};
					};
				};
			} else {
				if (!surfaceIsWater _newPos) then {
					_centerFound = true;
				};
			};
		};
	};
};

if (!_centerFound) then {
	diag_log format ["MCC: MWFindMissionCenter - no land in radius %1 around %2, using zone center", _minRadius, _pos];
	_newPos = _pos;
	_newPos set [2, 0];
	if (!surfaceIsWater _newPos) then {
		_centerFound = true;
	};
};

if (isNil "_newPos" || {count _newPos < 3}) then {
	_newPos = [0, 0, 0];
};
if (isNil "_location" || {typeName _location != typeName []} || {count _location < 2}) then {
	_location = [0, ""];
};

[_newPos, (_location select 1)]
