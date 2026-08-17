/*================================================MCC_fnc_MWCreateTaskOriginal====================================================================================================
// Find the mission Wizard's center - IMPROVED VERSION
// Example:[_obj,_task,_preciseMarker] call MCC_fnc_MWCreateTaskOriginal;
// _obj = position, objectice position
//_task = string, objective type
//_preciseMarker = Boolean, true - precise task marker
// Return - [taskName,Task pos]
//===================================================================================================================================================================*/
private ["_type","_stringName","_stringDescription","_pos","_objectName","_missionTime","_missionIntel","_indecator","_capturVar","_stateCond","_missionWherabouts","_pic","_sides","_taskId","_taskType","_vehicle","_group","_missionName"];

// MCC_fnc_MWCreateTask - create a mission objective module
_this params [
  ["_obj",objNull,[objNull]],
  ["_pos",[],[[]]],
  ["_task","",[""]],
  ["_preciseMarker",false,[false]],
  ["_side",sideLogic,[sideLogic]],
  ["_maxObjectivesDistance",400,[400]]
];

// Add error checking
if (_task == "") exitWith {
	diag_log "MCC MW: Error - Task type is empty";
	["MCC: Mission Wizard Error: Task type is empty"] spawn MCC_fnc_halt;
	[];
};

// Validate position
if (count _pos < 2) exitWith {
	diag_log "MCC MW: Error - Invalid position";
	[];
};

//define contesting sides
_sides = [east,west,resistance] - [_side];

//Global defines for briefings.
_missionTime =
   [
     localize "STR_MCC_MISSION_TIME_MORNING",
     localize "STR_MCC_MISSION_TIME_NIGHT",
     localize "STR_MCC_MISSION_TIME_YESTERDAY",
     localize "STR_MCC_MISSION_TIME_DAYS_AGO",
     localize "STR_MCC_MISSION_TIME_WEEK"
   ];

_missionIntel =
   [
     localize "STR_MCC_MISSION_INTEL_GATHERED",
     localize "STR_MCC_MISSION_INTEL_SATELLITE",
     localize "STR_MCC_MISSION_INTEL_INFORMANT",
     localize "STR_MCC_MISSION_INTEL_HIGH_COMMAND"
   ];

_missionWherabouts =
   [
      localize "STR_MCC_MISSION_WHEREABOUTS_LOCATION",
      localize "STR_MCC_MISSION_WHEREABOUTS_AREA",
      localize "STR_MCC_MISSION_WHEREABOUTS_SOMEWHERE",
      localize "STR_MCC_MISSION_WHEREABOUTS_CLOSE",
      localize "STR_MCC_MISSION_WHEREABOUTS_AROUND"
   ];

if (_pos isEqualTo []) then {_pos = getPos _obj};
if (count _pos ==2) then {_pos set [2,0]};

if !(_preciseMarker) then {
	_pos =  [(_pos select 0) + (random 300 - random 300),(_pos select 1) + (random 300 - random 300),(_pos select 2)];
};
_pic = "";

switch (_task) do {
   //Hostage
   case "secure_hvt": {
      if (isNull _obj) then {
         _objectName = "HVT";
      } else {
         _objectName = name _obj;
      };

      _stringName   = FORMAT ["Secure %1", _objectName];
      _stringDescription =  FORMAT ["Secure %2. <br/><br/>%3, HQ in their wisdom believe that since %1 %2 has been hiding %4.<br/>%2 is a most wanted HVT and should be considered armed and dangerous.<br/>Secure him alive and bring him back to base."
                             , _missionTime call BIS_fnc_selectRandom
                             , _objectName
                             , _missionIntel call BIS_fnc_selectRandom
                             , _missionWherabouts call BIS_fnc_selectRandom
                             , _stringName
							];
      _pic = "\A3\ui_f\data\igui\cfg\simpleTasks\types\walk_ca.paa";
      _taskType = "help";
   };

   //kill_hvt
   case "kill_hvt": {
      if (isNull _obj) then {
         _objectName = "HVT";
      } else {
         _objectName = name _obj;
      };

      _stringName   = FORMAT ["Kill or capture %1", _objectName];
      _stringDescription =  FORMAT ["Kill or capture %2. <br/><br/>%3, HQ in their wisdom believe that since %1 %2 has been hiding %4.<br/>%2 is a most wanted HVT and should be considered armed and dangerous.<br/>Capture him if possible, if not kill him. Either way, do not let him escape."
                             , _missionTime call BIS_fnc_selectRandom
                             , _objectName
                             , _missionIntel call BIS_fnc_selectRandom
                             , _missionWherabouts call BIS_fnc_selectRandom
                             , _stringName
							];
      _pic = "\a3\Missions_F_Bootcamp\data\img\Boot_m04_overview_CA.paa";
      _taskType = "kill";
   };

   //destroy_tanks
   case "destroy_tanks": {
      _objectName = if (isNull _obj) then {"Vehicle"} else {getText(configFile >> "CfgVehicles" >> typeof _obj >> "displayname")};
      _stringName   = FORMAT ["Destroy the prototype %1", _objectName];
      _stringDescription =  FORMAT ["Destroy the prototype %2.<br/><br/>%1 HQ received intel suggesting that the enemy has obtained a prototype %2.<br/>This is a game-changer and we must eliminate it by any means necessary.<br/>%3 the vehicle is hidden %4."
                             , _missionTime call BIS_fnc_selectRandom
                             , _objectName
                             , _missionIntel call BIS_fnc_selectRandom
                             , _missionWherabouts call BIS_fnc_selectRandom
                             , _stringName
                             ];
      _pic = "\a3\Missions_F_EPA\data\img\B_skirmish01_overview_CA.paa";
      _taskType = "destroy";
   };

   //destroy_aa
   case "destroy_aa": {
      _objectName = if (isNull _obj) then {"AA Vehicle"} else {getText(configFile >> "CfgVehicles" >> typeof _obj >> "displayname")};
      _stringName   = FORMAT ["Destroy the %1", _objectName];
      _stringDescription =  FORMAT ["Destroy the %2.<br/><br/>%1 HQ received intel suggesting that the enemy has obtained a %2.<br/>This is a game-changer and we must eliminate it by any means necessary.<br/>%3 the vehicle is hidden %4."
                             , _missionTime call BIS_fnc_selectRandom
                             , _objectName
                             , _missionIntel call BIS_fnc_selectRandom
                             , _missionWherabouts call BIS_fnc_selectRandom
                             , _stringName
                             ];
      _pic = "\a3\Missions_F_EPA\data\img\B_skirmish01_overview_CA.paa";
      _taskType = "destroy";
   };

   //destroy_artillery
   case "destroy_artillery": {
      _objectName = if (isNull _obj) then {"Artillery"} else {getText(configFile >> "CfgVehicles" >> typeof _obj >> "displayname")};
      _stringName   = FORMAT ["Destroy the %1", _objectName];
      _stringDescription =  FORMAT ["Destroy the %2.<br/><br/>%1 HQ received intel suggesting that the enemy has obtained a %2.<br/>This is a game-changer and we must eliminate it by any means necessary.<br/>%3 the vehicle is hidden %4."
                             , _missionTime call BIS_fnc_selectRandom
                             , _objectName
                             , _missionIntel call BIS_fnc_selectRandom
                             , _missionWherabouts call BIS_fnc_selectRandom
                             , _stringName
                             ];
      _pic = "\a3\Missions_F_EPA\data\img\B_skirmish01_overview_CA.paa";
      _taskType = "destroy";
   };

   //destroy_cache
   case "destroy_cache": {
      _objectName = if (isNull _obj) then {"Weapon Cache"} else {getText(configFile >> "CfgVehicles" >> typeof _obj >> "displayname")};
      _stringName   = FORMAT ["Destroy the %1", _objectName];
      _stringDescription =  FORMAT ["Destroy the %2.<br/><br/>%1 HQ received intel suggesting that the enemy has obtained a %2.<br/>This is a game-changer and we must eliminate it by any means necessary.<br/>%3 the vehicle is hidden %4."
                             , _missionTime call BIS_fnc_selectRandom
                             , _objectName
                             , _missionIntel call BIS_fnc_selectRandom
                             , _missionWherabouts call BIS_fnc_selectRandom
                             , _stringName
                             ];
      _pic = "\a3\Missions_F_EPA\data\img\B_skirmish01_overview_CA.paa";
      _taskType = "destroy";
   };

   //destroy_fuel
   case "destroy_fuel": {
      _objectName = if (isNull _obj) then {"Fuel Depot"} else {getText(configFile >> "CfgVehicles" >> typeof _obj >> "displayname")};
      _stringName   = FORMAT ["Destroy the %1", _objectName];
      _stringDescription =  FORMAT ["Destroy the %2.<br/><br/>%1 HQ received intel suggesting that the enemy has obtained a %2.<br/>This is a game-changer and we must eliminate it by any means necessary.<br/>%3 the vehicle is hidden %4."
                             , _missionTime call BIS_fnc_selectRandom
                             , _objectName
                             , _missionIntel call BIS_fnc_selectRandom
                             , _missionWherabouts call BIS_fnc_selectRandom
                             , _stringName
                             ];
      _pic = "\a3\Missions_F_EPA\data\img\B_skirmish01_overview_CA.paa";
      _taskType = "destroy";
   };

   //destroy_radar
   case "destroy_radar": {
      _objectName = if (isNull _obj) then {"Radar Station"} else {getText(configFile >> "CfgVehicles" >> typeof _obj >> "displayname")};
      _stringName   = FORMAT ["Destroy the %1", _objectName];
      _stringDescription =  FORMAT ["Destroy the %2.<br/><br/>%1 HQ received intel suggesting that the enemy has obtained a %2.<br/>This is a game-changer and we must eliminate it by any means necessary.<br/>%3 the vehicle is hidden %4."
                             , _missionTime call BIS_fnc_selectRandom
                             , _objectName
                             , _missionIntel call BIS_fnc_selectRandom
                             , _missionWherabouts call BIS_fnc_selectRandom
                             , _stringName
                             ];
      _pic = "\a3\Missions_F_EPA\data\img\B_skirmish01_overview_CA.paa";
      _taskType = "destroy";
   };

   //acquire_intel
   case "acquire_intel": {
      _objectName = if (isNull _obj) then {"Intel"} else {getText(configFile >> "CfgVehicles" >> typeof _obj >> "displayname")};
      _stringName   = FORMAT ["Acquire %1", _objectName];
      _stringDescription =  FORMAT ["Acquire %2.<br/><br/>%1 HQ received intel suggesting that the enemy has obtained a %2.<br/>This is a game-changer and we must eliminate it by any means necessary.<br/>%3 the vehicle is hidden %4."
                             , _missionTime call BIS_fnc_selectRandom
                             , _objectName
                             , _missionIntel call BIS_fnc_selectRandom
                             , _missionWherabouts call BIS_fnc_selectRandom
                             , _stringName
                             ];
      _pic = "\a3\Missions_F_EPA\data\img\B_skirmish01_overview_CA.paa";
      _taskType = "help";
   };

   //download_intel
   case "download_intel": {
      _objectName = if (isNull _obj) then {"Intel"} else {getText(configFile >> "CfgVehicles" >> typeof _obj >> "displayname")};
      _stringName   = FORMAT ["Download %1", _objectName];
      _stringDescription =  FORMAT ["Download %2.<br/><br/>%1 HQ received intel suggesting that the enemy has obtained a %2.<br/>This is a game-changer and we must eliminate it by any means necessary.<br/>%3 the vehicle is hidden %4."
                             , _missionTime call BIS_fnc_selectRandom
                             , _objectName
                             , _missionIntel call BIS_fnc_selectRandom
                             , _missionWherabouts call BIS_fnc_selectRandom
                             , _stringName
                             ];
      _pic = "\a3\Missions_F_EPA\data\img\B_skirmish01_overview_CA.paa";
      _taskType = "help";
   };

   //capture_area
   case "capture_area": {
      _objectName = if (isNull _obj) then {"Area"} else {getText(configFile >> "CfgVehicles" >> typeof _obj >> "displayname")};
      _stringName   = FORMAT ["Capture %1", _objectName];
      _stringDescription =  FORMAT ["Capture %2.<br/><br/>%1 HQ received intel suggesting that the enemy has obtained a %2.<br/>This is a game-changer and we must eliminate it by any means necessary.<br/>%3 the vehicle is hidden %4."
                             , _missionTime call BIS_fnc_selectRandom
                             , _objectName
                             , _missionIntel call BIS_fnc_selectRandom
                             , _missionWherabouts call BIS_fnc_selectRandom
                             , _stringName
                             ];
      _pic = "\a3\Missions_F_EPA\data\img\B_skirmish01_overview_CA.paa";
      _taskType = "help";
   };

   //disarm_ied
   case "disarm_ied": {
      _objectName = if (isNull _obj) then {"IED"} else {getText(configFile >> "CfgVehicles" >> typeof _obj >> "displayname")};
      _stringName   = FORMAT ["Disarm %1", _objectName];
      _stringDescription =  FORMAT ["Disarm %2.<br/><br/>%1 HQ received intel suggesting that the enemy has obtained a %2.<br/>This is a game-changer and we must eliminate it by any means necessary.<br/>%3 the vehicle is hidden %4."
                             , _missionTime call BIS_fnc_selectRandom
                             , _objectName
                             , _missionIntel call BIS_fnc_selectRandom
                             , _missionWherabouts call BIS_fnc_selectRandom
                             , _stringName
                             ];
      _pic = "\a3\Missions_F_EPA\data\img\B_skirmish01_overview_CA.paa";
      _taskType = "help";
   };

   default {
      _stringName = localize "STR_MCC_TASK_UNKNOWN";
      _stringDescription = localize "STR_MCC_TASK_DESCRIPTION_UNAVAILABLE";
      _pic = "\A3\ui_f\data\igui\cfg\simpleTasks\types\unknown_ca.paa";
      _taskType = "unknown";
   };
};

_missionName = _stringName;

// 创建任务组
_group = createGroup sideLogic;

// 检查任务模块类是否存在
if (!isClass (configFile >> "CfgVehicles" >> "MCC_ModuleObjective_FCurator")) exitWith {
	diag_log "MCC MW: Error - MCC_ModuleObjective_FCurator class not found";
	["MCC: Mission Wizard Error: Task module class not found"] spawn MCC_fnc_halt;
	[];
};

if (_task == "clear_area") then {
    _vehicle = _group createunit ["MCC_ModuleObjective_FCurator", _pos,[],0.5,"NONE"];
    
    // 检查车辆是否成功创建
    if (isNull _vehicle) exitWith {
		diag_log "MCC MW: Error - Failed to create task module";
		["MCC: Mission Wizard Error: Failed to create task module"] spawn MCC_fnc_halt;
		[];
	};
	
	// 设置创建时间用于清理
	_vehicle setVariable ["MCC_creationTime", time, true];
    
    _vehicle setVariable ["BIS_fnc_initModules_disableAutoActivation", false,true];
    _taskId = str _vehicle + str (["MCC_fnc_moduleObjective_id",1] call bis_fnc_counter);
    _vehicle setvariable ["RscAttributeOwners",_sides,true];
    if (typeName _obj == "OBJECT") then {_vehicle setvariable ["AttachObject_object",_obj,true]};
    _vehicle setvariable ["RscAttributeTaskState","created", true];
    _vehicle setvariable ["taskType",_taskType,true];
    _vehicle setvariable ["taskName",[_taskId,_missionName],true];
    _vehicle setvariable ["RscAttributeTaskDescription",[_stringDescription,_stringName,_stringName],true];

    //turn the sides into strings so we can compile it
    private _sidesStr = [];
    {_sidesStr pushBack str _x} forEach _sides;

    _vehicle setvariable ["OnOwnerChange",format ["if (str (_this select 1) in %1) then {(_this select 0) enableSimulation false};", _sidesStr],true];
    _vehicle setvariable ["type",4,true];
    _vehicle setvariable ["radius",_maxObjectivesDistance,true];
    _vehicle setvariable ["sides",[east,west,resistance],true];
    _vehicle setvariable ["owner",_side,true];

    {_x addCuratorEditableObjects [[_vehicle],false]} forEach allCurators;
    _vehicle setvariable ["updated",true,true];
} else {
  //spawn task for each side
  {
    _vehicle = _group createunit ["MCC_ModuleObjective_FCurator", _pos,[],0.5,"NONE"];
    
    // 检查车辆是否成功创建
    if (isNull _vehicle) then {
		diag_log "MCC MW: Error - Failed to create task module for side";
		continue; // 跳过这个阵营，继续处理下一个
	};
	
	// 设置创建时间用于清理
	_vehicle setVariable ["MCC_creationTime", time, true];
    
    _vehicle setVariable ["BIS_fnc_initModules_disableAutoActivation", false,true];
    _taskId = str _vehicle + str (["MCC_fnc_moduleObjective_id",1] call bis_fnc_counter);
    _vehicle setvariable ["RscAttributeOwners",[_x],true];
    if !(isNull _obj) then {_vehicle setvariable ["AttachObject_object",_obj,true]};
    _vehicle setvariable ["RscAttributeTaskState","created", true];
    _vehicle setvariable ["taskType",_taskType,true];
    _vehicle setvariable ["taskName",[_taskId,_missionName],true];
    _vehicle setvariable ["RscAttributeTaskDescription",[_stringDescription,_stringName,_stringName],true];

    if (!(isNull _obj) && _preciseMarker) then {
      _vehicle setvariable ["showMarker",[_obj,true],true];
       _vehicle setvariable ["show3d",true,true];
    } else {
      _vehicle setvariable ["showMarker",_pos,true];
       _vehicle setvariable ["show3d",false,true];
    };

    _vehicle setvariable ["proiority",0,true];
    _vehicle setvariable ["notification",true,true];

    {_x addCuratorEditableObjects [[_vehicle],false]} forEach allCurators;
    _vehicle setvariable ["updated",true,true];
  } foreach _sides;
};

MCC_MWObjectivesNames = [_pos,"",_stringName,_stringDescription,"",_pic,1,[],_vehicle];
publicVariable "MCC_MWObjectivesNames";

// 返回任务信息
[_pos,"",_stringName,_stringDescription,"",_pic,1,[],_vehicle]