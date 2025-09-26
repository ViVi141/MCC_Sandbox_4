/*
	File: fn_MWCreateTaskCompat.sqf
	Author: MCC Sandbox Team
	Description: Compatibility layer for existing MCC modules
	
	This function ensures backward compatibility while providing
	enhanced error handling and performance optimizations.
*/

// Enhanced MCC_fnc_MWCreateTask with backward compatibility
MCC_fnc_MWCreateTask = {
	params [
		["_obj", objNull, [objNull]],
		["_pos", [], [[]]],
		["_task", "", [""]],
		["_preciseMarker", false, [false]],
		["_side", sideLogic, [sideLogic]],
		["_maxObjectivesDistance", 400, [0]],
		["_sidePlayer", sideLogic, [sideLogic]]
	];
	
	// Log function call for debugging
	diag_log format ["MCC_fnc_MWCreateTask called: %1, %2, %3", _obj, _pos, _task];
	
	// Validate input parameters
	if (_task == "") then {
		diag_log "MCC_fnc_MWCreateTask: Error - Task type is empty";
		return [];
	};
	
	if (count _pos < 2) then {
		diag_log "MCC_fnc_MWCreateTask: Error - Invalid position";
		return [];
	};
	
	// Check if task manager is available
	if (isNil "MCC_taskCreationQueue") then {
		diag_log "MCC_fnc_MWCreateTask: Task manager not initialized, using direct creation";
		return [_obj, _pos, _task, _preciseMarker, _side, _maxObjectivesDistance] call MCC_fnc_MWCreateTaskDirect;
	};
	
	// Use task manager for enhanced creation
	_taskData = [_obj, _pos, _task, _preciseMarker, _side, _maxObjectivesDistance];
	[_taskData, 1] call MCC_fnc_queueTask; // Priority 1 for normal tasks
	
	// Return placeholder result for immediate compatibility
	[objNull, _pos, _task, _preciseMarker, _side, _maxObjectivesDistance]
};

// Enhanced direct creation function
MCC_fnc_MWCreateTaskDirect = {
	params [
		["_obj", objNull, [objNull]],
		["_pos", [], [[]]],
		["_task", "", [""]],
		["_preciseMarker", false, [false]],
		["_side", sideLogic, [sideLogic]],
		["_maxObjectivesDistance", 400, [0]]
	];
	
	// Validate input parameters
	if (_task == "") then {
		diag_log "MCC_fnc_MWCreateTaskDirect: Error - Task type is empty";
		return [];
	};
	
	if (count _pos < 2) then {
		diag_log "MCC_fnc_MWCreateTaskDirect: Error - Invalid position";
		return [];
	};
	
	// Direct creation with enhanced error handling
	_attempts = 0;
	_maxAttempts = 3;
	_result = [];
	
	while {_attempts < _maxAttempts && count _result == 0} do {
		_attempts = _attempts + 1;
		
		try {
			// Call the original function with enhanced error handling
			_result = [_obj, _pos, _task, _preciseMarker, _side, _maxObjectivesDistance] call MCC_fnc_MWCreateTaskOriginal;
			
			if (count _result == 0) then {
				throw "Task creation returned empty result";
			};
			
			// Validate created task
			if (MCC_taskValidationEnabled) then {
				[_result] call MCC_fnc_validateTask;
			};
			
		} catch {
			diag_log format ["MCC_fnc_MWCreateTaskDirect: Creation failed (attempt %1): %2", _attempts, _exception];
			
			if (_attempts < _maxAttempts) then {
				sleep 0.5; // Wait before retry
			};
		};
	};
	
	if (count _result == 0) then {
		diag_log "MCC_fnc_MWCreateTaskDirect: Creation failed after all attempts";
	};
	
	_result
};

// Store original function (this will be set after the original function is loaded)
if (isNil "MCC_fnc_MWCreateTaskOriginal") then {
	MCC_fnc_MWCreateTaskOriginal = {
		// Fallback to direct call if original not available
		[_this select 0, _this select 1, _this select 2, _this select 3, _this select 4, _this select 5] call MCC_fnc_MWCreateTask;
	};
};
