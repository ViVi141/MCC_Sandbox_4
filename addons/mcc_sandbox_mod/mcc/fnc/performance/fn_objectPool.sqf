/*
	File: fn_objectPool.sqf
	Author: MCC Sandbox Team
	Description: Object pooling system for performance optimization
	
	This system reduces object creation/destruction overhead by
	reusing objects from a pool.
*/

// Object pool storage
MCC_objectPools = createHashMap;

// Initialize object pools
MCC_fnc_initObjectPools = {
	// Vehicle pool
	MCC_objectPools set ["vehicles", []];
	
	// Unit pool
	MCC_objectPools set ["units", []];
	
	// Marker pool
	MCC_objectPools set ["markers", []];
	
	// Effect pool
	MCC_objectPools set ["effects", []];
	
	// Helper pool
	MCC_objectPools set ["helpers", []];
	
	diag_log localize "STR_MCC_OBJECT_POOLS_INITIALIZED";
};

// Get object from pool
MCC_fnc_getFromPool = {
	params ["_poolType", "_createFunction"];
	
	_pool = MCC_objectPools get _poolType;
	if (isNil "_pool") then {
		_pool = [];
		MCC_objectPools set [_poolType, _pool];
	};
	
	_object = nil;
	if (count _pool > 0) then {
		_object = _pool deleteAt 0;
		// Reset object state
		[_object] call MCC_fnc_resetPooledObject;
	} else {
		// Create new object if pool is empty
		_object = call _createFunction;
	};
	
	_object
};

// Return object to pool
MCC_fnc_returnToPool = {
	params ["_object", "_poolType"];
	
	if (isNull _object) exitWith {};
	
	_pool = MCC_objectPools get _poolType;
	if (isNil "_pool") then {
		_pool = [];
		MCC_objectPools set [_poolType, _pool];
	};
	
	// Hide object instead of deleting
	_object hideObjectGlobal true;
	_object enableSimulation false;
	
	_pool pushBack _object;
	
	// Limit pool size
	_maxPoolSize = 50;
	if (count _pool > _maxPoolSize) then {
		_excessObject = _pool deleteAt 0;
		deleteVehicle _excessObject;
	};
};

// Reset pooled object state
MCC_fnc_resetPooledObject = {
	params ["_object"];
	
	// Reset common properties
	_object hideObjectGlobal false;
	_object enableSimulation true;
	_object setDamage 0;
	_object setFuel 1;
	
	// Clear cargo
	clearWeaponCargoGlobal _object;
	clearMagazineCargoGlobal _object;
	clearItemCargoGlobal _object;
	clearBackpackCargoGlobal _object;
	
	// Reset position
	_object setPos [0,0,0];
	_object setDir 0;
	_object setVelocity [0,0,0];
};

// Create pooled vehicle
MCC_fnc_createPooledVehicle = {
	params ["_vehicleClass", "_position", "_direction"];
	
	_vehicle = [_vehicleClass, _position, _direction] call MCC_fnc_getFromPool;
	if (isNull _vehicle) then {
		_vehicle = _vehicleClass createVehicle _position;
		_vehicle setDir _direction;
	};
	
	_vehicle
};

// Create pooled unit
MCC_fnc_createPooledUnit = {
	params ["_unitClass", "_position", "_group"];
	
	_unit = [_unitClass, _position, _group] call MCC_fnc_getFromPool;
	if (isNull _unit) then {
		_unit = _group createUnit [_unitClass, _position, [], 0, "NONE"];
	};
	
	_unit
};

// Create pooled marker
MCC_fnc_createPooledMarker = {
	params ["_markerName", "_position", "_shape", "_size", "_color", "_text"];
	
	_marker = [_markerName, _position, _shape, _size, _color, _text] call MCC_fnc_getFromPool;
	if (isNull _marker) then {
		_marker = createMarker [_markerName, _position];
		_marker setMarkerShape _shape;
		_marker setMarkerSize _size;
		_marker setMarkerColor _color;
		_marker setMarkerText _text;
	};
	
	_marker
};

// Clean up object pools
MCC_fnc_cleanupObjectPools = {
	{
		_poolType = _x;
		_pool = MCC_objectPools get _poolType;
		
		// Delete all objects in pool
		{
			if (!isNull _x) then {
				deleteVehicle _x;
			};
		} forEach _pool;
		
		// Clear pool
		MCC_objectPools set [_poolType, []];
	} forEach (keys MCC_objectPools);
	
	diag_log localize "STR_MCC_OBJECT_POOLS_CLEANED";
};

// Get pool statistics
MCC_fnc_getPoolStats = {
	_stats = createHashMap;
	
	{
		_poolType = _x;
		_pool = MCC_objectPools get _poolType;
		_stats set [_poolType, count _pool];
	} forEach (keys MCC_objectPools);
	
	_stats
};

// Initialize pools on mission start
if (isServer) then {
	[] call MCC_fnc_initObjectPools;
};
