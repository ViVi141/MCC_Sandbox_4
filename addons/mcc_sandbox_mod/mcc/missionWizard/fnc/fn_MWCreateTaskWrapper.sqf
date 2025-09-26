/*
	File: fn_MWCreateTaskWrapper.sqf
	Author: MCC Sandbox Team
	Description: Wrapper function for task creation with enhanced error handling
	
	This function provides:
	- Enhanced error handling
	- Retry mechanism
	- Performance monitoring
	- Task validation
*/

MCC_fnc_MWCreateTaskWrapper = {
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
		diag_log "MCC Task Wrapper: Error - Task type is empty";
		return [];
	};
	
	if (count _pos < 2) then {
		diag_log "MCC Task Wrapper: Error - Invalid position";
		return [];
	};
	
	// Check if task manager is available
	if (isNil "MCC_taskCreationQueue") then {
		diag_log "MCC Task Wrapper: Task manager not initialized, using direct creation";
		return [_obj, _pos, _task, _preciseMarker, _side, _maxObjectivesDistance] call MCC_fnc_MWCreateTask;
	};
	
	// Use task manager for queued creation
	_taskData = [_obj, _pos, _task, _preciseMarker, _side, _maxObjectivesDistance];
	[_taskData, 1] call MCC_fnc_queueTask; // Priority 1 for normal tasks
	
	// Return placeholder result
	[objNull, _pos, _task, _preciseMarker, _side, _maxObjectivesDistance]
};

// High priority task creation (for critical tasks)
MCC_fnc_MWCreateTaskHighPriority = {
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
		diag_log "MCC Task Wrapper: Error - Task type is empty";
		return [];
	};
	
	if (count _pos < 2) then {
		diag_log "MCC Task Wrapper: Error - Invalid position";
		return [];
	};
	
	// Check if task manager is available
	if (isNil "MCC_taskCreationQueue") then {
		diag_log "MCC Task Wrapper: Task manager not initialized, using direct creation";
		return [_obj, _pos, _task, _preciseMarker, _side, _maxObjectivesDistance] call MCC_fnc_MWCreateTask;
	};
	
	// Use task manager for high priority creation
	_taskData = [_obj, _pos, _task, _preciseMarker, _side, _maxObjectivesDistance];
	[_taskData, 10] call MCC_fnc_queueTask; // Priority 10 for high priority tasks
	
	// Return placeholder result
	[objNull, _pos, _task, _preciseMarker, _side, _maxObjectivesDistance]
};

// Direct task creation (bypasses queue)
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
		diag_log "MCC Task Wrapper: Error - Task type is empty";
		return [];
	};
	
	if (count _pos < 2) then {
		diag_log "MCC Task Wrapper: Error - Invalid position";
		return [];
	};
	
	// Direct creation with enhanced error handling
	_attempts = 0;
	_maxAttempts = 3;
	_result = [];
	
	while {_attempts < _maxAttempts && count _result == 0} do {
		_attempts = _attempts + 1;
		
		try {
			_result = [_obj, _pos, _task, _preciseMarker, _side, _maxObjectivesDistance] call MCC_fnc_MWCreateTask;
			
			if (count _result == 0) then {
				throw "Task creation returned empty result";
			};
		} catch {
			diag_log format ["MCC Task Wrapper: Direct creation failed (attempt %1): %2", _attempts, _exception];
			
			if (_attempts < _maxAttempts) then {
				sleep 0.5; // Wait before retry
			};
		};
	};
	
	if (count _result == 0) then {
		diag_log "MCC Task Wrapper: Direct creation failed after all attempts";
	};
	
	_result
};
