# 括号嵌套检查工具

## 📋 功能说明

此工具用于检查项目中所有代码文件的括号嵌套是否正确，支持：

- ✅ **圆括号** `()` - 函数调用、表达式
- ✅ **方括号** `[]` - 数组、索引访问
- ✅ **花括号** `{}` - 代码块、哈希表

### 主要功能

- 自动扫描项目中的所有代码文件
- 智能识别字符串和注释中的括号（不计算）
- 精确定位括号错误的位置（行号、列号）
- 区分三种类型的错误：
  - 未闭合的括号
  - 未匹配的闭括号
  - 括号类型不匹配
- 生成详细的 Markdown 报告

## 🚀 使用方法

### 基本使用

```bash
# 检查整个项目
python check_brackets.py

# 指定项目根目录
python check_brackets.py --root addons/mcc_sandbox_mod

# 指定输出文件
python check_brackets.py --output my_report.md
```

### 命令行参数

```bash
python check_brackets.py [选项]

选项:
  --root ROOT          项目根目录（默认: addons/mcc_sandbox_mod）
  --output OUTPUT      输出报告文件（默认: bracket_check_report.md）
  --extensions EXT     要检查的文件扩展名（默认: .sqf .hpp）
  --limit N            限制检查的文件数量（用于测试）
```

### 使用示例

#### 示例 1: 检查所有文件

```bash
# 检查整个项目
python check_brackets.py
```

#### 示例 2: 只检查 SQF 文件

```bash
# 只检查 .sqf 文件
python check_brackets.py --extensions .sqf
```

#### 示例 3: 测试模式（限制文件数量）

```bash
# 只检查前 10 个文件（用于测试）
python check_brackets.py --limit 10
```

#### 示例 4: 检查特定文件类型

```bash
# 检查 .sqf 和 .hpp 文件
python check_brackets.py --extensions .sqf .hpp
```

## 📊 报告格式

报告包含以下信息：

### 统计信息

- 总文件数
- 有问题的文件数
- 总问题数

### 详细结果

每个有问题的文件都会显示：

1. **文件路径**
2. **总行数**
3. **问题列表**（按类型分组）：
   - ❌ 未闭合的括号
   - ❌ 未匹配的闭括号
   - ❌ 括号类型不匹配

每个问题包含：
- 行号和列号
- 括号类型（圆括号/方括号/花括号）
- 问题描述
- 相关代码片段

### 报告示例

```markdown
# 括号嵌套检查报告

生成时间: 2025-01-18 10:30:00

## 统计信息

- **总文件数**: 150
- **有问题的文件**: 3
- **总问题数**: 5

## 详细结果

### addons/mcc_sandbox_mod/example.sqf

**总行数**: 50
**问题数**: 2

#### ❌ 未闭合的括号

🔴 **行 15，列 10** (圆括号)

**问题**: 未闭合的括号 '('（期望 ')'）

**代码**:
```sqf
if (condition) then {
    // 代码
```

🔴 **行 25，列 5** (方括号)

**问题**: 未闭合的括号 '['（期望 ']'）

**代码**:
```sqf
_array = [1, 2, 3
```
```

## 🔍 检查内容

工具会检查以下括号类型：

### 1. 圆括号 `()`

用于：
- 函数调用：`call function()`
- 表达式：`(a + b) * c`
- 条件语句：`if (condition) then`

### 2. 方括号 `[]`

用于：
- 数组：`[1, 2, 3]`
- 数组访问：`_array select 0`
- 参数传递：`[param1, param2]`

### 3. 花括号 `{}`

用于：
- 代码块：`{ code }`
- 哈希表：`createHashMapFromArray [...]`
- 配置类：`class MyClass { ... }`

## ⚙️ 工作原理

### 1. 字符串处理

工具会智能识别字符串中的括号，不会将它们计入括号匹配：

```sqf
_text = "This is a (string) with brackets";  // 括号不会被检查
```

### 2. 注释处理

注释中的括号也不会被检查：

```sqf
// This is a comment with (brackets)  // 括号不会被检查
```

### 3. 括号匹配算法

使用栈（Stack）数据结构来跟踪括号：
- 遇到开括号时入栈
- 遇到闭括号时出栈并检查是否匹配
- 文件结束时检查栈中是否还有未闭合的括号

## ⚠️ 注意事项

### 1. 字符串中的括号

工具会正确识别字符串，但复杂的字符串转义可能需要手动检查：

```sqf
_text = "He said \"Hello (world)\"";  // 正确识别
```

### 2. 多行字符串

SQF 不支持多行字符串，所以每行独立处理。

### 3. 宏定义

`#define` 宏定义中的括号会被检查，这可能导致误报：

```sqf
#define MACRO(x) (x * 2)  // 会被检查，但这是宏定义
```

### 4. 预处理器指令

`#include`、`#define` 等预处理器指令中的括号也会被检查。

## 🎯 最佳实践

### 1. 首次运行

建议先用测试模式运行：

```bash
# 只检查前 5 个文件
python check_brackets.py --limit 5
```

### 2. 修复问题

根据报告中的问题，逐一修复：

1. 查看问题描述和代码片段
2. 定位到具体行号和列号
3. 修复括号问题
4. 重新运行检查

### 3. 持续集成

可以将此工具集成到 CI/CD 流程中：

```bash
# 检查并返回退出码
python check_brackets.py
if [ $? -ne 0 ]; then
    echo "括号检查失败"
    exit 1
fi
```

## 🔧 故障排除

### 问题 1: 误报

**可能原因**:
- 字符串处理逻辑问题
- 宏定义中的括号
- 预处理器指令

**解决**:
- 手动检查报告中的问题
- 查看代码上下文
- 确认是否真的是错误

### 问题 2: 编码问题

**错误**: `UnicodeDecodeError`

**解决**:
- 脚本会自动尝试多种编码
- 如果仍有问题，检查文件编码

### 问题 3: 性能问题

**可能原因**: 文件太多或太大

**解决**:
- 使用 `--limit` 参数分批检查
- 使用 `--extensions` 只检查特定文件类型

## 📝 示例工作流

### 完整的代码审查流程

```bash
# 1. 检查括号
python check_brackets.py

# 2. 查看报告
cat bracket_check_report.md

# 3. 修复问题
# 根据报告中的建议修复括号问题

# 4. 重新检查
python check_brackets.py

# 5. 提交代码
git add .
git commit -m "修复括号嵌套问题"
```

### 与 Git 集成

```bash
# 在提交前检查括号
python check_brackets.py --output pre_commit_check.md
if grep -q "有问题的文件" pre_commit_check.md; then
    echo "发现括号问题，请修复后再提交"
    exit 1
fi
```

## 🎓 高级用法

### 自定义文件类型

```bash
# 只检查特定文件类型
python check_brackets.py --extensions .sqf .hpp .cpp
```

### 批量检查

```bash
# 检查所有文件并生成报告
python check_brackets.py --output full_report.md
```

---

**最后更新**: 2025-01-18  
**版本**: 1.0.0

