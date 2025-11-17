# remoteExec 使用检查报告

生成时间: 2025-11-18 04:12:36

## 统计信息

- **总问题数**: 24
- **已修复**: 11
- **跳过**: 13
- **错误**: 0

## 问题分类

- **null_check**: 24 个

## 修复建议

### bon_artillery\bon_arti_fire.sqf

#### 行 47 [null_check]

**原始代码**:
```sqf
					[[netid _requestor,_requestor], "shoutS5"] remoteExec ["MCC_fnc_globalSay3D", 0, false];
```

**说明**: 在使用 netId 或对象作为 remoteExec 参数前，没有检查对象是否为 null。

**置信度**: 1.00

---

#### 行 49 [null_check]

**原始代码**:
```sqf
					[[netid _requestor,_requestor], "shoutO5"] remoteExec ["MCC_fnc_globalSay3D", 0, false];
```

**说明**: 在使用 netId _requestor 之前没有检查 _requestor 是否为 null。

**置信度**: 0.95

---

#### 行 66 [null_check]

**原始代码**:
```sqf
					[[netid _requestor,_requestor], "splashS6"] remoteExec ["MCC_fnc_globalSay3D", 0, false];
```

**修复后**:
```sqf
if (!(isNull _requestor)) then { [[netid _requestor,_requestor], "splashS6"] remoteExec ["MCC_fnc_globalSay3D", 0, false]; };
```

**说明**: 在使用 netId _requestor 之前没有检查 _requestor 是否为 null。

**置信度**: 1.00

---

#### 行 68 [null_check]

**原始代码**:
```sqf
					[[netid _requestor,_requestor], "splashO6"] remoteExec ["MCC_fnc_globalSay3D", 0, false];
```

**修复后**:
```sqf
if (!(isNull _requestor)) then {
    [[netid _requestor,_requestor], "splashO6"] remoteExec ["MCC_fnc_globalSay3D", 0, false];
};
```

**说明**: 在使用 netId _requestor 之前没有进行 null 检查。如果 _requestor 是 null，则会报错。

**置信度**: 1.00

---

### bon_artillery\bon_arti_request.sqf

#### 行 57 [null_check]

**原始代码**:
```sqf
	[[netid _this,_this], "requestO1"] remoteExec ["MCC_fnc_globalSay3D", 0, false];
```

**说明**: 在使用 netId 或对象作为 remoteExec 参数前，没有检查对象是否为 null。

**置信度**: 1.00

---

#### 行 59 [null_check]

**原始代码**:
```sqf
	[[netid _this,_this], "requestS1", "MCC_fnc_globalSay3D", true, false] remoteExec ["MCC_fnc_globalSay3D", 0, true];
```

**说明**: 在使用 netId 或对象作为 remoteExec 参数前，没有检查对象是否为 null。

**置信度**: 1.00

---

#### 行 73 [null_check]

**原始代码**:
```sqf
		[[netid _requestor,_requestor], "gridO2"] remoteExec ["MCC_fnc_globalSay3D", 0, false];
```

**说明**: 在使用 netId _requestor 之前没有进行 null 检查。如果 _requestor 是 null，调用 netId 会导致错误。

**置信度**: 0.95

---

#### 行 75 [null_check]

**原始代码**:
```sqf
		[[netid _requestor,_requestor], "gridS2", "MCC_fnc_globalSay3D", true, false] remoteExec ["MCC_fnc_globalSay3D", _requestor, true, false];
```

**说明**: 在使用 netId _requestor 之前没有进行 null 检查。如果 _requestor 为 null，则会报错。

**置信度**: 1.00

---

#### 行 77 [null_check]

**原始代码**:
```sqf
		[[netid _requestor,_requestor], "splashO3"] remoteExec ["MCC_fnc_globalSay3D", 0, true, false];
```

**说明**: 在使用 netId 或对象作为 remoteExec 参数前，没有检查对象是否为 null。

**置信度**: 0.90

---

#### 行 79 [null_check]

**原始代码**:
```sqf
		[[netid _requestor,_requestor], "splashS3"] remoteExec ["MCC_fnc_globalSay3D", 0, false];
```

**说明**: 在使用 netId _requestor 之前没有进行 null 检查。如果 _requestor 为 null，则会报错。

**置信度**: 1.00

---

#### 行 81 [null_check]

**原始代码**:
```sqf
		[[netid _requestor,_requestor], "messegeS4"] remoteExec ["MCC_fnc_globalSay3D", 0, false];
```

**说明**: 在使用 netId 或对象作为 remoteExec 参数前，没有检查对象是否为 null。

**置信度**: 1.00

---

#### 行 83 [null_check]

**原始代码**:
```sqf
		[[netid _requestor,_requestor], "messegeO4"] remoteExec ["MCC_fnc_globalSay3D", 0, false];
```

**说明**: 在使用 netId _requestor 之前没有进行 null 检查。如果 _requestor 是 null，调用 netId 会导致错误。

**置信度**: 0.95

---

#### 行 92 [null_check]

**原始代码**:
```sqf
		[[netid _requestor,_requestor], "gridO2"] remoteExec ["MCC_fnc_globalSay3D", 0, false];
```

**说明**: 在使用 netId 或对象作为 remoteExec 参数前，没有检查对象是否为 null。

**置信度**: 0.95

---

#### 行 94 [null_check]

**原始代码**:
```sqf
		[[netid _requestor,_requestor], "gridS2", "MCC_fnc_globalSay3D", true, false] remoteExec ["MCC_fnc_globalSay3D", 0, false];
```

**说明**: 在使用 netId _requestor 之前没有检查 _requestor 是否为 null。

**置信度**: 0.95

---

#### 行 96 [null_check]

**原始代码**:
```sqf
		[[netid _requestor,_requestor], "splashO3", "MCC_fnc_globalSay3D", true, false] remoteExec ["MCC_fnc_globalSay3D", _requestor, true];
```

**修复后**:
```sqf
if (!(isNull _requestor)) then {
    [[netid _requestor,_requestor], "splashO3", "MCC_fnc_globalSay3D", true, false] remoteExec ["MCC_fnc_globalSay3D", _requestor, true];
};
```

**说明**: 在使用 netId _requestor 之前没有检查 _requestor 是否为 null。

**置信度**: 1.00

---

#### 行 98 [null_check]

**原始代码**:
```sqf
		[[netid _requestor,_requestor], "splashS3"] remoteExec ["MCC_fnc_globalSay3D", 0, false];
```

**修复后**:
```sqf
if (!(isNull _requestor)) then { [[netid _requestor,_requestor], "splashS3"] remoteExec ["MCC_fnc_globalSay3D", 0, false]; };
```

**说明**: 在使用 netId _requestor 之前没有检查 _requestor 是否为 null。

**置信度**: 1.00

---

### init.sqf

#### 行 774 [null_check]

**原始代码**:
```sqf
			[2,compile _command] remoteExec ["MCC_fnc_globalExecute", true, false];
```

**修复后**:
```sqf
[2,compile _command] remoteExec ["MCC_fnc_globalExecute", true, false];
```

**说明**: 在 remoteExec 调用前没有检查 _command 是否为 null。

**置信度**: 1.00

---

#### 行 964 [null_check]

**原始代码**:
```sqf
												[getPlayerUID _healer,200,"For Healing"] remoteExec ["MCC_fnc_addRating", _healer, false];
```

**修复后**:
```sqf
[getPlayerUID _healer,200,"For Healing"] remoteExec ["MCC_fnc_addRating", _healer, false];
```

**说明**: 在 remoteExec 调用前没有检查 _healer 是否为 null。

**置信度**: 1.00

---

#### 行 1005 [null_check]

**原始代码**:
```sqf
				_null = [(compile format ["MCC_curator addCuratorEditableObjects [[objectFromNetId '%1'],false];",netid player])] remoteExec ["BIS_fnc_spawn", 2, false];
```

**修复后**:
```sqf
if (!(isNull player)) then {
    _null = [(compile format ["MCC_curator addCuratorEditableObjects [[objectFromNetId '%1'],false];",netid player])] remoteExec ["BIS_fnc_spawn", 2, false];
};
```

**说明**: 在使用 netId player 之前没有检查 player 是否为 null。

**置信度**: 1.00

---

#### 行 1048 [null_check]

**原始代码**:
```sqf
															[_unit, 5] remoteExec ["MCC_fnc_stunBehav",_unit];
```

**修复后**:
```sqf
if (!(isNull _unit)) then {
    [_unit, 5] remoteExec ["MCC_fnc_stunBehav",_unit];
};
```

**说明**: 在调用 remoteExec 之前没有检查 _unit 是否为 null。

**置信度**: 1.00

---

### mcc\dialogs\mcc_boxGen_change.sqf

#### 行 206 [null_check]

**原始代码**:
```sqf
			 mcc_safe = mcc_safe + FORMAT ["[%1, %2, %3, %4, %5, %6] remoteExec [""MCC_fnc_boxGenerator"", 0, false];
```

**说明**: 在使用 remoteExec 之前没有检查对象是否为 null。

**置信度**: 0.90

---

#### 行 208 [null_check]

**原始代码**:
```sqf
			[MCC3DValue select 0, MCC3DValue select 1, tempBoxWeapons, tempBoxMagazine, tempBoxItems, tempBoxRucks] remoteExec ["MCC_fnc_boxGenerator", 0, false];
```

**修复后**:
```sqf
[MCC3DValue select 0, MCC3DValue select 1, tempBoxWeapons, tempBoxMagazine, tempBoxItems, tempBoxRucks] remoteExec ["MCC_fnc_boxGenerator", 0, false];
```

**说明**: 在 remoteExec 调用前没有检查对象是否为 null。

**置信度**: 1.00

---

### mcc\dialogs\mcc_groupGen_init.sqf

#### 行 33 [null_check]

**原始代码**:
```sqf
if (player != getAssignedCuratorUnit MCC_curator) then { [compile format ["objectFromNetId '%1' assignCurator MCC_curator;", netid player]] remoteExec ["BIS_fnc_spawn", 2, false]; };
```

**修复后**:
```sqf
if (player != getAssignedCuratorUnit MCC_curator) then { if !(isNull player) then { [compile format ['objectFromNetId '%1' assignCurator MCC_curator;', netid player]] remoteExec ['BIS_fnc_spawn', 2, false]; }; };
```

**说明**: 在使用 netId player 之前没有检查 player 是否为 null。

**置信度**: 1.00

---

#### 行 150 [null_check]

**原始代码**:
```sqf
		[1] remoteExec ["MCC_fnc_FPS", 0, false];
```

**修复后**:
```sqf
[1] remoteExec ["MCC_fnc_FPS", 0, false];
```

**说明**: 在 remoteExec 调用前没有检查对象是否为 null。

**置信度**: 1.00

---

