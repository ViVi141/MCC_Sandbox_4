# Arma 3 语法检查工具（使用 LM Studio）

## 📋 功能说明

此工具使用 LM Studio 的本地 LLM 模型对项目中的每个 Arma 3 文件进行语法检查，确保代码符合 Arma 3 SQF 语法规范。

### 主要功能

- ✅ **自动扫描**：自动扫描项目中的所有 Arma 3 相关文件（.sqf, .hpp, .cpp 等）
- ✅ **语法检查**：使用 LM Studio 的 LLM 模型进行深度语法分析
- ✅ **问题定位**：精确定位语法错误的位置（行号、列号）
- ✅ **修复建议**：提供具体的修复建议
- ✅ **并发处理**：支持多线程并发检查，提高效率
- ✅ **详细报告**：生成 Markdown 格式的详细检查报告

## 🚀 使用前准备

### 1. 安装依赖

```bash
pip install requests
```

### 2. 启动 LM Studio

1. 打开 LM Studio
2. 加载模型（推荐：`qwen/qwen3-vl-8b` 或类似模型）
3. 启动本地服务器（默认端口：1234）
4. 确保 API 服务器正在运行

### 3. 验证 LM Studio 连接

```bash
# 测试 API 连接
curl http://localhost:1234/v1/models
```

## 📖 使用方法

### 基本使用

```bash
# 检查整个项目
python check_arma3_syntax_with_lmstudio.py

# 指定项目根目录
python check_arma3_syntax_with_lmstudio.py --root addons/mcc_sandbox_mod

# 指定输出文件
python check_arma3_syntax_with_lmstudio.py --output my_report.md
```

### 命令行参数

```bash
python check_arma3_syntax_with_lmstudio.py [选项]

选项:
  --root ROOT          项目根目录（默认: addons/mcc_sandbox_mod）
  --output OUTPUT      输出报告文件（默认: arma3_syntax_check_report.md）
  --max-workers N      并发检查线程数（默认: 3）
  --limit N            限制检查的文件数量（用于测试）
  --extensions EXT     要检查的文件扩展名（默认: .sqf .hpp）
```

### 使用示例

#### 示例 1: 检查所有文件

```bash
# 检查整个项目，使用 5 个并发线程
python check_arma3_syntax_with_lmstudio.py --max-workers 5
```

#### 示例 2: 只检查 SQF 文件

```bash
# 只检查 .sqf 文件
python check_arma3_syntax_with_lmstudio.py --extensions .sqf
```

#### 示例 3: 测试模式（限制文件数量）

```bash
# 只检查前 10 个文件（用于测试）
python check_arma3_syntax_with_lmstudio.py --limit 10
```

#### 示例 4: 串行检查（单线程）

```bash
# 使用单线程串行检查（适合调试）
python check_arma3_syntax_with_lmstudio.py --max-workers 1
```

## 📊 报告格式

报告包含以下信息：

### 统计信息

- 总文件数
- 已检查文件数
- 通过检查的文件数
- 发现错误的文件数
- 检查出错的文件数

### 详细结果

每个有问题的文件都会显示：

1. **文件路径**
2. **检查状态**：passed / failed / error
3. **问题列表**：
   - 行号和列号
   - 严重程度（error / warning / info）
   - 问题描述
   - 相关代码片段
   - 修复建议

### 报告示例

```markdown
# Arma 3 语法检查报告

生成时间: 2025-01-18 10:30:00

## 统计信息

- **总文件数**: 150
- **已检查**: 150
- **通过**: 145
- **失败**: 3
- **错误**: 2

## 详细结果

### ❌ 语法错误文件 (3)

### addons/mcc_sandbox_mod/mcc/fnc/test.sqf

**状态**: failed

**总行数**: 50
**已检查行数**: 50
**检查时间**: 2.35秒

**问题数**: 2

**问题列表**:

🔴 **行 15** (列 10): 未闭合的括号

```sqf
if (condition) then {
    // 代码
```

💡 **建议**: 在第 20 行添加闭合括号 `}`

🔴 **行 25**: remoteExec 调用格式错误

```sqf
[params] remoteExec ["function", true, false];
```

💡 **建议**: 第二个参数应该是数字 0 或 2，而不是布尔值 true
```

## 🔍 检查内容

工具会检查以下方面：

### 1. 基本语法错误

- ✅ 括号匹配（圆括号、方括号、花括号）
- ✅ 引号匹配（单引号、双引号）
- ✅ 分号和逗号使用
- ✅ 基本语法结构

### 2. SQF 语法规范

- ✅ 变量声明和使用
- ✅ 函数调用语法
- ✅ 数组和哈希表语法
- ✅ 控制流语句（if/else, switch, while, for）
- ✅ 操作符使用

### 3. Arma 3 特定语法

- ✅ `remoteExec` 调用格式
- ✅ `BIS_fnc_*` 函数调用
- ✅ 配置类语法（CfgPatches, CfgFunctions 等）
- ✅ 事件处理器语法

### 4. 常见错误

- ✅ 未闭合的括号或引号
- ✅ 错误的数组语法
- ✅ 函数参数不匹配
- ✅ 变量作用域问题

## ⚙️ 配置说明

### LM Studio API 配置

默认配置（针对 AMD Radeon RX 7900 XT 优化）：
- **API URL**: `http://localhost:1234/v1/chat/completions`
- **模型**: `qwen/qwen2.5-coder-14b`
- **超时时间**: 180 秒
- **最大上下文长度**: 6000 tokens（输出）- 保守设置以确保稳定性
- **最大输入长度**: 16000 tokens（输入）- 充分利用 20GB VRAM
- **最大文件行数**: 3500 行（单次检查）
- **分片重叠**: 150 行（避免在分片边界遗漏问题）
- **分片处理**: 已启用（自动处理大文件）

如需修改，编辑脚本中的配置：

```python
LM_STUDIO_API_URL = "http://localhost:1234/v1/chat/completions"
MODEL_NAME = "qwen/qwen2.5-coder-14b"
MAX_CONTEXT_TOKENS = 6000   # 最大输出 tokens
MAX_INPUT_TOKENS = 16000    # 最大输入 tokens
MAX_FILE_LINES = 3500       # 单次检查的最大行数
CHUNK_OVERLAP = 150         # 分片重叠行数
ENABLE_CHUNKING = True      # 是否启用分片处理
```

### 文件过滤

默认排除：
- `.git` 目录
- `node_modules` 目录
- `.bak`, `.orig`, `.tmp`, `.log` 文件

默认检查的文件类型：
- `.sqf` - SQF 脚本文件
- `.hpp` - 头文件
- `.cpp` - C++ 配置文件
- `.h` - C 头文件
- `.ext` - 扩展文件
- `config.cpp` - 配置文件
- `description.ext` - 描述文件
- `stringtable.xml` - 字符串表

## 🎯 最佳实践

### 1. 首次运行

建议先用测试模式运行：

```bash
# 只检查前 5 个文件
python check_arma3_syntax_with_lmstudio.py --limit 5
```

### 2. 大项目检查

对于大型项目，建议：

```bash
# 使用更多并发线程
python check_arma3_syntax_with_lmstudio.py --max-workers 5

# 或者分批检查
python check_arma3_syntax_with_lmstudio.py --extensions .sqf --output sqf_report.md
python check_arma3_syntax_with_lmstudio.py --extensions .hpp --output hpp_report.md
```

### 3. 持续集成

可以将此工具集成到 CI/CD 流程中：

```bash
# 检查并返回退出码
python check_arma3_syntax_with_lmstudio.py
if [ $? -ne 0 ]; then
    echo "语法检查失败"
    exit 1
fi
```

## ⚠️ 注意事项

### 1. LM Studio 必须运行

确保 LM Studio 服务器正在运行，否则会报错：

```
API 错误: Connection refused
```

### 2. 大文件处理（分片功能）

对于超过 3500 行的文件，工具会自动进行分片处理：
- 文件会被分成多个片段（每个片段最多 3500 行）
- 片段之间有 150 行的重叠区域，避免在边界处遗漏问题
- 每个片段独立检查，然后合并结果
- 自动去重，确保同一问题不会重复报告

例如：一个 10000 行的文件会被分成 3 个片段：
- 片段 1: 行 1-3500
- 片段 2: 行 3351-6850（与片段1重叠150行）
- 片段 3: 行 6701-10000（与片段2重叠150行）

这样可以确保整个文件都被检查，不会遗漏任何问题。

### 3. API 超时

如果文件很大或模型响应慢，可能会超时。可以：

- 增加超时时间（修改脚本中的 `timeout` 参数）
- 减少并发线程数
- 分批检查文件

### 4. 模型选择

当前使用模型：
- **`qwen/qwen2.5-coder-14b`** - 推荐，专门用于代码分析，支持 32K tokens 上下文

其他推荐模型：
- `Qwen/Qwen2.5-Coder-7B-Instruct` - 更轻量级的选择
- `deepseek-coder-6.7b-instruct` - 代码专用模型

### 5. 性能考虑

- **并发线程数**：建议 3-5 个，过多可能导致 API 过载
- **检查时间**：每个文件大约需要 2-5 秒（取决于模型和文件大小）
- **总时间**：100 个文件大约需要 5-10 分钟

## 🔧 故障排除

### 问题 1: 无法连接到 LM Studio

**错误**: `Connection refused` 或 `API 错误: 500`

**解决**:
1. 确认 LM Studio 正在运行
2. 检查端口是否正确（默认 1234）
3. 确认模型已加载

### 问题 2: API 超时

**错误**: `API 调用超时（180秒）`

**解决**:
1. 减少并发线程数：`--max-workers 1`
2. 检查大文件，考虑分批处理
3. 增加超时时间（修改脚本中的 `timeout` 参数）
4. 确保 LM Studio 有足够的 GPU 内存（14B 模型需要更多资源）

### 问题 3: JSON 解析错误

**错误**: `JSON 解析失败`

**解决**:
1. 检查模型输出格式
2. 尝试使用不同的模型
3. 查看 `llm_response` 字段了解原始响应

### 问题 4: 内存不足

**错误**: 系统内存不足

**解决**:
1. 减少并发线程数
2. 分批检查文件（使用 `--limit`）
3. 关闭其他占用内存的程序

## 📝 示例工作流

### 完整的代码审查流程

```bash
# 1. 检查语法
python check_arma3_syntax_with_lmstudio.py

# 2. 查看报告
cat arma3_syntax_check_report.md

# 3. 修复问题
# 根据报告中的建议修复语法错误

# 4. 重新检查
python check_arma3_syntax_with_lmstudio.py

# 5. 提交代码
git add .
git commit -m "修复语法错误"
```

### 与 Git 集成

```bash
# 在提交前检查语法
python check_arma3_syntax_with_lmstudio.py --output pre_commit_check.md
if grep -q "失败" pre_commit_check.md; then
    echo "发现语法错误，请修复后再提交"
    exit 1
fi
```

## 🎓 高级用法

### 自定义检查规则

可以修改脚本中的 `_build_prompt` 方法来添加自定义检查规则：

```python
def _build_prompt(self, file_path: Path, content: str) -> str:
    prompt = f"""请检查以下 Arma 3 文件...
    
    自定义检查项：
    - 检查是否使用了过时的 BIS_fnc_MP
    - 检查 remoteExec 调用格式
    - 检查变量命名规范
    ...
    """
    return prompt
```

### 集成到 IDE

可以将此工具集成到 VS Code 或其他 IDE 中：

1. 创建任务配置文件（`.vscode/tasks.json`）
2. 添加快捷键绑定
3. 设置自动检查

---

**最后更新**: 2025-01-18  
**版本**: 1.0.0

