#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用 LM Studio 的 qwen/qwen2.5-coder-14b 检查所有 remoteExec 的使用
检查常见错误：
1. 对象为 null 时调用 netId
2. 缺少 isNull 检查
3. remoteExec 语法错误
4. netId 在单机模式下的使用
"""

import re
import json
import requests
from pathlib import Path
from typing import List, Dict, Optional
from dataclasses import dataclass
import argparse
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# ============================================================================
# 配置
# ============================================================================

LM_STUDIO_API_URL = "http://localhost:1234/v1/chat/completions"
MODEL_NAME = "qwen/qwen2.5-coder-14b"
PROJECT_ROOT = "addons/mcc_sandbox_mod"

# ============================================================================
# AMD Radeon RX 7900 XT (20GB VRAM) 优化配置
# ============================================================================
MAX_CONTEXT_TOKENS = 8000
MAX_INPUT_TOKENS = 20000
TIMEOUT = 300
DEFAULT_MAX_WORKERS = 4
CONTEXT_LINES = 30  # remoteExec 需要更多上下文

# ============================================================================
# 数据模型
# ============================================================================

@dataclass
class RemoteExecUsage:
    """remoteExec 使用位置"""
    file_path: str
    line: int
    column: int
    code_snippet: str
    full_line: str
    context_before: List[str]  # 之前的代码行
    context_after: List[str]    # 之后的代码行

@dataclass
class FileUsages:
    """文件的 remoteExec 使用集合"""
    file_path: str
    usages: List[RemoteExecUsage]

@dataclass
class FixSuggestion:
    """修复建议"""
    file_path: str
    line: int
    original_code: str
    fixed_code: str
    explanation: str
    confidence: float
    issue_type: str  # "null_check", "netid_usage", "syntax_error", "other"

# ============================================================================
# remoteExec 扫描器
# ============================================================================

class RemoteExecScanner:
    """扫描所有 remoteExec 使用"""
    
    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
    
    def scan_all_files(self) -> List[FileUsages]:
        """扫描所有文件中的 remoteExec 使用"""
        all_usages = []
        
        # 查找所有 .sqf 文件
        sqf_files = list(self.project_root.rglob("*.sqf"))
        print(f"扫描 {len(sqf_files)} 个 .sqf 文件...")
        
        for sqf_file in sqf_files:
            usages = self.scan_file(sqf_file)
            if usages:
                rel_path = str(sqf_file.relative_to(self.project_root))
                all_usages.append(FileUsages(
                    file_path=rel_path,
                    usages=usages
                ))
        
        return all_usages
    
    def scan_file(self, file_path: Path) -> List[RemoteExecUsage]:
        """扫描单个文件中的 remoteExec 使用"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
        except Exception as e:
            print(f"警告: 无法读取文件 {file_path}: {e}")
            return []
        
        usages = []
        
        for line_num, line in enumerate(lines, 1):
            # 查找 remoteExec 调用
            if 'remoteExec' in line:
                # 尝试找到完整的 remoteExec 调用（可能跨多行）
                full_call = self._extract_full_call(lines, line_num - 1)
                
                if full_call:
                    # 获取上下文
                    context_start = max(0, line_num - 1 - CONTEXT_LINES)
                    context_end = min(len(lines), line_num + CONTEXT_LINES)
                    context_before = [line.rstrip() for line in lines[context_start:line_num - 1]]
                    context_after = [line.rstrip() for line in lines[line_num:context_end]]
                    
                    # 计算列位置
                    column = line.find('remoteExec')
                    
                    usages.append(RemoteExecUsage(
                        file_path=str(file_path.relative_to(self.project_root)),
                        line=line_num,
                        column=column + 1,
                        code_snippet=full_call,
                        full_line=line.rstrip(),
                        context_before=context_before,
                        context_after=context_after
                    ))
        
        return usages
    
    def _extract_full_call(self, lines: List[str], start_line: int) -> Optional[str]:
        """提取完整的 remoteExec 调用（处理多行情况）"""
        if start_line >= len(lines):
            return None
        
        # 从当前行向前查找，找到调用的开始
        call_start = start_line
        bracket_count = 0
        found_remoteExec = False
        
        # 向前查找
        for i in range(start_line, -1, -1):
            if i >= len(lines):
                continue
            line = lines[i]
            if 'remoteExec' in line:
                found_remoteExec = True
                # 计算括号
                bracket_count += line.count('[') - line.count(']')
                call_start = i
                break
        
        if not found_remoteExec:
            return None
        
        # 向后查找，直到括号匹配
        call_lines = []
        for i in range(call_start, min(len(lines), call_start + 10)):
            line = lines[i]
            call_lines.append(line.rstrip())
            bracket_count += line.count('[') - line.count(']')
            if bracket_count <= 0 and 'remoteExec' in line:
                break
        
        return ' '.join(call_lines)

# ============================================================================
# LM Studio API 分析器
# ============================================================================

class LMStudioAnalyzer:
    """使用 LM Studio 分析 remoteExec 使用（支持 MCP 风格的交互）"""
    
    def __init__(self, api_url: str = LM_STUDIO_API_URL, model: str = MODEL_NAME, project_root: str = PROJECT_ROOT):
        self.api_url = api_url
        self.model = model
        self.timeout = TIMEOUT
        self.project_root = Path(project_root)
        self.max_iterations = 3  # 最大迭代次数（防止无限循环）
    
    def analyze_file_usages(self, file_usages: FileUsages, project_root: str, max_workers: int = 1) -> List[FixSuggestion]:
        """分析文件的 remoteExec 使用"""
        suggestions = []
        
        # 处理文件路径
        file_path_str = file_usages.file_path.replace('\\', '/')
        if file_path_str.startswith(project_root.replace('\\', '/')):
            file_path = Path(file_path_str)
        else:
            file_path = Path(project_root) / file_path_str
        
        if not file_path.exists():
            print(f"警告: 文件不存在: {file_path}")
            return suggestions
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                file_content = f.read()
        except Exception as e:
            print(f"错误: 无法读取文件 {file_path}: {e}")
            return suggestions
        
        lines = file_content.split('\n')
        
        # 并发分析
        if max_workers > 1 and len(file_usages.usages) > 1:
            with ThreadPoolExecutor(max_workers=min(max_workers, len(file_usages.usages))) as executor:
                futures = {
                    executor.submit(self._analyze_single_usage, usage, lines, file_usages.file_path): usage
                    for usage in file_usages.usages
                }
                
                for future in as_completed(futures):
                    try:
                        suggestion = future.result()
                        if suggestion:
                            suggestions.append(suggestion)
                    except Exception as e:
                        usage = futures[future]
                        print(f"  错误: 分析失败 {file_usages.file_path}:{usage.line} - {e}")
        else:
            # 串行分析
            for usage in file_usages.usages:
                suggestion = self._analyze_single_usage(usage, lines, file_usages.file_path)
                if suggestion:
                    suggestions.append(suggestion)
        
        return suggestions
    
    def _analyze_single_usage(self, usage: RemoteExecUsage, file_lines: List[str], file_path: str) -> Optional[FixSuggestion]:
        """分析单个 remoteExec 使用"""
        # 预检查：过滤明显不需要检查的情况
        if self._should_skip_analysis(usage):
            return None
        
        # 构建上下文代码
        context_code = '\n'.join([
            f"{i+len(usage.context_before)-CONTEXT_LINES+1:4d}| {line}"
            for i, line in enumerate(usage.context_before + [usage.full_line] + usage.context_after)
        ])
        
        # 构建提示词
        prompt = f"""你是一个 Arma 3 SQF 代码专家。请检查以下 remoteExec 的使用是否正确。

**文件**: {file_path}
**位置**: 第 {usage.line} 行，第 {usage.column} 列

**remoteExec 调用**:
```sqf
{usage.code_snippet}
```

**完整行**:
```sqf
{usage.full_line}
```

**上下文代码** (带行号):
```
{context_code}
```

请检查以下问题：
1. **null 检查**: 在使用 netId 或对象作为 remoteExec 参数前，是否检查了对象是否为 null？
2. **netId 使用**: netId 的使用是否正确？在单机模式下应该返回空字符串
3. **语法错误**: remoteExec 的语法是否正确？括号是否匹配？
4. **对象有效性**: 传递给 remoteExec 的对象是否可能为 null 或无效？

**重要：区分对象和基本类型**:
- **对象变量**: 以 `_` 开头的变量（如 `_unit`, `_player`, `_target`）通常是对象，需要 null 检查
- **字符串/数字**: 字符串字面量、数字、字符串变量（如 `_command`, `_str`）不需要 null 检查
- **数组**: 纯数字或字符串数组（如 `[1]`, `["text"]`）不需要 null 检查
- **特殊变量**: `player`, `cursorTarget` 等内置对象需要 null 检查

**常见错误模式**:
- `netId _unit` 在 `_unit` 可能为 null 时使用（**这是真实错误**）
- 缺少 `!(isNull _unit)` 检查（**这是真实错误**）
- 单机模式下直接使用 `netId` 而不是 `if (isMultiplayer) then {{netId _unit}} else {{""}}`
- remoteExec 的括号不匹配

**误报示例（不需要修复）**:
- `[2, compile _command]` - `_command` 是字符串，不需要检查
- `[1] remoteExec [...]` - 数字数组，没有对象参数
- `[getPlayerUID _healer, 200, "text"]` - 如果只有 `_healer` 作为 target，需要检查；如果只是参数，不需要

**正确的模式**:
```sqf
// 正确：检查 null 并使用安全的 netId（对象作为参数和 target）
if (!(isNull _unit)) then {{
    [[if (isMultiplayer) then {{netId _unit}} else {{""}},_unit], ...] remoteExec ["function", _unit, false];
}};

// 正确：在早期退出时检查
if (isNull _target || !alive _target) exitWith {{}};
[[if (isMultiplayer) then {{netId _target}} else {{""}}, _target], ...] remoteExec ["function", _target, false];

// 正确：对象只作为 target，参数中没有对象
if (!(isNull _healer)) then {{
    [getPlayerUID _healer, 200, "text"] remoteExec ["function", _healer, false];
}};
```

**修复要求**:
- 如果发现问题，fixed_code 必须包含完整的修复代码，包括 if 语句和 null 检查
- 不要只移除缩进或格式化代码，必须实际添加 null 检查
- 确保引号正确（SQF 使用双引号，不是单引号）
- 如果修复需要多行，保持适当的缩进

请以 JSON 格式返回，格式如下：
{{
    "has_issue": true/false,
    "issue_type": "null_check" / "netid_usage" / "syntax_error" / "other" / "none",
    "explanation": "问题说明（中文）",
    "fixed_code": "修复后的完整代码（如果需要修复）",
    "confidence": 0.0-1.0,
    "suggested_line_number": {usage.line}
}}

如果没有问题，has_issue 应该为 false，fixed_code 为空字符串。"""
        
        response = self._call_api(prompt)
        if not response:
            return None
        
        # 解析响应
        try:
            json_match = re.search(r'\{.*\}', response, re.DOTALL)
            if json_match:
                result = json.loads(json_match.group(0))
                
                if result.get('has_issue', False):
                    return FixSuggestion(
                        file_path=file_path,
                        line=usage.line,
                        original_code=usage.full_line,
                        fixed_code=result.get('fixed_code', ''),
                        explanation=result.get('explanation', ''),
                        confidence=result.get('confidence', 0.5),
                        issue_type=result.get('issue_type', 'other')
                    )
                else:
                    return None
        except json.JSONDecodeError as e:
            print(f"  [解析错误] {file_path}:{usage.line} - 无法解析 JSON: {e}")
            print(f"  响应: {response[:200]}")
            return None
        
        return None
    
    def _should_skip_analysis(self, usage: RemoteExecUsage) -> bool:
        """预检查：过滤明显不需要检查的情况"""
        code = usage.code_snippet.lower()
        full_line = usage.full_line.lower()
        
        # 检查是否包含对象参数
        # 如果 remoteExec 的参数中没有对象变量，可能不需要检查
        # 例如：[1], ["text"], [compile _command] 等
        
        # 检查是否有 netId 调用（这是最需要检查的）
        if 'netid' in code or 'netId' in code:
            return False  # 有 netId，需要检查
        
        # 检查 remoteExec 的 target 参数是否是对象变量
        # remoteExec 的格式通常是: [...] remoteExec ["function", target, jip]
        remoteexec_match = re.search(r'remoteExec\s*\[\s*["\'][^"\']+["\']\s*,\s*([^,\]]+)\s*[,\)]', full_line)
        if remoteexec_match:
            target = remoteexec_match.group(1).strip()
            # 如果是对象变量（以 _ 开头或 player, cursorTarget 等）
            if re.match(r'^(_\w+|player|cursorTarget|objNull)', target):
                return False  # target 是对象，需要检查
        
        # 检查参数中是否有对象变量
        # 查找 [...] 中的对象变量
        params_match = re.search(r'\[([^\]]+)\]\s*remoteExec', full_line)
        if params_match:
            params = params_match.group(1)
            # 检查是否有对象变量
            if re.search(r'\b(_\w+|player|cursorTarget)\b', params):
                return False  # 参数中有对象，需要检查
        
        # 如果只是数字、字符串或 compile，可能是误报
        if re.match(r'^\s*\[\s*\d+\s*\]', full_line):  # [1], [2] 等
            return True  # 纯数字数组，跳过
        
        if 'compile' in code and not re.search(r'\b(_\w+|player|cursorTarget)\b', full_line):
            # compile _command 等，没有对象变量
            return True  # 可能是误报，跳过
        
        return False  # 默认需要检查
    
    def _call_api(self, prompt: str) -> Optional[str]:
        """调用 LM Studio API"""
        try:
            response = requests.post(
                self.api_url,
                json={
                    "model": self.model,
                    "messages": [
                        {
                            "role": "system",
                            "content": """你是一个 Arma 3 SQF 代码专家，擅长检查 remoteExec 的使用是否正确。

你的任务：
1. 检查 remoteExec 调用前是否有适当的 null 检查
2. 检查 netId 的使用是否正确（特别是单机模式）
3. 检查语法错误
4. 提供准确的修复建议
5. 始终以 JSON 格式返回结果

特别注意：
- **区分对象和基本类型**：只有对象变量需要 null 检查，字符串、数字、数组不需要
- 在 SQF 中，如果对象为 null，调用 netId 会报错
- 应该先检查 `!(isNull _object)` 或 `isNull _object`
- 在单机模式下，netId 应该返回空字符串
- remoteExec 的语法：`[params, "function", target, jip] remoteExec ["function", target, jip]`
- **修复代码要求**：必须实际添加 null 检查，不要只格式化代码
- **引号要求**：SQF 字符串使用双引号 `"`，不是单引号 `'`"""
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    "temperature": 0.1,
                    "max_tokens": MAX_CONTEXT_TOKENS,
                    "top_p": 0.9,
                    "frequency_penalty": 0.0,
                    "presence_penalty": 0.0
                },
                timeout=self.timeout
            )
            
            if response.status_code == 200:
                result = response.json()
                return result['choices'][0]['message']['content']
            else:
                print(f"API 错误: {response.status_code} - {response.text}")
                return None
        
        except requests.exceptions.Timeout:
            print(f"API 调用超时（{self.timeout}秒）")
            return None
        except Exception as e:
            print(f"API 调用错误: {e}")
            return None

# ============================================================================
# 修复应用器
# ============================================================================

class FixApplier:
    """应用修复建议"""
    
    def __init__(self, project_root: str, dry_run: bool = True):
        self.project_root = Path(project_root)
        self.dry_run = dry_run
    
    def apply_fixes(self, suggestions: List[FixSuggestion]) -> Dict[str, int]:
        """应用修复建议"""
        stats = {
            'total': len(suggestions),
            'applied': 0,
            'skipped': 0,
            'errors': 0
        }
        
        # 按文件分组
        fixes_by_file = {}
        for suggestion in suggestions:
            if suggestion.file_path not in fixes_by_file:
                fixes_by_file[suggestion.file_path] = []
            fixes_by_file[suggestion.file_path].append(suggestion)
        
        # 对每个文件应用修复
        for file_path, file_suggestions in fixes_by_file.items():
            file_path_str = file_path.replace('\\', '/')
            if file_path_str.startswith(str(self.project_root).replace('\\', '/')):
                full_path = Path(file_path_str)
            else:
                full_path = self.project_root / file_path_str
            
            if not full_path.exists():
                print(f"警告: 文件不存在: {full_path}")
                stats['errors'] += len(file_suggestions)
                continue
            
            try:
                with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                    lines = f.readlines()
                
                # 按行号倒序排序
                file_suggestions.sort(key=lambda x: x.line, reverse=True)
                
                # 应用修复
                for suggestion in file_suggestions:
                    if 0 < suggestion.line <= len(lines):
                        original_line = lines[suggestion.line - 1]
                        if suggestion.fixed_code and suggestion.fixed_code.strip():
                            # 验证修复是否有效
                            if not self._validate_fix(suggestion, original_line):
                                print(f"  ⚠ 跳过无效修复 {file_path}:{suggestion.line} - 修复建议可能不完整")
                                stats['skipped'] += 1
                                continue
                            
                            fixed = suggestion.fixed_code.rstrip()
                            if not fixed.endswith('\n'):
                                fixed += '\n'
                            
                            lines[suggestion.line - 1] = fixed
                            stats['applied'] += 1
                            print(f"  ✓ 修复 {file_path}:{suggestion.line} [{suggestion.issue_type}]")
                            print(f"     原: {original_line.rstrip()}")
                            print(f"     新: {fixed.rstrip()}")
                        else:
                            stats['skipped'] += 1
                
                # 写回文件
                if not self.dry_run and stats['applied'] > 0:
                    with open(full_path, 'w', encoding='utf-8') as f:
                        f.writelines(lines)
                    print(f"  ✓ 已保存: {file_path}")
                elif self.dry_run:
                    print(f"  [试运行] 将修复 {file_path}")
            
            except Exception as e:
                print(f"错误: 无法处理文件 {full_path}: {e}")
                stats['errors'] += len(file_suggestions)
        
        return stats
    
    def _validate_fix(self, suggestion: FixSuggestion, original_line: str) -> bool:
        """验证修复建议是否有效"""
        fixed_code = suggestion.fixed_code.strip()
        original = original_line.strip()
        
        # 如果修复后的代码和原始代码相同（除了缩进），说明没有实际修复
        if fixed_code.replace(' ', '') == original.replace(' ', ''):
            return False
        
        # 对于 null_check 类型，必须包含 isNull 检查
        if suggestion.issue_type == 'null_check':
            if 'isnull' not in fixed_code.lower() and 'isNull' not in fixed_code:
                return False
            
            # 必须包含 if 语句
            if 'if' not in fixed_code.lower():
                return False
        
        # 检查引号是否正确（SQF 使用双引号）
        if "'" in fixed_code and '"' not in fixed_code:
            # 如果只有单引号，可能是错误的
            # 但 format 函数内部可能使用单引号，所以只检查明显错误的情况
            if re.search(r'remoteExec\s*\[\s*\'', fixed_code):
                return False  # remoteExec 的参数应该用双引号
        
        # 检查是否实际添加了检查（修复后的代码应该比原始代码长或结构不同）
        if len(fixed_code) < len(original) * 0.8:
            # 如果修复后的代码明显更短，可能是错误的
            return False
        
        return True

# ============================================================================
# 报告生成器
# ============================================================================

class FixReportGenerator:
    """生成修复报告"""
    
    def __init__(self, output_file: str = "remoteExec_fix_report.md"):
        self.output_file = output_file
    
    def generate(self, suggestions: List[FixSuggestion], stats: Dict) -> str:
        """生成修复报告"""
        report = f"""# remoteExec 使用检查报告

生成时间: {time.strftime('%Y-%m-%d %H:%M:%S')}

## 统计信息

- **总问题数**: {stats.get('total', 0)}
- **已修复**: {stats.get('applied', 0)}
- **跳过**: {stats.get('skipped', 0)}
- **错误**: {stats.get('errors', 0)}

## 问题分类

"""
        
        # 按问题类型分组
        by_type = {}
        for suggestion in suggestions:
            issue_type = suggestion.issue_type
            if issue_type not in by_type:
                by_type[issue_type] = []
            by_type[issue_type].append(suggestion)
        
        for issue_type, type_suggestions in sorted(by_type.items()):
            report += f"- **{issue_type}**: {len(type_suggestions)} 个\n"
        
        report += "\n## 修复建议\n\n"
        
        # 按文件分组
        fixes_by_file = {}
        for suggestion in suggestions:
            if suggestion.file_path not in fixes_by_file:
                fixes_by_file[suggestion.file_path] = []
            fixes_by_file[suggestion.file_path].append(suggestion)
        
        # 生成详细报告
        for file_path, file_suggestions in sorted(fixes_by_file.items()):
            report += f"### {file_path}\n\n"
            
            for suggestion in sorted(file_suggestions, key=lambda x: x.line):
                report += f"#### 行 {suggestion.line} [{suggestion.issue_type}]\n\n"
                report += f"**原始代码**:\n```sqf\n{suggestion.original_code}\n```\n\n"
                if suggestion.fixed_code:
                    report += f"**修复后**:\n```sqf\n{suggestion.fixed_code}\n```\n\n"
                report += f"**说明**: {suggestion.explanation}\n\n"
                report += f"**置信度**: {suggestion.confidence:.2f}\n\n"
                report += "---\n\n"
        
        return report
    
    def save(self, report: str):
        """保存报告"""
        with open(self.output_file, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"\n报告已保存到: {self.output_file}")

# ============================================================================
# 主程序
# ============================================================================

def main():
    parser = argparse.ArgumentParser(description='检查所有 remoteExec 的使用并生成修复建议')
    parser.add_argument('--root', type=str, default=PROJECT_ROOT,
                       help='项目根目录（默认: addons/mcc_sandbox_mod）')
    parser.add_argument('--output', type=str, default='remoteExec_fix_report.md',
                       help='输出报告文件（默认: remoteExec_fix_report.md）')
    parser.add_argument('--apply', action='store_true',
                       help='应用修复（默认: 仅生成报告）')
    parser.add_argument('--limit', type=int, default=None,
                       help='限制处理的文件数量（用于测试）')
    parser.add_argument('--max-workers', type=int, default=DEFAULT_MAX_WORKERS,
                       help=f'并发处理线程数（默认: {DEFAULT_MAX_WORKERS}）')
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("remoteExec 使用检查工具")
    print("=" * 60)
    print(f"\n项目根目录: {args.root}")
    print(f"输出文件: {args.output}")
    print(f"应用修复: {'是' if args.apply else '否（试运行）'}")
    print("\n[AMD Radeon RX 7900 XT 优化配置]")
    print(f"  最大上下文: {MAX_CONTEXT_TOKENS} tokens")
    print(f"  并发线程数: {args.max_workers}")
    print(f"  API 超时: {TIMEOUT} 秒")
    print(f"  上下文行数: {CONTEXT_LINES} 行")
    
    # 扫描所有 remoteExec 使用
    print("\n扫描 remoteExec 使用...")
    scanner = RemoteExecScanner(args.root)
    files_usages = scanner.scan_all_files()
    
    if args.limit:
        files_usages = files_usages[:args.limit]
        print(f"限制处理前 {args.limit} 个文件")
    
    total_usages = sum(len(fu.usages) for fu in files_usages)
    print(f"找到 {len(files_usages)} 个文件，共 {total_usages} 个 remoteExec 使用")
    
    # 分析错误
    print(f"\n分析 remoteExec 使用（使用 LM Studio，{args.max_workers} 个并发线程）...")
    analyzer = LMStudioAnalyzer()
    all_suggestions = []
    
    # 使用线程池并发处理多个文件
    if args.max_workers > 1 and len(files_usages) > 1:
        print(f"使用 {args.max_workers} 个并发线程处理文件...")
        with ThreadPoolExecutor(max_workers=min(args.max_workers, len(files_usages))) as executor:
            futures = {
                executor.submit(analyzer.analyze_file_usages, file_usages, args.root, args.max_workers): file_usages
                for file_usages in files_usages
            }
            
            completed = 0
            for future in as_completed(futures):
                file_usages = futures[future]
                completed += 1
                try:
                    suggestions = future.result()
                    all_suggestions.extend(suggestions)
                    print(f"[{completed}/{len(files_usages)}] ✓ {file_usages.file_path}: {len(file_usages.usages)} 个使用，{len(suggestions)} 个问题")
                except Exception as e:
                    print(f"[{completed}/{len(files_usages)}] ✗ {file_usages.file_path}: 错误 - {e}")
    else:
        # 串行处理
        for i, file_usages in enumerate(files_usages, 1):
            print(f"\n[{i}/{len(files_usages)}] 分析: {file_usages.file_path} ({len(file_usages.usages)} 个使用)")
            
            suggestions = analyzer.analyze_file_usages(file_usages, args.root, 1)
            all_suggestions.extend(suggestions)
            
            print(f"  发现 {len(suggestions)} 个问题")
            time.sleep(0.2)  # 短暂延迟避免 API 过载
    
    # 应用修复
    print(f"\n\n总共发现 {len(all_suggestions)} 个问题")
    
    if all_suggestions:
        applier = FixApplier(args.root, dry_run=not args.apply)
        stats = applier.apply_fixes(all_suggestions)
        
        # 生成报告
        report_gen = FixReportGenerator(args.output)
        report = report_gen.generate(all_suggestions, stats)
        report_gen.save(report)
        
        print("\n" + "=" * 60)
        print("处理完成")
        print("=" * 60)
        print(f"总问题数: {stats['total']}")
        print(f"已修复: {stats['applied']}")
        print(f"跳过: {stats['skipped']}")
        print(f"错误: {stats['errors']}")
    else:
        print("\n没有发现问题")

if __name__ == "__main__":
    main()

