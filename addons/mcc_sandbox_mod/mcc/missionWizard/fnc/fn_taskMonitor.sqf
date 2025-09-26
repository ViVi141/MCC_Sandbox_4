/*
	File: fn_taskMonitor.sqf
	Author: MCC Sandbox Team
	Description: Task monitoring and management functions
*/

// Open task monitor dialog
MCC_fnc_openTaskMonitor = {
	if (isNil "MCC_taskCreationQueue") then {
		hint "Task manager not initialized";
		return;
	};
	
	createDialog "MCC_taskMonitorDialog";
	[] call MCC_fnc_refreshTaskStats;
};

// Refresh task statistics
MCC_fnc_refreshTaskStats = {
	if (isNil "MCC_taskCreationStats") then {
		hint "Task statistics not available";
		return;
	};
	
	_stats = [] call MCC_fnc_getTaskStats;
	_listbox = findDisplay 9001 displayCtrl 1501;
	
	if (isNull _listbox) then {
		hint "Task monitor dialog not found";
		return;
	};
	
	lbClear _listbox;
	
	// Add statistics
	lbAdd [1501, format ["Queue Size: %1", _stats get "queueSize"]];
	lbAdd [1501, format ["In Progress: %1", _stats get "inProgress"]];
	lbAdd [1501, format ["Successful: %1", _stats get "successful"]];
	lbAdd [1501, format ["Failed: %1", _stats get "failed"]];
	lbAdd [1501, format ["Retries: %1", _stats get "retries"]];
	lbAdd [1501, format ["Total Created: %1", _stats get "totalCreated"]];
	
	// Add current tasks
	lbAdd [1501, ""];
	lbAdd [1501, "Current Tasks:"];
	
	_taskCount = 0;
	{
		_task = _x;
		if (!isNull _task && alive _task) then {
			_taskCount = _taskCount + 1;
			_taskName = _task getVariable ["taskName", "Unknown"];
			_taskType = _task getVariable ["taskType", "Unknown"];
			_taskState = _task getVariable ["RscAttributeTaskState", "Unknown"];
			
			lbAdd [1501, format ["Task %1: %2 (%3) - %4", _taskCount, _taskName, _taskType, _taskState]];
		};
	} forEach allMissionObjects "MCC_ModuleObjective_FCurator";
	
	lbAdd [1501, ""];
	lbAdd [1501, format ["Total Active Tasks: %1", _taskCount]];
};

// Add task monitor to console menu
MCC_fnc_addTaskMonitorMenu = {
	if (isNil "MCC_consoleMenuItems") then {
		MCC_consoleMenuItems = [];
	};
	
	MCC_consoleMenuItems pushBack [
		"Task Monitor",
		"Open task monitoring and management",
		"[] call MCC_fnc_openTaskMonitor;"
	];
};
