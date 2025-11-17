# 括号嵌套检查报告

生成时间: 2025-11-18 03:49:04

## 统计信息

- **总文件数**: 1571
- **有问题的文件**: 54
- **总问题数**: 277

## 详细结果

### addons\mcc_sandbox_mod\mcc\bombDefuse\fnc\fn_bdButtonsModule.sqf

**总行数**: 99
**问题数**: 16

#### ❌ 未闭合的括号

🔴 **行 23，列 68** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if ((_serialNumber mod 3) == 0 && (_serialNumber mod 7) == 0) then {
```

🔴 **行 24，列 28** (方括号)

**问题**: 未闭合的括号 '['（期望 ']'）

**代码**:
```sqf
_buttonsCombinations = [["@",false],["1",false],["^",true],["~",true],[")",true],["]",true],["(",false],["[",true],["|",true],["\",false],["/",false],["?",false],["3",false],["%",false],["*",true],["L",true],["8",true],["5",false],[";",true],["A",false],["a",true],["g",false],["G",true],["b",false],["B",true],["p",false],["P",true],["w",true],["W",false],["m",true],["n",false],["N",true],["M",false],["t",true],["T",false],["`",true],[":",false],["o",true],["0",false]];
```

🔴 **行 25，列 8** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
} else {
```

🔴 **行 26，列 42** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if ((_serialNumber mod 3) == 0) then {
```

🔴 **行 27，列 29** (方括号)

**问题**: 未闭合的括号 '['（期望 ']'）

**代码**:
```sqf
_buttonsCombinations = [["@",false],["1",false],["^",false],["~",true],[")",true],["]",true],["(",false],["[",true],["|",true],["\",false],["/",false],["?",false],["3",false],["%",true],["*",false],["L",true],["8",false],["5",false],[";",true],["A",true],["a",false],["g",false],["G",true],["b",true],["B",true],["p",true],["P",false],["w",true],["W",false],["m",false],["n",false],["N",false],["M",true],["t",true],["T",true],["`",false],[":",false],["o",true],["0",false]];
```

🔴 **行 28，列 12** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
} else {
```

🔴 **行 68，列 27** (方括号)

**问题**: 未闭合的括号 '['（期望 ']'）

**代码**:
```sqf
_ctrl ctrlAddEventHandler ['MouseButtonUp',format [
```

🔴 **行 68，列 51** (方括号)

**问题**: 未闭合的括号 '['（期望 ']'）

**代码**:
```sqf
_ctrl ctrlAddEventHandler ['MouseButtonUp',format [
```

#### ❌ 括号类型不匹配

🟠 **行 24，列 131** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 24 行第 131 列

**代码**:
```sqf
_buttonsCombinations = [["@",false],["1",false],["^",true],["~",true],[")",true],["]",true],["(",false],["[",true],["|",true],["\",false],["/",false],["?",false],["3",false],["%",false],["*",true],["L",true],["8",true],["5",false],[";",true],["A",false],["a",true],["g",false],["G",true],["b",false],["B",true],["p",false],["P",true],["w",true],["W",false],["m",true],["n",false],["N",true],["M",false],["t",true],["T",false],["`",true],[":",false],["o",true],["0",false]];
```

🟠 **行 25，列 1** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 24 行第 131 列）

**代码**:
```sqf
} else {
```

🟠 **行 27，列 133** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 27 行第 133 列

**代码**:
```sqf
_buttonsCombinations = [["@",false],["1",false],["^",false],["~",true],[")",true],["]",true],["(",false],["[",true],["|",true],["\",false],["/",false],["?",false],["3",false],["%",true],["*",false],["L",true],["8",false],["5",false],[";",true],["A",true],["a",false],["g",false],["G",true],["b",true],["B",true],["p",true],["P",false],["w",true],["W",false],["m",false],["n",false],["N",false],["M",true],["t",true],["T",true],["`",false],[":",false],["o",true],["0",false]];
```

🟠 **行 28，列 5** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 27 行第 133 列）

**代码**:
```sqf
} else {
```

🟠 **行 29，列 32** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 29 行第 32 列

**代码**:
```sqf
_buttonsCombinations = [["@",false],["1",false],["^",true],["~",false],[")",true],["]",false],["(",true],["[",false],["|",false],["\",false],["/",false],["?",true],["3",true],["%",true],["*",true],["L",true],["8",true],["5",false],[";",false],["A",false],["a",true],["g",true],["G",false],["b",false],["B",true],["p",false],["P",false],["w",false],["W",false],["m",true],["n",false],["N",true],["M",false],["t",true],["T",false],["`",true],[":",false],["o",false],["0",false]];
```

🟠 **行 29，列 138** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 29 行第 138 列

**代码**:
```sqf
_buttonsCombinations = [["@",false],["1",false],["^",true],["~",false],[")",true],["]",false],["(",true],["[",false],["|",false],["\",false],["/",false],["?",true],["3",true],["%",true],["*",true],["L",true],["8",true],["5",false],[";",false],["A",false],["a",true],["g",true],["G",false],["b",false],["B",true],["p",false],["P",false],["w",false],["W",false],["m",true],["n",false],["N",true],["M",false],["t",true],["T",false],["`",true],[":",false],["o",false],["0",false]];
```

🟠 **行 30，列 5** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 29 行第 138 列）

**代码**:
```sqf
};
```

🟠 **行 31，列 1** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 29 行第 32 列）

**代码**:
```sqf
};
```

---

### addons\mcc_sandbox_mod\mcc\helpers\fnc\fn_helpersInit.sqf

**总行数**: 129
**问题数**: 15

#### ❌ 未闭合的括号

🔴 **行 6，列 106** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (player == player && !( isDedicated) && !(missionNamespace getVariable ["MCC_isLocalHC",false])) then {
```

🔴 **行 7，列 10** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
0 spawn {
```

🔴 **行 34，列 11** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
0 spawn {
```

🔴 **行 57，列 11** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
0 spawn {
```

🔴 **行 76，列 9** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
0 spawn {
```

#### ❌ 括号类型不匹配

🟠 **行 42，列 15** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 42 行第 15 列

**代码**:
```sqf
_answer = ["<t font='TahomaB'>You have just been assigned as Engineer/EOD</t>
```

🟠 **行 53，列 4** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 42 行第 15 列）

**代码**:
```sqf
};
```

🟠 **行 60，列 15** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 60 行第 15 列

**代码**:
```sqf
_answer = ["<img size='10' img image=" + format ["'%1mcc\helpers\data\commanderRTS.paa'", MCC_path] + " align='center'/>
```

🟠 **行 72，列 4** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 60 行第 15 列）

**代码**:
```sqf
};
```

🟠 **行 79，列 15** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 79 行第 15 列

**代码**:
```sqf
_answer = ["<img size='10' img image=" + format ["'%1mcc\helpers\data\sqlPic.paa'", MCC_path] + "align='center'/>
```

🟠 **行 89，列 4** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 79 行第 15 列）

**代码**:
```sqf
};
```

🟠 **行 96，列 15** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 96 行第 15 列

**代码**:
```sqf
_answer = ["<img size='9' img image=" + format ["'%1mcc\helpers\data\PRlogistics.paa'", MCC_path] + " align='center'/>
```

🟠 **行 107，列 4** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 96 行第 15 列）

**代码**:
```sqf
};
```

🟠 **行 114，列 15** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 114 行第 15 列

**代码**:
```sqf
_answer = ["<img size='9' img image=" + format ["'%1mcc\helpers\data\logisticsHeli.paa'", MCC_path] + " align='center'/>
```

🟠 **行 125，列 4** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 114 行第 15 列）

**代码**:
```sqf
};
```

---

### addons\mcc_sandbox_mod\mcc\general_scripts\evac\evac_move.sqf

**总行数**: 359
**问题数**: 11

#### ❌ 未闭合的括号

🔴 **行 42，列 1** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
{
```

🔴 **行 77，列 2** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
{
```

🔴 **行 94，列 3** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
{
```

🔴 **行 151，列 3** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
{
```

🔴 **行 338，列 2** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
{
```

#### ❌ 括号类型不匹配

🟠 **行 107，列 9** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 107 行第 9 列

**代码**:
```sqf
[compile format ["unassignVehicle objectFromNetID '%1'; objectFromNetID '%1' action ['eject', vehicle objectFromNetID '%1']", netID _unit] remoteExec ["BIS_fnc_spawn", _unit, false];
```

🟠 **行 108，列 7** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 107 行第 9 列）

**代码**:
```sqf
}
```

🟠 **行 288，列 9** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 288 行第 9 列

**代码**:
```sqf
[compile format ["objectFromNetID '%1' switchmove '';", netID _unit] remoteExec ["BIS_fnc_spawn", 0, false];
```

🟠 **行 289，列 7** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 288 行第 9 列）

**代码**:
```sqf
}
```

🟠 **行 357，列 1** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 357 行第 1 列

**代码**:
```sqf
[[_startPos, _height, 1, [netid _heli,_heli]] remoteExec ["MCC_fnc_evacMove", _heli, false];
```

🟠 **行 358，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 357 行第 1 列）

**代码**:
```sqf
};
```

---

### addons\mcc_sandbox_mod\mcc\pop_menu\spawn_group.sqf

**总行数**: 327
**问题数**: 10

#### ❌ 未闭合的括号

🔴 **行 16，列 1** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
{
```

🔴 **行 22，列 2** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
{
```

🔴 **行 24，列 3** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
{
```

🔴 **行 48，列 3** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
{
```

#### ❌ 括号类型不匹配

🟠 **行 33，列 25** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 33 行第 25 列

**代码**:
```sqf
hint parseText format["<br/>--------------------------<br/>
```

🟠 **行 44，列 3** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 33 行第 25 列）

**代码**:
```sqf
};
```

🟠 **行 105，列 1** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 105 行第 1 列

**代码**:
```sqf
[[_center,_radius,_action,_intanse,_faction,mcc_sidename] remoteExec ["MCC_fnc_garrison", 0, false];
```

🟠 **行 106，列 1** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 106 行第 1 列

**代码**:
```sqf
[[_center,_radius,_action,_intanse,_faction,mcc_sidename] remoteExec ["MCC_fnc_garrison", 0, false];
```

🟠 **行 107，列 3** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 106 行第 1 列）

**代码**:
```sqf
};
```

🟠 **行 130，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 105 行第 1 列）

**代码**:
```sqf
};
```

---

### addons\mcc_sandbox_mod\mcc\general_scripts\convoy\make_convoy_WP.sqf

**总行数**: 201
**问题数**: 7

#### ❌ 未闭合的括号

🔴 **行 9，列 26** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (!mcc_isloading) then {
```

🔴 **行 10，列 46** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (mcc_missionmaker == (name player)) then {
```

🔴 **行 34，列 24** (方括号)

**问题**: 未闭合的括号 '['（期望 ']'）

**代码**:
```sqf
hint parseText format["Add waypoints for convoy:<br/>--------------------------<br/>
```

#### ❌ 括号类型不匹配

🟠 **行 56，列 24** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 56 行第 24 列

**代码**:
```sqf
hint parseText format["Add waypoints for convoy:<br/>--------------------------<br/>
```

🟠 **行 100，列 24** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 100 行第 24 列

**代码**:
```sqf
hint parseText format["Add waypoints for convoy:<br/>--------------------------<br/>
```

🟠 **行 200，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 100 行第 24 列）

**代码**:
```sqf
} else { player globalchat "Access Denied"};
```

🟠 **行 201，列 1** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 56 行第 24 列）

**代码**:
```sqf
};
```

---

### addons\mcc_sandbox_mod\mcc\LHD\fnc\fn_LHDspawnMenuInit.sqf

**总行数**: 320
**问题数**: 7

#### ❌ 未闭合的括号

🔴 **行 245，列 1** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
{
```

#### ❌ 括号类型不匹配

🟠 **行 251，列 27** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 251 行第 27 列

**代码**:
```sqf
_ctrl ctrlAddEventHandler ['MouseButtonUp',format [
```

🟠 **行 251，列 51** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 251 行第 51 列

**代码**:
```sqf
_ctrl ctrlAddEventHandler ['MouseButtonUp',format [
```

🟠 **行 258，列 1** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 251 行第 51 列）

**代码**:
```sqf
} forEach _decks;
```

🟠 **行 262，列 2** (花括号)

**问题**: 括号类型不匹配: 开括号 '{' 在第 262 行第 2 列

**代码**:
```sqf
{
```

🟠 **行 268，列 151** (花括号)

**问题**: 括号类型不匹配: 期望 '}'，但找到 ']'（开括号在第 262 行第 2 列）

**代码**:
```sqf
_ctrl ctrlAddEventHandler ['MouseButtonUp',format ["closeDialog 0;[%1, %2, %3] spawn MCC_fnc_LHDspawnMenuInit;"] ,0,(_availableLHD find _x),_operator]];
```

🟠 **行 276，列 1** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 251 行第 27 列）

**代码**:
```sqf
};
```

---

### addons\mcc_sandbox_mod\mcc\rts\scripts\mcc_logisticsBaseBuild.sqf

**总行数**: 1306
**问题数**: 6

#### ❌ 未匹配的闭括号

🟡 **行 1099，列 2** (花括号)

**问题**: 未匹配的闭括号 '}'

**代码**:
```sqf
};
```

🟡 **行 1264，列 1** (花括号)

**问题**: 未匹配的闭括号 '}'

**代码**:
```sqf
};
```

#### ❌ 括号类型不匹配

🟠 **行 1053，列 48** (花括号)

**问题**: 括号类型不匹配: 开括号 '{' 在第 1053 行第 48 列

**代码**:
```sqf
if (vehicle leader _x == leader _x) then {
```

🟠 **行 1063，列 18** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 1063 行第 18 列

**代码**:
```sqf
_string = format ["{
```

🟠 **行 1074，列 1** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 1063 行第 18 列）

**代码**:
```sqf
} forEach %1;",_buildingPos];
```

🟠 **行 1085，列 13** (花括号)

**问题**: 括号类型不匹配: 期望 '}'，但找到 ']'（开括号在第 1053 行第 48 列）

**代码**:
```sqf
} forEach %1];
```

---

### addons\mcc_sandbox_mod\sampleMissions\MCC_campaign.Altis\init.sqf

**总行数**: 121
**问题数**: 6

#### ❌ 未闭合的括号

🔴 **行 71，列 40** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (!isDedicated && hasInterface) then {
```

🔴 **行 91，列 67** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (profileNamespace getVariable ["MCC_FCtutorialPR",true]) then {
```

#### ❌ 括号类型不匹配

🟠 **行 92，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 92 行第 13 列

**代码**:
```sqf
_answer = ["<img size='10' img image='\mcc_sandbox_mod\mcc\helpers\data\PRmap.paa' align='center'/>
```

🟠 **行 106，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 92 行第 13 列）

**代码**:
```sqf
};
```

🟠 **行 111，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 111 行第 13 列

**代码**:
```sqf
_answer = ["<img size='8.7' img image='\mcc_sandbox_mod\mcc\helpers\data\PRkeyboardLayout.paa' />
```

🟠 **行 120，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 111 行第 13 列）

**代码**:
```sqf
};
```

---

### addons\mcc_sandbox_mod\sampleMissions\MCC_campaign.Tanoa\init.sqf

**总行数**: 119
**问题数**: 6

#### ❌ 未闭合的括号

🔴 **行 71，列 40** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (!isDedicated && hasInterface) then {
```

🔴 **行 89，列 67** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (profileNamespace getVariable ["MCC_FCtutorialPR",true]) then {
```

#### ❌ 括号类型不匹配

🟠 **行 90，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 90 行第 13 列

**代码**:
```sqf
_answer = ["<img size='10' img image='\mcc_sandbox_mod\mcc\helpers\data\PRmap.paa' align='center'/>
```

🟠 **行 104，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 90 行第 13 列）

**代码**:
```sqf
};
```

🟠 **行 109，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 109 行第 13 列

**代码**:
```sqf
_answer = ["<img size='8.7' img image='\mcc_sandbox_mod\mcc\helpers\data\PRkeyboardLayout.paa' />
```

🟠 **行 118，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 109 行第 13 列）

**代码**:
```sqf
};
```

---

### addons\mcc_sandbox_mod\sampleMissions\MCC_campaign_BAF.abel\init.sqf

**总行数**: 118
**问题数**: 6

#### ❌ 未闭合的括号

🔴 **行 71，列 40** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (!isDedicated && hasInterface) then {
```

🔴 **行 88，列 67** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (profileNamespace getVariable ["MCC_FCtutorialPR",true]) then {
```

#### ❌ 括号类型不匹配

🟠 **行 89，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 89 行第 13 列

**代码**:
```sqf
_answer = ["<img size='10' img image='\mcc_sandbox_mod\mcc\helpers\data\PRmap.paa' align='center'/>
```

🟠 **行 103，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 89 行第 13 列）

**代码**:
```sqf
};
```

🟠 **行 108，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 108 行第 13 列

**代码**:
```sqf
_answer = ["<img size='8.7' img image='\mcc_sandbox_mod\mcc\helpers\data\PRkeyboardLayout.paa' />
```

🟠 **行 117，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 108 行第 13 列）

**代码**:
```sqf
};
```

---

### addons\mcc_sandbox_mod\sampleMissions\MCC_campaign_BAF.Malden\init.sqf

**总行数**: 118
**问题数**: 6

#### ❌ 未闭合的括号

🔴 **行 71，列 40** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (!isDedicated && hasInterface) then {
```

🔴 **行 88，列 67** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (profileNamespace getVariable ["MCC_FCtutorialPR",true]) then {
```

#### ❌ 括号类型不匹配

🟠 **行 89，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 89 行第 13 列

**代码**:
```sqf
_answer = ["<img size='10' img image='\mcc_sandbox_mod\mcc\helpers\data\PRmap.paa' align='center'/>
```

🟠 **行 103，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 89 行第 13 列）

**代码**:
```sqf
};
```

🟠 **行 108，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 108 行第 13 列

**代码**:
```sqf
_answer = ["<img size='8.7' img image='\mcc_sandbox_mod\mcc\helpers\data\PRkeyboardLayout.paa' />
```

🟠 **行 117，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 108 行第 13 列）

**代码**:
```sqf
};
```

---

### addons\mcc_sandbox_mod\sampleMissions\MCC_campaign_BAF.noe\init.sqf

**总行数**: 118
**问题数**: 6

#### ❌ 未闭合的括号

🔴 **行 71，列 40** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (!isDedicated && hasInterface) then {
```

🔴 **行 88，列 67** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (profileNamespace getVariable ["MCC_FCtutorialPR",true]) then {
```

#### ❌ 括号类型不匹配

🟠 **行 89，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 89 行第 13 列

**代码**:
```sqf
_answer = ["<img size='10' img image='\mcc_sandbox_mod\mcc\helpers\data\PRmap.paa' align='center'/>
```

🟠 **行 103，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 89 行第 13 列）

**代码**:
```sqf
};
```

🟠 **行 108，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 108 行第 13 列

**代码**:
```sqf
_answer = ["<img size='8.7' img image='\mcc_sandbox_mod\mcc\helpers\data\PRkeyboardLayout.paa' />
```

🟠 **行 117，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 108 行第 13 列）

**代码**:
```sqf
};
```

---

### addons\mcc_sandbox_mod\sampleMissions\MCC_campaign_CSAT.Altis\init.sqf

**总行数**: 118
**问题数**: 6

#### ❌ 未闭合的括号

🔴 **行 71，列 40** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (!isDedicated && hasInterface) then {
```

🔴 **行 88，列 67** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (profileNamespace getVariable ["MCC_FCtutorialPR",true]) then {
```

#### ❌ 括号类型不匹配

🟠 **行 89，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 89 行第 13 列

**代码**:
```sqf
_answer = ["<img size='10' img image='\mcc_sandbox_mod\mcc\helpers\data\PRmap.paa' align='center'/>
```

🟠 **行 103，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 89 行第 13 列）

**代码**:
```sqf
};
```

🟠 **行 108，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 108 行第 13 列

**代码**:
```sqf
_answer = ["<img size='8.7' img image='\mcc_sandbox_mod\mcc\helpers\data\PRkeyboardLayout.paa' />
```

🟠 **行 117，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 108 行第 13 列）

**代码**:
```sqf
};
```

---

### addons\mcc_sandbox_mod\sampleMissions\MCC_campaign_CSAT.Tanoa\init.sqf

**总行数**: 118
**问题数**: 6

#### ❌ 未闭合的括号

🔴 **行 71，列 40** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (!isDedicated && hasInterface) then {
```

🔴 **行 88，列 67** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (profileNamespace getVariable ["MCC_FCtutorialPR",true]) then {
```

#### ❌ 括号类型不匹配

🟠 **行 89，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 89 行第 13 列

**代码**:
```sqf
_answer = ["<img size='10' img image='\mcc_sandbox_mod\mcc\helpers\data\PRmap.paa' align='center'/>
```

🟠 **行 103，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 89 行第 13 列）

**代码**:
```sqf
};
```

🟠 **行 108，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 108 行第 13 列

**代码**:
```sqf
_answer = ["<img size='8.7' img image='\mcc_sandbox_mod\mcc\helpers\data\PRkeyboardLayout.paa' />
```

🟠 **行 117，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 108 行第 13 列）

**代码**:
```sqf
};
```

---

### addons\mcc_sandbox_mod\sampleMissions\MCC_campaign_GU.Chernarus\init.sqf

**总行数**: 118
**问题数**: 6

#### ❌ 未闭合的括号

🔴 **行 71，列 40** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (!isDedicated && hasInterface) then {
```

🔴 **行 88，列 67** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (profileNamespace getVariable ["MCC_FCtutorialPR",true]) then {
```

#### ❌ 括号类型不匹配

🟠 **行 89，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 89 行第 13 列

**代码**:
```sqf
_answer = ["<img size='10' img image='\mcc_sandbox_mod\mcc\helpers\data\PRmap.paa' align='center'/>
```

🟠 **行 103，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 89 行第 13 列）

**代码**:
```sqf
};
```

🟠 **行 108，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 108 行第 13 列

**代码**:
```sqf
_answer = ["<img size='8.7' img image='\mcc_sandbox_mod\mcc\helpers\data\PRkeyboardLayout.paa' />
```

🟠 **行 117，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 108 行第 13 列）

**代码**:
```sqf
};
```

---

### addons\mcc_sandbox_mod\sampleMissions\MCC_campaign_GU.Chernarus_Summer\init.sqf

**总行数**: 118
**问题数**: 6

#### ❌ 未闭合的括号

🔴 **行 71，列 40** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (!isDedicated && hasInterface) then {
```

🔴 **行 88，列 67** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (profileNamespace getVariable ["MCC_FCtutorialPR",true]) then {
```

#### ❌ 括号类型不匹配

🟠 **行 89，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 89 行第 13 列

**代码**:
```sqf
_answer = ["<img size='10' img image='\mcc_sandbox_mod\mcc\helpers\data\PRmap.paa' align='center'/>
```

🟠 **行 103，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 89 行第 13 列）

**代码**:
```sqf
};
```

🟠 **行 108，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 108 行第 13 列

**代码**:
```sqf
_answer = ["<img size='8.7' img image='\mcc_sandbox_mod\mcc\helpers\data\PRkeyboardLayout.paa' />
```

🟠 **行 117，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 108 行第 13 列）

**代码**:
```sqf
};
```

---

### addons\mcc_sandbox_mod\sampleMissions\MCC_campaign_GU.Chernarus_Winter\init.sqf

**总行数**: 118
**问题数**: 6

#### ❌ 未闭合的括号

🔴 **行 71，列 40** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (!isDedicated && hasInterface) then {
```

🔴 **行 88，列 67** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (profileNamespace getVariable ["MCC_FCtutorialPR",true]) then {
```

#### ❌ 括号类型不匹配

🟠 **行 89，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 89 行第 13 列

**代码**:
```sqf
_answer = ["<img size='10' img image='\mcc_sandbox_mod\mcc\helpers\data\PRmap.paa' align='center'/>
```

🟠 **行 103，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 89 行第 13 列）

**代码**:
```sqf
};
```

🟠 **行 108，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 108 行第 13 列

**代码**:
```sqf
_answer = ["<img size='8.7' img image='\mcc_sandbox_mod\mcc\helpers\data\PRkeyboardLayout.paa' />
```

🟠 **行 117，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 108 行第 13 列）

**代码**:
```sqf
};
```

---

### addons\mcc_sandbox_mod\sampleMissions\MCC_campaign_GU.noe\init.sqf

**总行数**: 118
**问题数**: 6

#### ❌ 未闭合的括号

🔴 **行 71，列 40** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (!isDedicated && hasInterface) then {
```

🔴 **行 88，列 67** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (profileNamespace getVariable ["MCC_FCtutorialPR",true]) then {
```

#### ❌ 括号类型不匹配

🟠 **行 89，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 89 行第 13 列

**代码**:
```sqf
_answer = ["<img size='10' img image='\mcc_sandbox_mod\mcc\helpers\data\PRmap.paa' align='center'/>
```

🟠 **行 103，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 89 行第 13 列）

**代码**:
```sqf
};
```

🟠 **行 108，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 108 行第 13 列

**代码**:
```sqf
_answer = ["<img size='8.7' img image='\mcc_sandbox_mod\mcc\helpers\data\PRkeyboardLayout.paa' />
```

🟠 **行 117，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 108 行第 13 列）

**代码**:
```sqf
};
```

---

### addons\mcc_sandbox_mod\sampleMissions\MCC_campaign_GU.Sara_dbe1\init.sqf

**总行数**: 118
**问题数**: 6

#### ❌ 未闭合的括号

🔴 **行 71，列 40** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (!isDedicated && hasInterface) then {
```

🔴 **行 88，列 67** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (profileNamespace getVariable ["MCC_FCtutorialPR",true]) then {
```

#### ❌ 括号类型不匹配

🟠 **行 89，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 89 行第 13 列

**代码**:
```sqf
_answer = ["<img size='10' img image='\mcc_sandbox_mod\mcc\helpers\data\PRmap.paa' align='center'/>
```

🟠 **行 103，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 89 行第 13 列）

**代码**:
```sqf
};
```

🟠 **行 108，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 108 行第 13 列

**代码**:
```sqf
_answer = ["<img size='8.7' img image='\mcc_sandbox_mod\mcc\helpers\data\PRkeyboardLayout.paa' />
```

🟠 **行 117，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 108 行第 13 列）

**代码**:
```sqf
};
```

---

### addons\mcc_sandbox_mod\sampleMissions\MCC_campaign_GU.Takistan\init.sqf

**总行数**: 118
**问题数**: 6

#### ❌ 未闭合的括号

🔴 **行 71，列 40** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (!isDedicated && hasInterface) then {
```

🔴 **行 88，列 67** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (profileNamespace getVariable ["MCC_FCtutorialPR",true]) then {
```

#### ❌ 括号类型不匹配

🟠 **行 89，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 89 行第 13 列

**代码**:
```sqf
_answer = ["<img size='10' img image='\mcc_sandbox_mod\mcc\helpers\data\PRmap.paa' align='center'/>
```

🟠 **行 103，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 89 行第 13 列）

**代码**:
```sqf
};
```

🟠 **行 108，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 108 行第 13 列

**代码**:
```sqf
_answer = ["<img size='8.7' img image='\mcc_sandbox_mod\mcc\helpers\data\PRkeyboardLayout.paa' />
```

🟠 **行 117，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 108 行第 13 列）

**代码**:
```sqf
};
```

---

### addons\mcc_sandbox_mod\sampleMissions\MCC_campaign_RHS.Altis\init.sqf

**总行数**: 118
**问题数**: 6

#### ❌ 未闭合的括号

🔴 **行 71，列 40** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (!isDedicated && hasInterface) then {
```

🔴 **行 88，列 67** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (profileNamespace getVariable ["MCC_FCtutorialPR",true]) then {
```

#### ❌ 括号类型不匹配

🟠 **行 89，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 89 行第 13 列

**代码**:
```sqf
_answer = ["<img size='10' img image='\mcc_sandbox_mod\mcc\helpers\data\PRmap.paa' align='center'/>
```

🟠 **行 103，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 89 行第 13 列）

**代码**:
```sqf
};
```

🟠 **行 108，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 108 行第 13 列

**代码**:
```sqf
_answer = ["<img size='8.7' img image='\mcc_sandbox_mod\mcc\helpers\data\PRkeyboardLayout.paa' />
```

🟠 **行 117，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 108 行第 13 列）

**代码**:
```sqf
};
```

---

### addons\mcc_sandbox_mod\sampleMissions\MCC_campaign_RHS_GRU.Altis\init.sqf

**总行数**: 118
**问题数**: 6

#### ❌ 未闭合的括号

🔴 **行 71，列 40** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (!isDedicated && hasInterface) then {
```

🔴 **行 88，列 67** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (profileNamespace getVariable ["MCC_FCtutorialPR",true]) then {
```

#### ❌ 括号类型不匹配

🟠 **行 89，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 89 行第 13 列

**代码**:
```sqf
_answer = ["<img size='10' img image='\mcc_sandbox_mod\mcc\helpers\data\PRmap.paa' align='center'/>
```

🟠 **行 103，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 89 行第 13 列）

**代码**:
```sqf
};
```

🟠 **行 108，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 108 行第 13 列

**代码**:
```sqf
_answer = ["<img size='8.7' img image='\mcc_sandbox_mod\mcc\helpers\data\PRkeyboardLayout.paa' />
```

🟠 **行 117，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 108 行第 13 列）

**代码**:
```sqf
};
```

---

### addons\mcc_sandbox_mod\sampleMissions\MCC_campaign_RHS_RU.Altis\init.sqf

**总行数**: 118
**问题数**: 6

#### ❌ 未闭合的括号

🔴 **行 71，列 40** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (!isDedicated && hasInterface) then {
```

🔴 **行 88，列 67** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (profileNamespace getVariable ["MCC_FCtutorialPR",true]) then {
```

#### ❌ 括号类型不匹配

🟠 **行 89，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 89 行第 13 列

**代码**:
```sqf
_answer = ["<img size='10' img image='\mcc_sandbox_mod\mcc\helpers\data\PRmap.paa' align='center'/>
```

🟠 **行 103，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 89 行第 13 列）

**代码**:
```sqf
};
```

🟠 **行 108，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 108 行第 13 列

**代码**:
```sqf
_answer = ["<img size='8.7' img image='\mcc_sandbox_mod\mcc\helpers\data\PRkeyboardLayout.paa' />
```

🟠 **行 117，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 108 行第 13 列）

**代码**:
```sqf
};
```

---

### addons\mcc_sandbox_mod\sampleMissions\MCC_campaign_RU.Chernarus\init.sqf

**总行数**: 118
**问题数**: 6

#### ❌ 未闭合的括号

🔴 **行 71，列 40** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (!isDedicated && hasInterface) then {
```

🔴 **行 88，列 67** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (profileNamespace getVariable ["MCC_FCtutorialPR",true]) then {
```

#### ❌ 括号类型不匹配

🟠 **行 89，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 89 行第 13 列

**代码**:
```sqf
_answer = ["<img size='10' img image='\mcc_sandbox_mod\mcc\helpers\data\PRmap.paa' align='center'/>
```

🟠 **行 103，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 89 行第 13 列）

**代码**:
```sqf
};
```

🟠 **行 108，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 108 行第 13 列

**代码**:
```sqf
_answer = ["<img size='8.7' img image='\mcc_sandbox_mod\mcc\helpers\data\PRkeyboardLayout.paa' />
```

🟠 **行 117，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 108 行第 13 列）

**代码**:
```sqf
};
```

---

### addons\mcc_sandbox_mod\sampleMissions\MCC_campaign_RU.Chernarus_Summer\init.sqf

**总行数**: 118
**问题数**: 6

#### ❌ 未闭合的括号

🔴 **行 71，列 40** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (!isDedicated && hasInterface) then {
```

🔴 **行 88，列 67** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (profileNamespace getVariable ["MCC_FCtutorialPR",true]) then {
```

#### ❌ 括号类型不匹配

🟠 **行 89，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 89 行第 13 列

**代码**:
```sqf
_answer = ["<img size='10' img image='\mcc_sandbox_mod\mcc\helpers\data\PRmap.paa' align='center'/>
```

🟠 **行 103，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 89 行第 13 列）

**代码**:
```sqf
};
```

🟠 **行 108，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 108 行第 13 列

**代码**:
```sqf
_answer = ["<img size='8.7' img image='\mcc_sandbox_mod\mcc\helpers\data\PRkeyboardLayout.paa' />
```

🟠 **行 117，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 108 行第 13 列）

**代码**:
```sqf
};
```

---

### addons\mcc_sandbox_mod\sampleMissions\MCC_campaign_RU.Chernarus_Winter\init.sqf

**总行数**: 118
**问题数**: 6

#### ❌ 未闭合的括号

🔴 **行 71，列 40** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (!isDedicated && hasInterface) then {
```

🔴 **行 88，列 67** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (profileNamespace getVariable ["MCC_FCtutorialPR",true]) then {
```

#### ❌ 括号类型不匹配

🟠 **行 89，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 89 行第 13 列

**代码**:
```sqf
_answer = ["<img size='10' img image='\mcc_sandbox_mod\mcc\helpers\data\PRmap.paa' align='center'/>
```

🟠 **行 103，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 89 行第 13 列）

**代码**:
```sqf
};
```

🟠 **行 108，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 108 行第 13 列

**代码**:
```sqf
_answer = ["<img size='8.7' img image='\mcc_sandbox_mod\mcc\helpers\data\PRkeyboardLayout.paa' />
```

🟠 **行 117，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 108 行第 13 列）

**代码**:
```sqf
};
```

---

### addons\mcc_sandbox_mod\sampleMissions\MCC_campaign_RU.noe\init.sqf

**总行数**: 118
**问题数**: 6

#### ❌ 未闭合的括号

🔴 **行 71，列 40** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (!isDedicated && hasInterface) then {
```

🔴 **行 88，列 67** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (profileNamespace getVariable ["MCC_FCtutorialPR",true]) then {
```

#### ❌ 括号类型不匹配

🟠 **行 89，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 89 行第 13 列

**代码**:
```sqf
_answer = ["<img size='10' img image='\mcc_sandbox_mod\mcc\helpers\data\PRmap.paa' align='center'/>
```

🟠 **行 103，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 89 行第 13 列）

**代码**:
```sqf
};
```

🟠 **行 108，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 108 行第 13 列

**代码**:
```sqf
_answer = ["<img size='8.7' img image='\mcc_sandbox_mod\mcc\helpers\data\PRkeyboardLayout.paa' />
```

🟠 **行 117，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 108 行第 13 列）

**代码**:
```sqf
};
```

---

### addons\mcc_sandbox_mod\sampleMissions\MCC_campaign_RU.Sara_dbe1\init.sqf

**总行数**: 118
**问题数**: 6

#### ❌ 未闭合的括号

🔴 **行 71，列 40** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (!isDedicated && hasInterface) then {
```

🔴 **行 88，列 67** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (profileNamespace getVariable ["MCC_FCtutorialPR",true]) then {
```

#### ❌ 括号类型不匹配

🟠 **行 89，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 89 行第 13 列

**代码**:
```sqf
_answer = ["<img size='10' img image='\mcc_sandbox_mod\mcc\helpers\data\PRmap.paa' align='center'/>
```

🟠 **行 103，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 89 行第 13 列）

**代码**:
```sqf
};
```

🟠 **行 108，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 108 行第 13 列

**代码**:
```sqf
_answer = ["<img size='8.7' img image='\mcc_sandbox_mod\mcc\helpers\data\PRkeyboardLayout.paa' />
```

🟠 **行 117，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 108 行第 13 列）

**代码**:
```sqf
};
```

---

### addons\mcc_sandbox_mod\sampleMissions\MCC_campaign_TK.Takistan\init.sqf

**总行数**: 118
**问题数**: 6

#### ❌ 未闭合的括号

🔴 **行 71，列 40** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (!isDedicated && hasInterface) then {
```

🔴 **行 88，列 67** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (profileNamespace getVariable ["MCC_FCtutorialPR",true]) then {
```

#### ❌ 括号类型不匹配

🟠 **行 89，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 89 行第 13 列

**代码**:
```sqf
_answer = ["<img size='10' img image='\mcc_sandbox_mod\mcc\helpers\data\PRmap.paa' align='center'/>
```

🟠 **行 103，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 89 行第 13 列）

**代码**:
```sqf
};
```

🟠 **行 108，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 108 行第 13 列

**代码**:
```sqf
_answer = ["<img size='8.7' img image='\mcc_sandbox_mod\mcc\helpers\data\PRkeyboardLayout.paa' />
```

🟠 **行 117，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 108 行第 13 列）

**代码**:
```sqf
};
```

---

### addons\mcc_sandbox_mod\sampleMissions\MCC_campaign_USA.Chernarus_Summer\init.sqf

**总行数**: 118
**问题数**: 6

#### ❌ 未闭合的括号

🔴 **行 71，列 40** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (!isDedicated && hasInterface) then {
```

🔴 **行 88，列 67** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (profileNamespace getVariable ["MCC_FCtutorialPR",true]) then {
```

#### ❌ 括号类型不匹配

🟠 **行 89，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 89 行第 13 列

**代码**:
```sqf
_answer = ["<img size='10' img image='\mcc_sandbox_mod\mcc\helpers\data\PRmap.paa' align='center'/>
```

🟠 **行 103，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 89 行第 13 列）

**代码**:
```sqf
};
```

🟠 **行 108，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 108 行第 13 列

**代码**:
```sqf
_answer = ["<img size='8.7' img image='\mcc_sandbox_mod\mcc\helpers\data\PRkeyboardLayout.paa' />
```

🟠 **行 117，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 108 行第 13 列）

**代码**:
```sqf
};
```

---

### addons\mcc_sandbox_mod\sampleMissions\MCC_campaign_USA.Chernarus_Winter\init.sqf

**总行数**: 118
**问题数**: 6

#### ❌ 未闭合的括号

🔴 **行 71，列 40** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (!isDedicated && hasInterface) then {
```

🔴 **行 88，列 67** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (profileNamespace getVariable ["MCC_FCtutorialPR",true]) then {
```

#### ❌ 括号类型不匹配

🟠 **行 89，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 89 行第 13 列

**代码**:
```sqf
_answer = ["<img size='10' img image='\mcc_sandbox_mod\mcc\helpers\data\PRmap.paa' align='center'/>
```

🟠 **行 103，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 89 行第 13 列）

**代码**:
```sqf
};
```

🟠 **行 108，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 108 行第 13 列

**代码**:
```sqf
_answer = ["<img size='8.7' img image='\mcc_sandbox_mod\mcc\helpers\data\PRkeyboardLayout.paa' />
```

🟠 **行 117，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 108 行第 13 列）

**代码**:
```sqf
};
```

---

### addons\mcc_sandbox_mod\sampleMissions\MCC_campaign_USA.Takistan\init.sqf

**总行数**: 118
**问题数**: 6

#### ❌ 未闭合的括号

🔴 **行 71，列 40** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (!isDedicated && hasInterface) then {
```

🔴 **行 88，列 67** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (profileNamespace getVariable ["MCC_FCtutorialPR",true]) then {
```

#### ❌ 括号类型不匹配

🟠 **行 89，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 89 行第 13 列

**代码**:
```sqf
_answer = ["<img size='10' img image='\mcc_sandbox_mod\mcc\helpers\data\PRmap.paa' align='center'/>
```

🟠 **行 103，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 89 行第 13 列）

**代码**:
```sqf
};
```

🟠 **行 108，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 108 行第 13 列

**代码**:
```sqf
_answer = ["<img size='8.7' img image='\mcc_sandbox_mod\mcc\helpers\data\PRkeyboardLayout.paa' />
```

🟠 **行 117，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 108 行第 13 列）

**代码**:
```sqf
};
```

---

### addons\mcc_sandbox_mod\sampleMissions\MCC_campaign_USMC.Chernarus\init.sqf

**总行数**: 118
**问题数**: 6

#### ❌ 未闭合的括号

🔴 **行 71，列 40** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (!isDedicated && hasInterface) then {
```

🔴 **行 88，列 67** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (profileNamespace getVariable ["MCC_FCtutorialPR",true]) then {
```

#### ❌ 括号类型不匹配

🟠 **行 89，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 89 行第 13 列

**代码**:
```sqf
_answer = ["<img size='10' img image='\mcc_sandbox_mod\mcc\helpers\data\PRmap.paa' align='center'/>
```

🟠 **行 103，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 89 行第 13 列）

**代码**:
```sqf
};
```

🟠 **行 108，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 108 行第 13 列

**代码**:
```sqf
_answer = ["<img size='8.7' img image='\mcc_sandbox_mod\mcc\helpers\data\PRkeyboardLayout.paa' />
```

🟠 **行 117，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 108 行第 13 列）

**代码**:
```sqf
};
```

---

### addons\mcc_sandbox_mod\sampleMissions\MCC_campaign_USMC.Sara_dbe1\init.sqf

**总行数**: 118
**问题数**: 6

#### ❌ 未闭合的括号

🔴 **行 71，列 40** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (!isDedicated && hasInterface) then {
```

🔴 **行 88，列 67** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (profileNamespace getVariable ["MCC_FCtutorialPR",true]) then {
```

#### ❌ 括号类型不匹配

🟠 **行 89，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 89 行第 13 列

**代码**:
```sqf
_answer = ["<img size='10' img image='\mcc_sandbox_mod\mcc\helpers\data\PRmap.paa' align='center'/>
```

🟠 **行 103，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 89 行第 13 列）

**代码**:
```sqf
};
```

🟠 **行 108，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 108 行第 13 列

**代码**:
```sqf
_answer = ["<img size='8.7' img image='\mcc_sandbox_mod\mcc\helpers\data\PRkeyboardLayout.paa' />
```

🟠 **行 117，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 108 行第 13 列）

**代码**:
```sqf
};
```

---

### addons\mcc_sandbox_mod\mcc\roleSelection\scripts\respawnPanel_init.sqf

**总行数**: 456
**问题数**: 5

#### ❌ 未闭合的括号

🔴 **行 222，列 10** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
[] spawn {
```

#### ❌ 括号类型不匹配

🟠 **行 421，列 52** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 421 行第 52 列

**代码**:
```sqf
(_disp displayCtrl _idc) ctrlAddEventHandler ["LBSelChanged",format ["if ((_this select 1) > -1) then {
```

🟠 **行 421，列 75** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 421 行第 75 列

**代码**:
```sqf
(_disp displayCtrl _idc) ctrlAddEventHandler ["LBSelChanged",format ["if ((_this select 1) > -1) then {
```

🟠 **行 424，列 23** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 421 行第 75 列）

**代码**:
```sqf
}",ctrlIDC _ctrlGroup]];
```

🟠 **行 425，列 6** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 421 行第 52 列）

**代码**:
```sqf
} else {
```

---

### addons\mcc_sandbox_mod\mcc\ai\fnc\fn_doHaltAI.sqf

**总行数**: 112
**问题数**: 4

#### ❌ 未闭合的括号

🔴 **行 51，列 18** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (_shout) then {
```

🔴 **行 55，列 1** (方括号)

**问题**: 未闭合的括号 '['（期望 ']'）

**代码**:
```sqf
[[[_target, _unit],
```

#### ❌ 括号类型不匹配

🟠 **行 55，列 2** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 55 行第 2 列

**代码**:
```sqf
[[[_target, _unit],
```

🟠 **行 66，列 1** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 55 行第 2 列）

**代码**:
```sqf
};
```

---

### addons\mcc_sandbox_mod\mcc\dialogs\mcc_boxGen_change.sqf

**总行数**: 215
**问题数**: 3

#### ❌ 未闭合的括号

🔴 **行 192，列 2** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
{
```

#### ❌ 括号类型不匹配

🟠 **行 206，列 34** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 206 行第 34 列

**代码**:
```sqf
mcc_safe = mcc_safe + FORMAT ["[%1, %2, %3, %4, %5, %6] remoteExec [""MCC_fnc_boxGenerator"", 0, false];
```

🟠 **行 210，列 4** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 206 行第 34 列）

**代码**:
```sqf
};
```

---

### addons\mcc_sandbox_mod\mcc\fnc\evac\fn_evacMove.sqf

**总行数**: 322
**问题数**: 3

#### ❌ 未闭合的括号

🔴 **行 54，列 1** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
{
```

#### ❌ 括号类型不匹配

🟠 **行 118，列 9** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 118 行第 9 列

**代码**:
```sqf
[compile format ["unassignVehicle objectFromNetID '%1'; objectFromNetID '%1' action ['eject', vehicle objectFromNetID '%1']", netID _unit] remoteExec ["BIS_fnc_spawn", _unit, false];
```

🟠 **行 119，列 7** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 118 行第 9 列）

**代码**:
```sqf
}
```

---

### addons\mcc_sandbox_mod\mcc\general_scripts\groupGen\spawn_request.sqf

**总行数**: 267
**问题数**: 3

#### ❌ 未闭合的括号

🔴 **行 29，列 1** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
{
```

#### ❌ 括号类型不匹配

🟠 **行 46，列 24** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 46 行第 24 列

**代码**:
```sqf
hint parseText format["<br/>--------------------------<br/>
```

🟠 **行 57，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 46 行第 24 列）

**代码**:
```sqf
};
```

---

### addons\mcc_sandbox_mod\mcc\general_scripts\triggers\triggers.sqf

**总行数**: 85
**问题数**: 3

#### ❌ 未闭合的括号

🔴 **行 20，列 1** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
{
```

#### ❌ 括号类型不匹配

🟠 **行 72，列 28** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 72 行第 28 列

**代码**:
```sqf
onMapSingleClick  format[" 	hint 'Trigger moved.';
```

🟠 **行 75，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 72 行第 28 列）

**代码**:
```sqf
};
```

---

### addons\mcc_sandbox_mod\mcc\general_scripts\unitManage\um.sqf

**总行数**: 484
**问题数**: 3

#### ❌ 未闭合的括号

🔴 **行 15，列 19** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
switch (_type) do {
```

#### ❌ 括号类型不匹配

🟠 **行 27，列 5** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 27 行第 5 列

**代码**:
```sqf
[[[netID _x,_x],teleportPos] remoteExec ["MCC_fnc_moveToPos", _x, false];
```

🟠 **行 28，列 4** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 27 行第 5 列）

**代码**:
```sqf
} foreach MCC_selectedUnits;
```

---

### addons\mcc_sandbox_mod\mcc\pop_menu\mcc_make_array_weapons.sqf

**总行数**: 108
**问题数**: 3

#### ❌ 未匹配的闭括号

🟡 **行 108，列 2** (花括号)

**问题**: 未匹配的闭括号 '}'

**代码**:
```sqf
};
```

#### ❌ 括号类型不匹配

🟠 **行 102，列 9** (花括号)

**问题**: 括号类型不匹配: 开括号 '{' 在第 102 行第 9 列

**代码**:
```sqf
default {
```

🟠 **行 103，列 66** (花括号)

**问题**: 括号类型不匹配: 期望 '}'，但找到 ']'（开括号在第 102 行第 9 列）

**代码**:
```sqf
U_EXPLOSIVE set [count U_EPLOSIVE, [_weaponDisplayName,_picture]]];
```

---

### addons\mcc_sandbox_mod\sampleMissions\PvPmine.Tanoa\init.sqf

**总行数**: 54
**问题数**: 3

#### ❌ 未闭合的括号

🔴 **行 30，列 40** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (!isDedicated && hasInterface) then {
```

#### ❌ 括号类型不匹配

🟠 **行 44，列 13** (方括号)

**问题**: 括号类型不匹配: 开括号 '[' 在第 44 行第 13 列

**代码**:
```sqf
_answer = ["<img size='10' img image='PRmap.paa' align='center'/>
```

🟠 **行 53，列 2** (方括号)

**问题**: 括号类型不匹配: 期望 ']'，但找到 '}'（开括号在第 44 行第 13 列）

**代码**:
```sqf
};
```

---

### addons\mcc_sandbox_mod\gaia\gaia_init.sqf

**总行数**: 112
**问题数**: 2

#### ❌ 未闭合的括号

🔴 **行 8，列 24** (方括号)

**问题**: 未闭合的括号 '['（期望 ']'）

**代码**:
```sqf
GAIA_scripts 	= format ["%1gaia\scripts\",MCC_path];
```

🔴 **行 9，列 21** (方括号)

**问题**: 未闭合的括号 '['（期望 ']'）

**代码**:
```sqf
GAIA_fsm 		= format ["%1gaia\fsm\",MCC_path];
```

---

### addons\mcc_sandbox_mod\mcc\interaction\fnc\fn_interactObject.sqf

**总行数**: 163
**问题数**: 2

#### ❌ 未闭合的括号

🔴 **行 10，列 263** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if ((player distance _object < 7) && ((missionNamespace getVariable ["MCC_interactionKey_holding",false]) || (MCC_isACE && MCC_isMode)) && !(missionNameSpace getVariable [format ["MCC_isInteracted%1",getpos _object], false]) && (isNull attachedTo _object)) then {
```

🔴 **行 69，列 35** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
if (!isnil "_typeOfobject") then {
```

---

### addons\mcc_sandbox_mod\mcc\fnc\general\fn_handleAddaction.sqf

**总行数**: 150
**问题数**: 1

#### ❌ 未匹配的闭括号

🟡 **行 150，列 1** (花括号)

**问题**: 未匹配的闭括号 '}'

**代码**:
```sqf
};
```

---

### addons\mcc_sandbox_mod\mcc\fnc\general\fn_keyToName.sqf

**总行数**: 101
**问题数**: 1

#### ❌ 未闭合的括号

🔴 **行 14，列 30** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
_text = switch (_dikCode) do {
```

---

### addons\mcc_sandbox_mod\mcc\fnc\general\fn_pickItem.sqf

**总行数**: 65
**问题数**: 1

#### ❌ 未闭合的括号

🔴 **行 16，列 27** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
_path = if (_isMode) then {"\mcc_sandbox_mod\"} else {""};
```

---

### addons\mcc_sandbox_mod\mcc\fnc\ied\fn_manageAC.sqf

**总行数**: 140
**问题数**: 1

#### ❌ 未闭合的括号

🔴 **行 64，列 37** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
while {alive _suspect && _check} do {
```

---

### addons\mcc_sandbox_mod\mcc\fnc\ied\fn_mineSingle.sqf

**总行数**: 105
**问题数**: 1

#### ❌ 未闭合的括号

🔴 **行 3，列 2** (方括号)

**问题**: 未闭合的括号 '['（期望 ']'）

**代码**:
```sqf
[["IEDkind","IEDMarkerName",centerPos,minefieldSize] remoteExec ["MCC_fnc_mineSingle",0,false];
```

---

### addons\mcc_sandbox_mod\mcc\general_scripts\delete\undo.sqf

**总行数**: 31
**问题数**: 1

#### ❌ 未闭合的括号

🔴 **行 11，列 1** (方括号)

**问题**: 未闭合的括号 '['（期望 ']'）

**代码**:
```sqf
[[2, {
```

---

### addons\mcc_sandbox_mod\mcc\general_scripts\unitManage\hc_server.sqf

**总行数**: 90
**问题数**: 1

#### ❌ 未闭合的括号

🔴 **行 6，列 2** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
{
```

---

### addons\mcc_sandbox_mod\mcc\UI\fnc\fn_camp_showOSD.sqf

**总行数**: 216
**问题数**: 1

#### ❌ 未闭合的括号

🔴 **行 8，列 46** (圆括号)

**问题**: 未闭合的括号 '('（期望 ')'）

**代码**:
```sqf
_this select 0: array (optional)	- position (default: player's position)
```

---

### addons\mcc_sandbox_mod\mcc\UI\fnc\fn_initCuratorAttribute.sqf

**总行数**: 36
**问题数**: 1

#### ❌ 未闭合的括号

🔴 **行 4，列 1** (花括号)

**问题**: 未闭合的括号 '{'（期望 '}'）

**代码**:
```sqf
{
```

---

