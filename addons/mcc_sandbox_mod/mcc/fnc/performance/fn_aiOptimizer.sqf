/*
	File: fn_aiOptimizer.sqf
	Author: MCC Sandbox Team
	Description: AI performance optimization system
	
	This system optimizes AI performance by managing AI behavior,
	reducing unnecessary calculations, and implementing smart
	AI management techniques.
*/

// AI optimization settings
MCC_aiOptimizationSettings = [
	["maxAIUnits", 50],           // Maximum AI units
	["updateInterval", 5],        // AI update interval in seconds
	["disableDistance", 1000],    // Distance to disable AI
	["enableDistance", 500],      // Distance to enable AI
	["skillReduction", 0.1],      // Skill reduction for distant units
	["behaviorUpdate", 10]        // Behavior update interval
];

// AI management variables
MCC_aiUnits = [];
MCC_aiUpdateTime = 0;
MCC_aiEnabled = true;

// Initialize AI optimizer
MCC_fnc_initAIOptimizer = {
	if (isServer) then {
		[] spawn MCC_fnc_aiManagementLoop;
		diag_log localize "STR_MCC_AI_OPTIMIZER_INITIALIZED";
	};
};

// Main AI management loop
MCC_fnc_aiManagementLoop = {
	while {MCC_aiEnabled} do {
		[] call MCC_fnc_updateAIUnits;
		[] call MCC_fnc_optimizeAIPerformance;
		[] call MCC_fnc_manageAIDistance;
		
		_updateInterval = [MCC_aiOptimizationSettings, "updateInterval"] call MCC_fnc_getSetting;
		sleep _updateInterval;
	};
};

// Update AI units list
MCC_fnc_updateAIUnits = {
	MCC_aiUnits = allUnits select {!isPlayer _x && alive _x};
	
	// Limit AI units (skip in unlimited mode)
	_unlimitedMode = false;
	if (!isNil "MCC_performanceConfig") then {
		_unlimitedMode = [MCC_performanceConfig, "unlimitedMode", false] call MCC_fnc_getPerformanceConfig;
	};
	if (!_unlimitedMode) then {
		_maxAI = [MCC_aiOptimizationSettings, "maxAIUnits"] call MCC_fnc_getSetting;
		if (count MCC_aiUnits > _maxAI) then {
			_excessUnits = MCC_aiUnits select [_maxAI, count MCC_aiUnits - _maxAI];
			{
				if (alive _x) then {
					deleteVehicle _x;
				};
			} forEach _excessUnits;
			MCC_aiUnits = MCC_aiUnits select [0, _maxAI];
		};
	};
};

// Optimize AI performance
MCC_fnc_optimizeAIPerformance = {
	{
		_unit = _x;
		if (alive _unit) then {
			// Reduce AI skill for distant units
			_distance = _unit distance player;
			_disableDistance = [MCC_aiOptimizationSettings, "disableDistance"] call MCC_fnc_getSetting;
			
			if (_distance > _disableDistance) then {
				// Disable AI for very distant units
				_unit enableSimulation false;
				_unit setSkill 0.1;
			} else {
				// Enable AI for nearby units
				_unit enableSimulation true;
				
				// Adjust skill based on distance
				_skillReduction = [MCC_aiOptimizationSettings, "skillReduction"] call MCC_fnc_getSetting;
				_baseSkill = 0.5;
				_distanceFactor = 1 - (_distance / _disableDistance);
				_finalSkill = _baseSkill * _distanceFactor;
				_unit setSkill _finalSkill;
			};
		};
	} forEach MCC_aiUnits;
};

// Manage AI distance
MCC_fnc_manageAIDistance = {
	_playerPos = getPos player;
	
	{
		_unit = _x;
		if (alive _unit) then {
			_distance = _unit distance _playerPos;
			_disableDistance = [MCC_aiOptimizationSettings, "disableDistance"] call MCC_fnc_getSetting;
			_enableDistance = [MCC_aiOptimizationSettings, "enableDistance"] call MCC_fnc_getSetting;
			
			if (_distance > _disableDistance) then {
				// Disable AI
				_unit enableSimulation false;
				_unit setVariable ["MCC_aiDisabled", true];
			} else {
				if (_distance < _enableDistance && (_unit getVariable ["MCC_aiDisabled", false])) then {
					// Re-enable AI
					_unit enableSimulation true;
					_unit setVariable ["MCC_aiDisabled", false];
				};
			};
		};
	} forEach MCC_aiUnits;
};

// Batch AI operations
MCC_fnc_batchAIOperations = {
	params ["_units", "_operation", "_params"];
	
	{
		_unit = _x;
		if (alive _unit) then {
			switch (_operation) do {
				case "setSkill": {
					_unit setSkill (_params select 0);
				};
				case "setCombatMode": {
					_unit setCombatMode (_params select 0);
				};
				case "setBehaviour": {
					_unit setBehaviour (_params select 0);
				};
				case "setSpeedMode": {
					_unit setSpeedMode (_params select 0);
				};
				case "setFormation": {
					_unit setFormation (_params select 0);
				};
			};
		};
	} forEach _units;
};

// Optimize AI waypoints
MCC_fnc_optimizeAIWaypoints = {
	params ["_group"];
	
	_waypoints = waypoints _group;
	_maxWaypoints = 5; // Limit waypoints for performance
	
	if (count _waypoints > _maxWaypoints) then {
		// Remove excess waypoints
		for "_i" from _maxWaypoints to (count _waypoints - 1) do {
			deleteWaypoint [_group, _maxWaypoints];
		};
	};
	
	// Optimize waypoint positions
	{
		_wp = _x;
		_wpPos = waypointPosition _wp;
		
		// Check if waypoint is too close to previous
		if (_forEachIndex > 0) then {
			_prevWp = _waypoints select (_forEachIndex - 1);
			_prevPos = waypointPosition _prevWp;
			_distance = _wpPos distance _prevPos;
			
			if (_distance < 10) then {
				deleteWaypoint [_group, _forEachIndex];
			};
		};
	} forEach _waypoints;
};

// Smart AI spawning
MCC_fnc_smartAISpawn = {
	params ["_unitClass", "_position", "_group", "_skill"];
	
	// Check if we can spawn more AI (skip check in unlimited mode)
	_unlimitedMode = false;
	if (!isNil "MCC_performanceConfig") then {
		_unlimitedMode = [MCC_performanceConfig, "unlimitedMode", false] call MCC_fnc_getPerformanceConfig;
	};
	if (!_unlimitedMode) then {
		_maxAI = [MCC_aiOptimizationSettings, "maxAIUnits"] call MCC_fnc_getSetting;
		if (count MCC_aiUnits >= _maxAI) then {
			diag_log localize "STR_MCC_AI_OPTIMIZER_MAX_UNITS";
			objNull
		} else {
			// Create unit with optimized settings
			_unit = _group createUnit [_unitClass, _position, [], 0, "NONE"];
			_unit setSkill _skill;
			
			// Add to AI units list
			MCC_aiUnits pushBack _unit;
			
			_unit
		};
	} else {
		// Create unit with optimized settings (unlimited mode)
		_unit = _group createUnit [_unitClass, _position, [], 0, "NONE"];
		_unit setSkill _skill;
		
		// Add to AI units list
		MCC_aiUnits pushBack _unit;
		
		_unit
	};
};

// Get setting value
MCC_fnc_getSetting = {
	params ["_settings", "_settingName"];
	
	_value = 0;
	{
		if ((_x select 0) == _settingName) then {
			_value = _x select 1;
		};
	} forEach _settings;
	
	_value
};

// Update setting
MCC_fnc_updateSetting = {
	params ["_settingName", "_newValue"];
	
	{
		if ((_x select 0) == _settingName) then {
			_x set [1, _newValue];
		};
	} forEach MCC_aiOptimizationSettings;
};

// Get AI statistics
MCC_fnc_getAIStats = {
	_stats = createHashMap;
	_stats set ["totalAI", count MCC_aiUnits];
	_stats set ["activeAI", count (MCC_aiUnits select {alive _x && simulationEnabled _x})];
	_stats set ["disabledAI", count (MCC_aiUnits select {alive _x && !simulationEnabled _x})];
	_stats set ["averageSkill", 0];
	
	_totalSkill = 0;
	_activeUnits = MCC_aiUnits select {alive _x && simulationEnabled _x};
	{
		_totalSkill = _totalSkill + (skill _x);
	} forEach _activeUnits;
	
	if (count _activeUnits > 0) then {
		_stats set ["averageSkill", _totalSkill / count _activeUnits];
	};
	
	_stats
};

// Initialize AI optimizer
if (isServer) then {
	[] call MCC_fnc_initAIOptimizer;
};
