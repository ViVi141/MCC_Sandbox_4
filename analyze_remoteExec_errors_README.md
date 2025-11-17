# remoteExec 使用检查工具

使用 LM Studio 的 `qwen/qwen2.5-coder-14b` 模型检查所有 `remoteExec` 的使用，发现并修复常见错误。

## 功能

检查以下常见问题：

1. **null 检查缺失**: 在使用 `netId` 或对象作为 `remoteExec` 参数前，是否检查了对象是否为 null
2. **netId 使用错误**: `netId` 的使用是否正确，特别是在单机模式下应该返回空字符串
3. **语法错误**: `remoteExec` 的语法是否正确，括号是否匹配
4. **对象有效性**: 传递给 `remoteExec` 的对象是否可能为 null 或无效

## 安装要求

1. **Python 3.7+**
2. **LM Studio** 运行在 `http://localhost:1234`
3. **qwen/qwen2.5-coder-14b** 模型已加载到 LM Studio

## 使用方法

### 基本用法（试运行，不修改文件）

```bash
python analyze_remoteExec_errors_with_lmstudio.py
```

### 限制处理文件数量（用于测试）

```bash
python analyze_remoteExec_errors_with_lmstudio.py --limit 5
```

### 应用修复（实际修改文件）

```bash
python analyze_remoteExec_errors_with_lmstudio.py --apply
```

### 自定义配置

```bash
python analyze_remoteExec_errors_with_lmstudio.py \
    --root addons/mcc_sandbox_mod \
    --output my_report.md \
    --max-workers 4 \
    --apply
```

## 参数说明

- `--root`: 项目根目录（默认: `addons/mcc_sandbox_mod`）
- `--output`: 输出报告文件（默认: `remoteExec_fix_report.md`）
- `--apply`: 应用修复（默认: 仅生成报告，不修改文件）
- `--limit`: 限制处理的文件数量（用于测试）
- `--max-workers`: 并发处理线程数（默认: 4，针对 AMD Radeon RX 7900 XT 优化）

## AMD Radeon RX 7900 XT 优化

脚本已针对 AMD Radeon RX 7900 XT (20GB VRAM) 进行优化：

- **最大上下文**: 8000 tokens（输出）/ 20000 tokens（输入）
- **并发线程数**: 4（可调整）
- **API 超时**: 300 秒
- **上下文行数**: 30 行（remoteExec 需要更多上下文）

## 检查的问题类型

### 1. null_check
缺少 null 检查，可能导致运行时错误。

**错误示例**:
```sqf
[[netId _unit, _unit], ...] remoteExec ["function", _unit, false];
```

**修复后**:
```sqf
if (!(isNull _unit)) then {
    [[if (isMultiplayer) then {netId _unit} else {""}, _unit], ...] remoteExec ["function", _unit, false];
};
```

### 2. netid_usage
`netId` 使用不正确，特别是在单机模式下。

**错误示例**:
```sqf
[[netId _target, _target], ...] remoteExec ["function", _target, false];
```

**修复后**:
```sqf
[[if (isMultiplayer) then {netId _target} else {""}, _target], ...] remoteExec ["function", _target, false];
```

### 3. syntax_error
`remoteExec` 语法错误，括号不匹配等。

### 4. other
其他问题。

## 输出报告

报告包含：

1. **统计信息**: 总问题数、已修复、跳过、错误
2. **问题分类**: 按问题类型分组统计
3. **详细修复建议**: 每个问题的原始代码、修复后代码、说明和置信度

## 示例输出

```
============================================================
remoteExec 使用检查工具
============================================================

项目根目录: addons/mcc_sandbox_mod
输出文件: remoteExec_fix_report.md
应用修复: 否（试运行）

[AMD Radeon RX 7900 XT 优化配置]
  最大上下文: 8000 tokens
  并发线程数: 4
  API 超时: 300 秒
  上下文行数: 30 行

扫描 remoteExec 使用...
扫描 246 个 .sqf 文件...
找到 246 个文件，共 1234 个 remoteExec 使用

分析 remoteExec 使用（使用 LM Studio，4 个并发线程）...
使用 4 个并发线程处理文件...
[1/246] ✓ mcc/fnc/general/fn_login.sqf: 2 个使用，0 个问题
[2/246] ✓ mcc/ai/fnc/fn_doHaltAI.sqf: 3 个使用，0 个问题
...

总共发现 45 个问题

报告已保存到: remoteExec_fix_report.md
```

## 注意事项

1. **试运行模式**: 默认不修改文件，只生成报告。使用 `--apply` 参数才会实际修改文件
2. **备份**: 在应用修复前，建议备份项目
3. **API 连接**: 确保 LM Studio 正在运行并监听 `localhost:1234`
4. **模型加载**: 确保 `qwen/qwen2.5-coder-14b` 模型已加载

## 常见问题

### Q: API 调用超时
A: 增加 `TIMEOUT` 值或减少 `--max-workers`

### Q: 找不到文件
A: 检查 `--root` 参数是否正确指向项目根目录

### Q: 修复建议不准确
A: 检查上下文行数是否足够，可以增加 `CONTEXT_LINES` 值

## 与括号检查工具的区别

- **括号检查工具** (`analyze_bracket_errors_with_lmstudio.py`): 检查括号匹配问题
- **remoteExec 检查工具** (本工具): 专门检查 `remoteExec` 的使用，关注 null 检查、netId 使用等特定问题

两个工具可以配合使用，全面检查代码质量。

