# 括号问题手动修复指南

生成时间: 2025-11-18 13:30:00

## 问题统计

- **总问题数**: 32 个括号不匹配问题
- **涉及文件数**: 21 个文件
- **问题类型分布**:
  - 括号类型不匹配 (mismatch): 大部分问题
  - 未闭合括号 (unclosed): 3 个问题

## 修复优先级

### 高优先级（简单修复）

#### 1. mcc\UI\fnc\fn_initCuratorAttribute.sqf
- **行 11, 列 75**: unclosed (括号: {)
- **问题**: 缺少闭合括号 `}`
- **修复**: 在行 11 末尾添加 `}`

**当前代码**:
```sqf
_path =  if (isClass (configFile >> "CfgPatches" >> "mcc_sandbox")) then {"\mcc_sandbox_mod\"} 	else {""};
```

**修复后**:
```sqf
_path =  if (isClass (configFile >> "CfgPatches" >> "mcc_sandbox")) then {"\mcc_sandbox_mod\"} 	else {""}};
```

---

#### 2. mcc\fnc\general\fn_keyToName.sqf
- **行 55, 列 10**: unclosed (括号: {)
- **问题**: 缺少闭合括号 `}`
- **修复**: 在行 55 后添加 `}`

**当前代码**:
```sqf
case 43:{"\"};
}
	case 44:{"Z"};
```

**修复后**:
```sqf
case 43:{"\"};
	}
}
	case 44:{"Z"};
```

---

#### 3. mcc\fnc\general\fn_pickItem.sqf
- **行 16, 列 27**: unclosed (括号: {)
- **问题**: 缺少闭合括号 `}`
- **修复**: 在行 16 后添加 `}`

**当前代码**:
```sqf
_path = if (_isMode) then {"\mcc_sandbox_mod\"} else {""};
};
```

**修复后**:
```sqf
_path = if (_isMode) then {"\mcc_sandbox_mod\"} else {""}};
};
```

---

### 中优先级（需要仔细检查）

#### 4. mcc\pop_menu\mcc_make_array_weapons.sqf
- **行 102, 列 9**: 括号不匹配 (开括号: {, 闭括号: ])
- **问题**: 行 103 有多余的 `]`
- **修复**: 删除多余的 `]`

**当前代码**:
```sqf
default {
U_EXPLOSIVE set [count U_EPLOSIVE, [_weaponDisplayName,_picture]]];
};
```

**修复后**:
```sqf
default {
U_EXPLOSIVE set [count U_EPLOSIVE, [_weaponDisplayName,_picture]]];
};
```

**注意**: 检查 `U_EPLOSIVE` 是否应该是 `U_EXPLOSIVE`（可能是拼写错误）

---

#### 5. mcc\pop_menu\spawn_group.sqf
- **行 113, 列 1**: 括号不匹配 (开括号: [, 闭括号: })
- **行 114, 列 1**: 括号不匹配 (开括号: [, 闭括号: })
- **问题**: 两行都有括号不匹配，可能是重复的代码
- **修复**: 检查并修复括号，删除重复行

**当前代码**:
```sqf
];
[[_center,_radius,_action,_intanse,_faction,mcc_sidename] remoteExec ["MCC_fnc_garrison", 0, false];
[[_center,_radius,_action,_intanse,_faction,mcc_sidename] remoteExec ["MCC_fnc_garrison", 0, false];
		};
```

**修复后** (删除重复行):
```sqf
];
[[_center,_radius,_action,_intanse,_faction,mcc_sidename] remoteExec ["MCC_fnc_garrison", 0, false];
		};
```

---

#### 6. mcc\settings\radioSettings.sqf
- **行 2, 列 1**: 括号不匹配 (开括号: [, 闭括号: })
- **问题**: 文件开头有括号不匹配
- **修复**: 检查文件结构

**当前代码**:
```sqf
//Enable MCC Radio System
[
    "MCC_VonRadio",
    ...
```

**需要检查**: 文件末尾是否有对应的闭合括号

---

#### 7. mcc\ai\fnc\fn_doHaltAI.sqf
- **行 62, 列 3**: 括号不匹配 (开括号: [, 闭括号: })
- **问题**: `remoteExec` 调用的括号不匹配
- **修复**: 检查并修复括号

**当前代码**:
```sqf
if (!(isNull _target) && !(isNull _unit)) then {
		[[_target, _unit], {
			_target = _this select 0;
			_men = _this select 1;
```

**需要检查**: 确保 `remoteExec` 调用的括号正确匹配

---

### 低优先级（复杂问题，需要上下文分析）

#### 8. mcc\LHD\fnc\fn_LHDspawnVehicle.sqf
- **行 345, 列 6**: 括号不匹配 (开括号: [, 闭括号: })
- **行 345, 列 14**: 括号不匹配 (开括号: [, 闭括号: })
- **行 354, 列 5**: 括号不匹配 (开括号: [, 闭括号: })
- **行 362, 列 29**: 括号不匹配 (开括号: {, 闭括号: ])
- **问题**: 多处括号不匹配，需要查看完整上下文

---

#### 9. mcc\cfg\modules\fnc\fn_weaponShopInit.sqf
- **行 48, 列 4**: 括号不匹配 (开括号: [, 闭括号: })
- **行 64, 列 29**: 括号不匹配 (开括号: {, 闭括号: ])
- **行 116, 列 2**: 括号不匹配 (开括号: [, 闭括号: })
- **行 132, 列 26**: 括号不匹配 (开括号: {, 闭括号: ])
- **问题**: 多处括号不匹配，需要查看完整上下文

---

## 修复步骤

### 步骤 1: 备份文件
```bash
# 脚本已自动备份到 backups 目录
# 如需手动备份：
cp addons/mcc_sandbox_mod/mcc/UI/fnc/fn_initCuratorAttribute.sqf backups/
```

### 步骤 2: 按优先级修复

1. **先修复简单问题**（高优先级）
   - `fn_initCuratorAttribute.sqf`
   - `fn_keyToName.sqf`
   - `fn_pickItem.sqf`

2. **再修复中等复杂度问题**（中优先级）
   - `mcc_make_array_weapons.sqf`
   - `spawn_group.sqf`
   - `radioSettings.sqf`
   - `fn_doHaltAI.sqf`

3. **最后处理复杂问题**（低优先级）
   - 需要查看完整上下文
   - 可能需要理解代码逻辑

### 步骤 3: 验证修复

```bash
# 运行脚本验证
python fix_sqf_brackets.py --dry-run
```

## 修复技巧

### 1. 括号类型不匹配
- **问题**: `[` 配 `}` 或 `{` 配 `]`
- **解决**: 找到对应的开括号，确定应该使用哪种括号类型

### 2. 未闭合括号
- **问题**: 缺少闭合括号
- **解决**: 在合适的位置添加闭合括号，注意缩进

### 3. 多余括号
- **问题**: 多余的闭合括号
- **解决**: 删除多余的括号

### 4. 嵌套括号
- **问题**: 括号嵌套层次错误
- **解决**: 仔细检查括号的嵌套关系

## 注意事项

⚠️ **重要提示**:
1. 修复前务必备份文件
2. 修复后运行脚本验证
3. 如果修复后仍有问题，检查代码逻辑
4. 某些问题可能需要理解代码上下文才能正确修复

## 快速修复脚本

可以创建一个简单的修复脚本来自动修复部分问题：

```python
# 示例：修复 fn_initCuratorAttribute.sqf
with open('addons/mcc_sandbox_mod/mcc/UI/fnc/fn_initCuratorAttribute.sqf', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 修复行 11
if len(lines) > 10:
    line = lines[10]  # 行 11 (0-based)
    if line.rstrip().endswith('""};'):
        lines[10] = line.rstrip() + '}\n'

with open('addons/mcc_sandbox_mod/mcc/UI/fnc/fn_initCuratorAttribute.sqf', 'w', encoding='utf-8') as f:
    f.writelines(lines)
```

## 问题列表（完整）

1. mcc\pop_menu\mcc_make_array_weapons.sqf - 行 102
2. mcc\pop_menu\spawn_group.sqf - 行 113, 114
3. mcc\settings\radioSettings.sqf - 行 2
4. mcc\UI\fnc\fn_initCuratorAttribute.sqf - 行 11 ✅ 简单
5. mcc\rts\scripts\mcc_logisticsBaseBuild.sqf - 行 1061
6. mcc\missionWizard\fnc\fn_MWObjectiveHVT.sqf - 行 195
7. mcc\LHD\fnc\fn_LHDspawnMenuInit.sqf - 行 261, 262
8. mcc\LHD\fnc\fn_LHDspawnVehicle.sqf - 行 345, 354, 362
9. mcc\interaction\fnc\fn_interactDoor.sqf - 行 120
10. mcc\general_scripts\convoy\make_convoy_WP.sqf - 行 10
11. mcc\general_scripts\evac\evac_move.sqf - 行 110, 292, 366
12. mcc\general_scripts\hostages\create_hostage.sqf - 行 27
13. mcc\general_scripts\unitManage\um.sqf - 行 27
14. mcc\fnc\general\fn_keyToName.sqf - 行 55 ✅ 简单
15. mcc\fnc\general\fn_pickItem.sqf - 行 16 ✅ 简单
16. mcc\fnc\MP\fn_construct_base.sqf - 行 113
17. mcc\cfg\modules\fnc\fn_weaponShopInit.sqf - 行 48, 64, 116, 132
18. mcc\bombDefuse\fnc\fn_bdButtonsModule.sqf - 行 24, 27
19. mcc\bombDefuse\fnc\fn_bdNumpadModule.sqf - 行 76
20. mcc\ambient\fnc\fn_ambientFirePlayerFiredEH.sqf - 行 11
21. mcc\ai\fnc\fn_doHaltAI.sqf - 行 62

