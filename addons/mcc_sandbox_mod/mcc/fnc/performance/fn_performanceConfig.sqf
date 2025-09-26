/*
	File: fn_performanceConfig.sqf
	Author: MCC Sandbox Team
	Description: Performance configuration and settings
	
	This file contains all performance-related settings and
	configuration options for the MCC Sandbox mod.
*/

// Performance configuration
MCC_performanceConfig = createHashMap;

// Object creation settings
MCC_performanceConfig set ["objectPooling", true];
MCC_performanceConfig set ["maxObjects", 1000];
MCC_performanceConfig set ["objectCleanupInterval", 300]; // 5 minutes

// AI optimization settings
MCC_performanceConfig set ["maxAIUnits", 50];
MCC_performanceConfig set ["aiUpdateInterval", 5];
MCC_performanceConfig set ["aiDisableDistance", 1000];
MCC_performanceConfig set ["aiEnableDistance", 500];
MCC_performanceConfig set ["aiSkillReduction", 0.1];

// Network optimization settings
MCC_performanceConfig set ["networkBatchSize", 10];
MCC_performanceConfig set ["networkUpdateInterval", 1];
MCC_performanceConfig set ["maxNetworkOperations", 100];

// Memory management settings
MCC_performanceConfig set ["memoryCleanupInterval", 600]; // 10 minutes
MCC_performanceConfig set ["maxMemoryUsage", 80]; // Percentage
MCC_performanceConfig set ["garbageCollectionInterval", 120]; // 2 minutes

// Rendering optimization settings
MCC_performanceConfig set ["lodDistance", 1000];
MCC_performanceConfig set ["shadowDistance", 500];
MCC_performanceConfig set ["particleDensity", 0.5];

// Performance monitoring settings
MCC_performanceConfig set ["monitoringEnabled", true];
MCC_performanceConfig set ["monitoringInterval", 30];
MCC_performanceConfig set ["logPerformance", true];
MCC_performanceConfig set ["performanceWarnings", true];

// Get configuration value
MCC_fnc_getPerformanceConfig = {
	params ["_key", "_defaultValue"];
	
	_value = MCC_performanceConfig get _key;
	if (isNil "_value") then {
		_value = _defaultValue;
		MCC_performanceConfig set [_key, _defaultValue];
	};
	
	_value
};

// Set configuration value
MCC_fnc_setPerformanceConfig = {
	params ["_key", "_value"];
	
	MCC_performanceConfig set [_key, _value];
	
	// Apply changes if needed
	[] call MCC_fnc_applyPerformanceConfig;
};

// Apply performance configuration
MCC_fnc_applyPerformanceConfig = {
	// Apply AI settings
	_maxAI = [MCC_performanceConfig, "maxAIUnits"] call MCC_fnc_getPerformanceConfig;
	if (!isNil "MCC_aiOptimizationSettings") then {
		MCC_aiOptimizationSettings set [0, ["maxAIUnits", _maxAI]];
	};
	
	// Apply object pooling
	_objectPooling = [MCC_performanceConfig, "objectPooling"] call MCC_fnc_getPerformanceConfig;
	if (_objectPooling && !isNil "MCC_fnc_initObjectPools") then {
		[] call MCC_fnc_initObjectPools;
	};
	
	// Apply monitoring
	_monitoringEnabled = [MCC_performanceConfig, "monitoringEnabled"] call MCC_fnc_getPerformanceConfig;
	if (_monitoringEnabled && !isNil "MCC_fnc_performanceMonitor") then {
		[] call MCC_fnc_performanceMonitor;
	};
};

// Load performance configuration from profile
MCC_fnc_loadPerformanceConfig = {
	_profileKey = "MCC_PerformanceConfig";
	_savedConfig = profileNamespace getVariable [_profileKey, []];
	
	if (count _savedConfig > 0) then {
		{
			_key = _x select 0;
			_value = _x select 1;
			MCC_performanceConfig set [_key, _value];
		} forEach _savedConfig;
		
		diag_log localize "STR_MCC_PERFORMANCE_CONFIG_LOADED";
	} else {
		diag_log localize "STR_MCC_PERFORMANCE_CONFIG_DEFAULTS";
	};
	
	[] call MCC_fnc_applyPerformanceConfig;
};

// Save performance configuration to profile
MCC_fnc_savePerformanceConfig = {
	_profileKey = "MCC_PerformanceConfig";
	_configArray = [];
	
	{
		_key = _x;
		_value = MCC_performanceConfig get _key;
		_configArray pushBack [_key, _value];
	} forEach (keys MCC_performanceConfig);
	
	profileNamespace setVariable [_profileKey, _configArray];
	saveProfileNamespace;
	
	diag_log localize "STR_MCC_PERFORMANCE_CONFIG_SAVED";
};

// Reset to default configuration
MCC_fnc_resetPerformanceConfig = {
	MCC_performanceConfig = createHashMap;
	
	// Reinitialize with defaults
	[] call MCC_fnc_loadPerformanceConfig;
	
	diag_log localize "STR_MCC_PERFORMANCE_CONFIG_RESET";
};

// Get performance statistics
MCC_fnc_getPerformanceStats = {
	_stats = createHashMap;
	
	// Object statistics
	_stats set ["totalObjects", count allMissionObjects "All"];
	_stats set ["vehicles", count vehicles];
	_stats set ["units", count allUnits];
	_stats set ["markers", count allMapMarkers];
	
	// AI statistics
	if (!isNil "MCC_aiUnits") then {
		_stats set ["aiUnits", count MCC_aiUnits];
		_stats set ["activeAI", count (MCC_aiUnits select {alive _x && simulationEnabled _x})];
	};
	
	// Performance metrics
	_stats set ["fps", diag_fps];
	_stats set ["frameTime", diag_fpsMin];
	_stats set ["memory", count allMissionObjects "All"];
	
	_stats
};

// Performance optimization presets
MCC_fnc_setPerformancePreset = {
	params ["_preset"];
	
	switch (_preset) do {
		case "low": {
			[["maxAIUnits", 25]] call MCC_fnc_setPerformanceConfig;
			[["objectPooling", false]] call MCC_fnc_setPerformanceConfig;
			[["aiUpdateInterval", 10]] call MCC_fnc_setPerformanceConfig;
			[["monitoringInterval", 60]] call MCC_fnc_setPerformanceConfig;
			[["unlimitedMode", false]] call MCC_fnc_setPerformanceConfig;
		};
		case "medium": {
			[["maxAIUnits", 50]] call MCC_fnc_setPerformanceConfig;
			[["objectPooling", true]] call MCC_fnc_setPerformanceConfig;
			[["aiUpdateInterval", 5]] call MCC_fnc_setPerformanceConfig;
			[["monitoringInterval", 30]] call MCC_fnc_setPerformanceConfig;
			[["unlimitedMode", false]] call MCC_fnc_setPerformanceConfig;
		};
		case "high": {
			[["maxAIUnits", 100]] call MCC_fnc_setPerformanceConfig;
			[["objectPooling", true]] call MCC_fnc_setPerformanceConfig;
			[["aiUpdateInterval", 2]] call MCC_fnc_setPerformanceConfig;
			[["monitoringInterval", 15]] call MCC_fnc_setPerformanceConfig;
			[["unlimitedMode", false]] call MCC_fnc_setPerformanceConfig;
		};
		case "unlimited": {
			[["maxAIUnits", 9999]] call MCC_fnc_setPerformanceConfig;
			[["maxObjects", 9999]] call MCC_fnc_setPerformanceConfig;
			[["objectPooling", false]] call MCC_fnc_setPerformanceConfig;
			[["aiUpdateInterval", 1]] call MCC_fnc_setPerformanceConfig;
			[["monitoringInterval", 5]] call MCC_fnc_setPerformanceConfig;
			[["unlimitedMode", true]] call MCC_fnc_setPerformanceConfig;
			[["aiDisableDistance", 99999]] call MCC_fnc_setPerformanceConfig;
			[["aiEnableDistance", 99999]] call MCC_fnc_setPerformanceConfig;
		};
	};
	
	diag_log format [localize "STR_MCC_PERFORMANCE_PRESET_APPLIED", _preset];
};

// Add performance menu to MCC console
MCC_fnc_addPerformanceMenu = {
	// Add performance menu to MCC console
	if (!isNil "MCC_consoleMenuItems") then {
		MCC_consoleMenuItems pushBack ["Performance Monitor", "[] call MCC_fnc_displayPerformanceInfo;", "Performance monitoring and optimization"];
		MCC_consoleMenuItems pushBack ["Performance Settings", "[] call MCC_fnc_openPerformanceSettings;", "Configure performance settings"];
		MCC_consoleMenuItems pushBack ["Performance Presets", "[] call MCC_fnc_openPerformancePresets;", "Quick performance presets"];
	};
};

// Open performance settings dialog
MCC_fnc_openPerformanceSettings = {
	createDialog "MCC_PerformanceSettings";
	
	// Populate settings
	[] spawn {
		waitUntil {!isNull (findDisplay 12346)};
		
		// CPU threshold
		_ctrl = (findDisplay 12346) displayCtrl 2001;
		if (!isNull _ctrl) then {
			_cpuThreshold = [MCC_performanceConfig, "cpuThreshold", 80] call MCC_fnc_getPerformanceConfig;
			_ctrl ctrlSetText str _cpuThreshold;
		};
		
		// Memory threshold
		_ctrl = (findDisplay 12346) displayCtrl 2002;
		if (!isNull _ctrl) then {
			_memThreshold = [MCC_performanceConfig, "memoryThreshold", 70] call MCC_fnc_getPerformanceConfig;
			_ctrl ctrlSetText str _memThreshold;
		};
		
		// AI limit
		_ctrl = (findDisplay 12346) displayCtrl 2003;
		if (!isNull _ctrl) then {
			_aiLimit = [MCC_performanceConfig, "maxAIUnits", 50] call MCC_fnc_getPerformanceConfig;
			_ctrl ctrlSetText str _aiLimit;
		};
	};
};

// Open performance presets dialog
MCC_fnc_openPerformancePresets = {
	createDialog "MCC_PerformancePresets";
	
	// Add preset buttons
	[] spawn {
		waitUntil {!isNull (findDisplay 12347)};
		
		// Low performance button
		_ctrl = (findDisplay 12347) displayCtrl 3001;
		if (!isNull _ctrl) then {
			_ctrl ctrlAddEventHandler ["ButtonClick", {
				["low"] call MCC_fnc_setPerformancePreset;
				hint localize "STR_MCC_PERFORMANCE_LOW_APPLIED";
				closeDialog 0;
			}];
		};
		
		// Medium performance button
		_ctrl = (findDisplay 12347) displayCtrl 3002;
		if (!isNull _ctrl) then {
			_ctrl ctrlAddEventHandler ["ButtonClick", {
				["medium"] call MCC_fnc_setPerformancePreset;
				hint localize "STR_MCC_PERFORMANCE_MEDIUM_APPLIED";
				closeDialog 0;
			}];
		};
		
		// High performance button
		_ctrl = (findDisplay 12347) displayCtrl 3003;
		if (!isNull _ctrl) then {
			_ctrl ctrlAddEventHandler ["ButtonClick", {
				["high"] call MCC_fnc_setPerformancePreset;
				hint localize "STR_MCC_PERFORMANCE_HIGH_APPLIED";
				closeDialog 0;
			}];
		};
		
		// Unlimited performance button
		_ctrl = (findDisplay 12347) displayCtrl 3004;
		if (!isNull _ctrl) then {
			_ctrl ctrlAddEventHandler ["ButtonClick", {
				["unlimited"] call MCC_fnc_setPerformancePreset;
				hint localize "STR_MCC_PERFORMANCE_UNLIMITED_APPLIED";
				closeDialog 0;
			}];
		};
	};
};

// Apply performance settings from dialog
MCC_fnc_applyPerformanceSettings = {
	// Get values from dialog
	_cpuThreshold = parseNumber (ctrlText ((findDisplay 12346) displayCtrl 2001));
	_memThreshold = parseNumber (ctrlText ((findDisplay 12346) displayCtrl 2002));
	_aiLimit = parseNumber (ctrlText ((findDisplay 12346) displayCtrl 2003));
	_objectPooling = cbChecked ((findDisplay 12346) displayCtrl 2004);
	_monitoring = cbChecked ((findDisplay 12346) displayCtrl 2005);
	
	// Apply settings
	MCC_performanceConfig set ["cpuThreshold", _cpuThreshold];
	MCC_performanceConfig set ["memoryThreshold", _memThreshold];
	MCC_performanceConfig set ["maxAIUnits", _aiLimit];
	MCC_performanceConfig set ["objectPooling", _objectPooling];
	MCC_performanceConfig set ["monitoringEnabled", _monitoring];
	
	// Save to profile
	[] call MCC_fnc_savePerformanceConfig;
	
	// Apply changes
	[] call MCC_fnc_applyPerformanceConfig;
	
	hint localize "STR_MCC_PERFORMANCE_SETTINGS_APPLIED";
	closeDialog 0;
};

// Initialize performance configuration
if (isServer) then {
	[] call MCC_fnc_loadPerformanceConfig;
	[] call MCC_fnc_addPerformanceMenu;
};
