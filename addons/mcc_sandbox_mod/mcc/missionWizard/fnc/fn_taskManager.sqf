/*
	File: fn_taskManager.sqf
	Author: MCC Sandbox Team
	Description: Advanced task management system for MCC Mission Wizard
	
	This system provides:
	- Task creation queue
	- Error handling and retry
	- Performance monitoring
	- Memory management
*/

// Task management variables
MCC_taskCreationQueue = [];
MCC_taskCreationInProgress = false;
MCC_taskCreationStats = createHashMap;
MCC_taskValidationEnabled = true;
MCC_maxRetryAttempts = 3;
MCC_taskCleanupInterval = 300; // 5 minutes

// Initialize task manager
MCC_fnc_initTaskManager = {
	if (isServer) then {
		// Initialize statistics
		MCC_taskCreationStats set ["successful", 0];
		MCC_taskCreationStats set ["failed", 0];
		MCC_taskCreationStats set ["retries", 0];
		MCC_taskCreationStats set ["totalCreated", 0];
		
		// Start task processing loop
		[] spawn MCC_fnc_processTaskQueue;
		
		// Start cleanup loop
		[] spawn MCC_fnc_taskCleanupLoop;
		
		diag_log "MCC Task Manager initialized";
	};
};

// Add task to creation queue
MCC_fnc_queueTask = {
	params [
		["_taskData", [], [[]]],
		["_priority", 0, [0]]
	];
	
	// Add priority and timestamp
	_taskData pushBack _priority;
	_taskData pushBack time;
	
	// Insert based on priority (higher priority first)
	_inserted = false;
	{
		if (_priority > (_x select (count _x - 2))) then {
			MCC_taskCreationQueue insert [_forEachIndex, _taskData];
			_inserted = true;
			break;
		};
	} forEach MCC_taskCreationQueue;
	
	if (!_inserted) then {
		MCC_taskCreationQueue pushBack _taskData;
	};
	
	diag_log format ["MCC Task Manager: Task queued, queue size: %1", count MCC_taskCreationQueue];
};

// Process task creation queue
MCC_fnc_processTaskQueue = {
	while {true} do {
		if (count MCC_taskCreationQueue > 0 && !MCC_taskCreationInProgress) then {
			MCC_taskCreationInProgress = true;
			
			_taskData = MCC_taskCreationQueue deleteAt 0;
			[_taskData] call MCC_fnc_createTaskAsync;
			
			MCC_taskCreationInProgress = false;
		};
		
		sleep 0.1; // Prevent blocking
	};
};

// Create task asynchronously
MCC_fnc_createTaskAsync = {
	params ["_taskData"];
	
	// Extract task parameters
	_obj = _taskData select 0;
	_pos = _taskData select 1;
	_task = _taskData select 2;
	_preciseMarker = _taskData select 3;
	_side = _taskData select 4;
	_maxObjectivesDistance = _taskData select 5;
	_priority = _taskData select (count _taskData - 2);
	_timestamp = _taskData select (count _taskData - 1);
	
	// Check if task is too old (older than 30 seconds)
	if (time - _timestamp > 30) then {
		diag_log "MCC Task Manager: Task expired, skipping";
		MCC_taskCreationStats set ["failed", (MCC_taskCreationStats get "failed") + 1];
		return;
	};
	
	// Attempt to create task
	_attempts = 0;
	_success = false;
	
	while {_attempts < MCC_maxRetryAttempts && !_success} do {
		_attempts = _attempts + 1;
		
		try {
			_result = [_obj, _pos, _task, _preciseMarker, _side, _maxObjectivesDistance] call MCC_fnc_MWCreateTask;
			
			if (!isNil "_result" && {count _result > 0}) then {
				_success = true;
				MCC_taskCreationStats set ["successful", (MCC_taskCreationStats get "successful") + 1];
				MCC_taskCreationStats set ["totalCreated", (MCC_taskCreationStats get "totalCreated") + 1];
				
				// Validate created task
				if (MCC_taskValidationEnabled) then {
					[_result] call MCC_fnc_validateTask;
				};
				
				diag_log format ["MCC Task Manager: Task created successfully (attempt %1)", _attempts];
			} else {
				throw "Task creation returned empty result";
			};
		} catch {
			diag_log format ["MCC Task Manager: Task creation failed (attempt %1): %2", _attempts, _exception];
			
			if (_attempts < MCC_maxRetryAttempts) then {
				sleep 0.5; // Wait before retry
				MCC_taskCreationStats set ["retries", (MCC_taskCreationStats get "retries") + 1];
			};
		};
	};
	
	if (!_success) then {
		MCC_taskCreationStats set ["failed", (MCC_taskCreationStats get "failed") + 1];
		diag_log format ["MCC Task Manager: Task creation failed after %1 attempts", _attempts];
	};
};

// Validate task
MCC_fnc_validateTask = {
	params ["_taskData"];
	
	if (isNil "_taskData" || {count _taskData == 0}) then {
		diag_log "MCC Task Manager: Invalid task data";
		return false;
	};
	
	_task = _taskData select 8; // Task object is at index 8
	
	if (isNull _task) then {
		diag_log "MCC Task Manager: Task object is null";
		return false;
	};
	
	if (!alive _task) then {
		diag_log "MCC Task Manager: Task object is not alive";
		return false;
	};
	
	// Check required variables
	_requiredVars = ["RscAttributeOwners", "RscAttributeTaskState", "taskType", "taskName"];
	{
		if (isNil {_task getVariable _x}) then {
			diag_log format ["MCC Task Manager: Task missing required variable: %1", _x];
			return false;
		};
	} forEach _requiredVars;
	
	diag_log "MCC Task Manager: Task validation passed";
	true
};

// Get task statistics
MCC_fnc_getTaskStats = {
	MCC_taskCreationStats set ["queueSize", count MCC_taskCreationQueue];
	MCC_taskCreationStats set ["inProgress", MCC_taskCreationInProgress];
	MCC_taskCreationStats
};

// Clean up old or invalid tasks
MCC_fnc_taskCleanupLoop = {
	while {true} do {
		sleep MCC_taskCleanupInterval;
		
		[] call MCC_fnc_cleanupInvalidTasks;
		[] call MCC_fnc_cleanupOldTasks;
		
		diag_log "MCC Task Manager: Cleanup cycle completed";
	};
};

// Clean up invalid tasks
MCC_fnc_cleanupInvalidTasks = {
	_invalidTasks = [];
	
	{
		_task = _x;
		if (!isNull _task && alive _task) then {
			// Check if task has required variables
			_hasRequiredVars = true;
			{
				if (isNil {_task getVariable _x}) then {
					_hasRequiredVars = false;
					break;
				};
			} forEach ["RscAttributeOwners", "RscAttributeTaskState", "taskType"];
			
			if (!_hasRequiredVars) then {
				_invalidTasks pushBack _task;
			};
		} else {
			_invalidTasks pushBack _task;
		};
	} forEach allMissionObjects "MCC_ModuleObjective_FCurator";
	
	// Delete invalid tasks
	{
		if (!isNull _x) then {
			deleteVehicle _x;
		};
	} forEach _invalidTasks;
	
	if (count _invalidTasks > 0) then {
		diag_log format ["MCC Task Manager: Cleaned up %1 invalid tasks", count _invalidTasks];
	};
};

// Clean up old tasks
MCC_fnc_cleanupOldTasks = {
	_maxTaskAge = 3600; // 1 hour
	_oldTasks = [];
	
	{
		_task = _x;
		if (!isNull _task && alive _task) then {
			_creationTime = _task getVariable ["MCC_creationTime", 0];
			if (_creationTime == 0) then {
				_task setVariable ["MCC_creationTime", time, true];
			} else {
				if (time - _creationTime > _maxTaskAge) then {
					_oldTasks pushBack _task;
				};
			};
		};
	} forEach allMissionObjects "MCC_ModuleObjective_FCurator";
	
	// Delete old tasks
	{
		if (!isNull _x) then {
			deleteVehicle _x;
		};
	} forEach _oldTasks;
	
	if (count _oldTasks > 0) then {
		diag_log format ["MCC Task Manager: Cleaned up %1 old tasks", count _oldTasks];
	};
};

// Emergency cleanup
MCC_fnc_emergencyCleanup = {
	diag_log "MCC Task Manager: Emergency cleanup initiated";
	
	// Clear queue
	MCC_taskCreationQueue = [];
	MCC_taskCreationInProgress = false;
	
	// Clean up all tasks
	{
		if (!isNull _x) then {
			deleteVehicle _x;
		};
	} forEach allMissionObjects "MCC_ModuleObjective_FCurator";
	
	diag_log "MCC Task Manager: Emergency cleanup completed";
};

// Initialize task manager
if (isServer) then {
	[] call MCC_fnc_initTaskManager;
};
