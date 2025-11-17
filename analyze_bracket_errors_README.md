# 括号错误分析和修复工具（使用 LM Studio）

## 功能说明

此工具使用 LM Studio 的本地 LLM 模型（qwen/qwen2.5-coder-14b）分析括号检查报告中的错误，并生成格式化的修复建议。

### 主要功能

- ✅ **智能分析**：使用 LM Studio 的 LLM 模型分析每个括号错误
- ✅ **误报识别**：自动识别脚本误报（如字符串中的括号）
- ✅ **修复建议**：为真实错误提供具体的修复建议
- ✅ **自动修复**：可选择自动应用修复（默认：仅生成报告）
- ✅ **详细报告**：生成 Markdown 格式的详细修复报告

## 使用前准备

### 1. 安装依赖

```bash
pip install requests
```

### 2. 启动 LM Studio

1. 打开 LM Studio
2. 加载模型：`qwen/qwen2.5-coder-14b`
3. 启动本地服务器（默认端口：1234）
4. 确保 API 服务器正在运行

### 3. 验证 LM Studio 连接

```bash
# 测试 API 连接
curl http://localhost:1234/v1/models
```

## 使用方法

### 基本使用（仅生成报告，不应用修复）

```bash
python analyze_bracket_errors_with_lmstudio.py
```

### 应用修复

```bash
python analyze_bracket_errors_with_lmstudio.py --apply
```

### 命令行参数

```bash
python analyze_bracket_errors_with_lmstudio.py [选项]

选项:
  --report REPORT      括号检查报告文件（默认: bracket_check_report.md）
  --root ROOT          项目根目录（默认: addons/mcc_sandbox_mod）
  --output OUTPUT      输出报告文件（默认: bracket_fix_report.md）
  --apply              应用修复（默认: 仅生成报告）
  --limit N            限制处理的文件数量（用于测试）
  --max-workers N      并发处理线程数（默认: 2）
```

### 使用示例

#### 示例 1: 测试分析（仅处理前 2 个文件）

```bash
python analyze_bracket_errors_with_lmstudio.py --limit 2
```

#### 示例 2: 分析所有错误并应用修复

```bash
python analyze_bracket_errors_with_lmstudio.py --apply
```

#### 示例 3: 指定自定义报告文件

```bash
python analyze_bracket_errors_with_lmstudio.py --report my_report.md --output my_fix_report.md
```

## 工作流程

1. **解析报告**：读取 `bracket_check_report.md`，提取所有错误
2. **分析错误**：对每个错误调用 LM Studio API 进行分析
3. **生成建议**：为真实错误生成修复建议，识别误报
4. **应用修复**：如果使用 `--apply`，自动应用修复到文件
5. **生成报告**：生成详细的修复报告

## 输出说明

### 控制台输出

- `[1/60] 分析: file.sqf (16 个错误)` - 正在分析的文件
- `  [误报] file.sqf:23 - 这是误报，因为...` - 识别为误报的错误
- `  ✓ 修复 file.sqf:23` - 成功修复的错误
- `     原: 原始代码` - 修复前的代码
- `     新: 修复后的代码` - 修复后的代码

### 报告文件

生成的 `bracket_fix_report.md` 包含：
- 统计信息（总错误数、已修复、跳过、错误）
- 每个文件的详细修复建议
- 修复前后的代码对比
- 修复说明和置信度

## 注意事项

1. **误报识别**：脚本会自动识别误报（如字符串中的括号），这些不会生成修复建议
2. **试运行模式**：默认不应用修复，只生成报告，使用 `--apply` 才会真正修改文件
3. **API 超时**：如果 LM Studio 响应慢，可能需要增加超时时间（修改脚本中的 `TIMEOUT`）
4. **并发控制**：默认使用 2 个并发线程，避免 API 过载

## 配置说明

### AMD Radeon RX 7900 XT 优化配置

脚本已针对 AMD Radeon RX 7900 XT (20GB VRAM) 进行优化：

```python
MAX_CONTEXT_TOKENS = 8000      # 最大输出 tokens（充分利用 20GB VRAM）
MAX_INPUT_TOKENS = 20000       # 最大输入 tokens（代码+提示词）
TIMEOUT = 300                  # API 超时时间（大模型需要更长时间）
DEFAULT_MAX_WORKERS = 4        # 默认并发线程数（7900 XT 可以支持更高并发）
CONTEXT_LINES = 20             # 上下文行数（增加以提供更多上下文）
```

**优化特性**：
- ✅ **更大的上下文窗口**：8000 tokens 输出 / 20000 tokens 输入
- ✅ **更高并发**：默认 4 个并发线程（可调整）
- ✅ **更长超时**：300 秒，适合大模型处理
- ✅ **更多上下文**：20 行上下文，提供更准确的代码分析
- ✅ **并发处理**：同时处理多个文件和错误，充分利用 GPU

### 自定义配置

如需修改配置，编辑脚本中的以下变量：

```python
LM_STUDIO_API_URL = "http://localhost:1234/v1/chat/completions"
MODEL_NAME = "qwen/qwen2.5-coder-14b"
MAX_CONTEXT_TOKENS = 8000      # 最大输出 tokens
MAX_INPUT_TOKENS = 20000       # 最大输入 tokens
TIMEOUT = 300                  # API 超时时间（秒）
DEFAULT_MAX_WORKERS = 4        # 默认并发线程数
CONTEXT_LINES = 20             # 上下文行数
```

### 性能调优建议

**对于 7900 XT (20GB VRAM)**：
- 可以安全使用 4-6 个并发线程
- 可以处理更大的上下文（8000+ tokens）
- 建议保持默认配置以获得最佳性能

**对于较小显存的 GPU**：
- 减少 `MAX_WORKERS` 到 1-2
- 减少 `MAX_CONTEXT_TOKENS` 到 4000-6000
- 减少 `CONTEXT_LINES` 到 10-15

## 故障排除

### 问题：API 连接失败

**解决方案**：
1. 确保 LM Studio 正在运行
2. 检查端口是否为 1234
3. 验证模型是否已加载

### 问题：解析 JSON 失败

**解决方案**：
- 这通常是因为 LLM 返回的 JSON 格式不正确
- 脚本会自动跳过这些错误并继续处理

### 问题：文件路径错误

**解决方案**：
- 确保项目根目录路径正确
- 检查报告中的文件路径格式

