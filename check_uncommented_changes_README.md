# Git 未注释变更检查脚本

## 📋 功能说明

此脚本用于检查 Git 版本差异中，哪些代码行从**注释状态**变为**非注释状态**。这对于代码审查非常有用，可以检测到：

- 不应该被取消注释的代码
- 意外取消注释的示例代码
- 被错误激活的调试代码

## 🚀 使用方法

### 基本使用

```bash
# 检查工作区相对于 HEAD 的变更
python check_uncommented_changes.py

# 检查两个提交之间的差异
python check_uncommented_changes.py --base HEAD~1 --target HEAD

# 检查特定提交相对于另一个提交的差异
python check_uncommented_changes.py --base v2.0.0 --target v2.0.1
```

### 命令行参数

```bash
python check_uncommented_changes.py [选项]

选项:
  --base BASE        基准提交（默认: HEAD）
  --target TARGET    目标提交（默认: 工作区）
  --repo REPO        Git 仓库路径（默认: 当前目录）
  --output OUTPUT    输出报告文件（默认: uncommented_changes_report.md）
  --no-output-file   不保存报告文件，只输出到控制台
```

## 📊 使用示例

### 示例 1: 检查工作区变更

```bash
# 检查当前工作区相对于 HEAD 的变更
python check_uncommented_changes.py

# 输出:
# ============================================================
# 检查从注释状态变为非注释状态的代码行
# ============================================================
# 
# 比较: HEAD -> 工作区
# 
# 找到 3 处从注释变为非注释的变更
```

### 示例 2: 比较两个提交

```bash
# 比较两个提交之间的差异
python check_uncommented_changes.py --base abc123 --target def456

# 输出:
# 比较: abc123 -> def456
# 找到 5 处从注释变为非注释的变更
```

### 示例 3: 自定义输出文件

```bash
# 将报告保存到指定文件
python check_uncommented_changes.py --output my_report.md
```

### 示例 4: 只输出到控制台

```bash
# 不保存文件，只显示在控制台
python check_uncommented_changes.py --no-output-file
```

## 📄 报告格式

报告包含以下信息：

1. **统计信息**
   - 总变更数
   - 涉及文件数

2. **详细列表**（按文件分组）
   - 文件路径
   - 变更行号
   - 之前的代码（已注释）
   - 现在的代码（未注释）
   - 上下文代码

### 报告示例

```markdown
# 未注释变更检查报告

## 统计信息

- **总变更数**: 3
- **涉及文件数**: 2

## 详细列表

### addons/mcc_sandbox_mod/mcc/pv_handling/mcC_extras_pv_handler.sqf

**变更数**: 2

**行 16**:

**之前（已注释）**:
```
// [_commander, _action] remoteExec ["MCC_fnc_highCommand", 0, false];
```

**现在（未注释）**:
```
[_commander, _action] remoteExec ["MCC_fnc_highCommand", 0, false];
```

**上下文**:
```
    MCC_fnc_highCommand = {[(_this select 0), (_this select 1)] execVM MCC_path + "mcc\general_scripts\unitManage\hc_server.sqf"};
>>> [_commander, _action] remoteExec ["MCC_fnc_highCommand", 0, false];
// Params:
```

---
```

## 🔍 支持的文件类型

脚本自动识别以下文件类型的注释格式：

- **SQF 文件** (`.sqf`): `//` 注释
- **HPP 文件** (`.hpp`): `//` 注释
- **CPP 文件** (`.cpp`): `//` 注释
- **H 文件** (`.h`): `//` 注释
- **Python 文件** (`.py`): `#` 注释
- **JavaScript 文件** (`.js`): `//` 注释
- **TypeScript 文件** (`.ts`): `//` 注释

## ⚙️ 工作原理

1. **运行 Git Diff**: 使用 `git diff` 获取两个版本之间的差异
2. **解析差异**: 解析 diff 输出，识别添加和删除的行
3. **检测注释变更**: 
   - 检查删除的行是否被注释
   - 检查添加的行是否未注释
   - 比较内容相似度
4. **生成报告**: 列出所有从注释变为非注释的变更

## 🎯 使用场景

### 场景 1: 代码审查

在提交代码前，检查是否有不应该被取消注释的代码：

```bash
python check_uncommented_changes.py --base origin/main
```

### 场景 2: 版本对比

比较两个版本之间的变更：

```bash
python check_uncommented_changes.py --base v2.0.0 --target v2.0.1
```

### 场景 3: 检查特定文件

结合 Git 使用，只检查特定文件：

```bash
# 先查看哪些文件有变更
git diff --name-only HEAD

# 然后运行检查脚本
python check_uncommented_changes.py
```

## ⚠️ 注意事项

1. **相似度检测**: 脚本使用简单的相似度算法，可能会误报一些不相关的变更
2. **注释格式**: 只支持单行注释，不支持多行注释块
3. **Git 仓库**: 需要在 Git 仓库目录中运行

## 🔧 故障排除

### 问题 1: 找不到 Git 仓库

**错误**: `fatal: not a git repository`

**解决**: 确保在 Git 仓库根目录运行脚本，或使用 `--repo` 参数指定路径

### 问题 2: 没有检测到变更

**可能原因**:
- 工作区没有未提交的变更
- 指定的提交之间没有差异
- 没有从注释变为非注释的变更

**解决**: 使用 `git status` 和 `git diff` 确认有变更

### 问题 3: 误报

**可能原因**: 相似度检测算法可能将不相关的行识别为相关

**解决**: 手动审查报告，确认变更是否确实相关

## 📝 示例工作流

### 完整的代码审查流程

```bash
# 1. 检查工作区变更
python check_uncommented_changes.py

# 2. 查看报告
cat uncommented_changes_report.md

# 3. 如果有问题，检查具体文件
git diff addons/mcc_sandbox_mod/mcc/pv_handling/mcC_extras_pv_handler.sqf

# 4. 修复问题后重新检查
python check_uncommented_changes.py
```

## 🎓 高级用法

### 结合 Git Hooks

可以将此脚本添加到 Git pre-commit hook 中：

```bash
# .git/hooks/pre-commit
#!/bin/bash
python check_uncommented_changes.py --no-output-file
if [ $? -ne 0 ]; then
    echo "警告: 检测到从注释变为非注释的代码行"
    exit 1
fi
```

### 批量检查多个分支

```bash
# 检查所有分支相对于 main 的变更
for branch in $(git branch | grep -v main); do
    echo "检查分支: $branch"
    python check_uncommented_changes.py --base main --target $branch --output "report_${branch}.md"
done
```

---

**最后更新**: 2025-01-18  
**版本**: 1.0.0

