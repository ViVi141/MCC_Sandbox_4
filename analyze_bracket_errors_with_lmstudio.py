#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用 LM Studio 的 qwen/qwen2.5-coder-14b 分析括号检查报告中的错误
并生成格式化的修复建议
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
BRACKET_REPORT = "bracket_check_report.md"

# ============================================================================
# AMD Radeon RX 7900 XT (20GB VRAM) 优化配置
# ============================================================================
# 7900 XT 有 20GB VRAM，可以：
# - 运行更大的上下文窗口
# - 支持更高的并发数
# - 处理更复杂的代码分析任务
MAX_CONTEXT_TOKENS = 8000      # 最大输出 tokens（充分利用 20GB VRAM）
MAX_INPUT_TOKENS = 20000       # 最大输入 tokens（代码+提示词）
TIMEOUT = 300                  # API 超时时间（大模型需要更长时间）
DEFAULT_MAX_WORKERS = 4        # 默认并发线程数（7900 XT 可以支持更高并发）
BATCH_SIZE = 3                 # 批处理大小（同时分析多个错误）
CONTEXT_LINES = 20             # 上下文行数（增加以提供更多上下文）

# ============================================================================
# 数据模型
# ============================================================================

@dataclass
class BracketError:
    """括号错误"""
    file_path: str
    line: int
    column: int
    bracket_type: str  # "圆括号", "方括号", "花括号"
    error_type: str    # "unclosed", "unopened", "mismatch"
    message: str
    code_snippet: str

@dataclass
class FileErrors:
    """文件错误集合"""
    file_path: str
    total_lines: int
    error_count: int
    errors: List[BracketError]

@dataclass
class FixSuggestion:
    """修复建议"""
    file_path: str
    line: int
    original_code: str
    fixed_code: str
    explanation: str
    confidence: float  # 0.0-1.0

# ============================================================================
# 报告解析器
# ============================================================================

class ReportParser:
    """解析括号检查报告"""
    
    def __init__(self, report_file: str):
        self.report_file = Path(report_file)
    
    def parse(self) -> List[FileErrors]:
        """解析报告文件"""
        if not self.report_file.exists():
            print(f"错误: 报告文件不存在: {self.report_file}")
            return []
        
        with open(self.report_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        files_errors = []
        
        # 使用正则表达式匹配文件块
        file_blocks = re.split(r'^### ', content, flags=re.MULTILINE)
        
        for block in file_blocks[1:]:  # 跳过第一个空块
            lines = block.split('\n')
            if not lines:
                continue
            
            # 解析文件路径
            file_path = lines[0].strip().replace('\\', '/')
            
            # 解析总行数和问题数
            total_lines = 0
            error_count = 0
            for line in lines[1:10]:  # 只检查前几行
                if '总行数' in line:
                    match = re.search(r'总行数.*?(\d+)', line)
                    if match:
                        total_lines = int(match.group(1))
                if '问题数' in line:
                    match = re.search(r'问题数.*?(\d+)', line)
                    if match:
                        error_count = int(match.group(1))
            
            current_errors = []
            
            # 解析错误
            # 未闭合错误 (🔴)
            for match in re.finditer(
                r'🔴 \*\*行 (\d+)，列 (\d+)\*\* \((.+?)\)\n\n\*\*问题\*\*: (.+?)\n\n\*\*代码\*\*:\n```sqf\n(.*?)\n```',
                block,
                re.DOTALL
            ):
                bracket_type = match.group(3)
                error_type = "unclosed" if "未闭合" in match.group(4) else "unopened"
                current_errors.append(BracketError(
                    file_path=file_path,
                    line=int(match.group(1)),
                    column=int(match.group(2)),
                    bracket_type=bracket_type,
                    error_type=error_type,
                    message=match.group(4),
                    code_snippet=match.group(5).strip()
                ))
            
            # 类型不匹配错误 (🟠)
            for match in re.finditer(
                r'🟠 \*\*行 (\d+)，列 (\d+)\*\* \((.+?)\)\n\n\*\*问题\*\*: (.+?)\n\n\*\*代码\*\*:\n```sqf\n(.*?)\n```',
                block,
                re.DOTALL
            ):
                current_errors.append(BracketError(
                    file_path=file_path,
                    line=int(match.group(1)),
                    column=int(match.group(2)),
                    bracket_type=match.group(3),
                    error_type="mismatch",
                    message=match.group(4),
                    code_snippet=match.group(5).strip()
                ))
            
            # 未匹配的闭括号 (🟡)
            for match in re.finditer(
                r'🟡 \*\*行 (\d+)，列 (\d+)\*\* \((.+?)\)\n\n\*\*问题\*\*: (.+?)\n\n\*\*代码\*\*:\n```sqf\n(.*?)\n```',
                block,
                re.DOTALL
            ):
                current_errors.append(BracketError(
                    file_path=file_path,
                    line=int(match.group(1)),
                    column=int(match.group(2)),
                    bracket_type=match.group(3),
                    error_type="unopened",
                    message=match.group(4),
                    code_snippet=match.group(5).strip()
                ))
            
            if current_errors:
                files_errors.append(FileErrors(
                    file_path=file_path,
                    total_lines=total_lines,
                    error_count=error_count,
                    errors=current_errors
                ))
        
        return files_errors

# ============================================================================
# LM Studio API 调用
# ============================================================================

class LMStudioAnalyzer:
    """使用 LM Studio 分析错误"""
    
    def __init__(self, api_url: str = LM_STUDIO_API_URL, model: str = MODEL_NAME):
        self.api_url = api_url
        self.model = model
        self.timeout = TIMEOUT
    
    def analyze_file_errors(self, file_errors: FileErrors, project_root: str, max_workers: int = 1) -> List[FixSuggestion]:
        """分析文件错误并生成修复建议（支持批处理）"""
        suggestions = []
        
        # 处理文件路径
        # 如果文件路径已经包含项目根目录，直接使用；否则拼接
        file_path_str = file_errors.file_path.replace('\\', '/')
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
        
        # 使用相对路径用于显示
        try:
            display_path = str(file_path.relative_to(Path(project_root)))
        except ValueError:
            display_path = file_errors.file_path
        
        lines = file_content.split('\n')
        
        # 批处理分析（7900 XT 可以同时处理多个错误）
        if max_workers > 1 and len(file_errors.errors) > 1:
            # 使用线程池并发分析
            with ThreadPoolExecutor(max_workers=min(max_workers, len(file_errors.errors))) as executor:
                futures = {
                    executor.submit(self._analyze_single_error, error, lines, display_path): error
                    for error in file_errors.errors
                }
                
                for future in as_completed(futures):
                    try:
                        suggestion = future.result()
                        if suggestion:
                            suggestions.append(suggestion)
                    except Exception as e:
                        error = futures[future]
                        print(f"  错误: 分析失败 {display_path}:{error.line} - {e}")
        else:
            # 串行分析
            for error in file_errors.errors:
                suggestion = self._analyze_single_error(error, lines, display_path)
                if suggestion:
                    suggestions.append(suggestion)
        
        return suggestions
    
    def _analyze_single_error(self, error: BracketError, file_lines: List[str], file_path: str) -> Optional[FixSuggestion]:
        """分析单个错误"""
        # 获取错误周围的上下文（7900 XT 可以处理更大的上下文）
        context_start = max(0, error.line - CONTEXT_LINES)
        context_end = min(len(file_lines), error.line + CONTEXT_LINES)
        context_lines = file_lines[context_start:context_end]
        context_code = '\n'.join([f"{i+context_start+1:4d}| {line}" for i, line in enumerate(context_lines)])
        
        # 获取实际错误行的完整内容
        actual_line = file_lines[error.line - 1] if 0 < error.line <= len(file_lines) else error.code_snippet
        
        # 构建提示词
        prompt = f"""你是一个 Arma 3 SQF 代码专家。请分析以下括号错误并提供修复建议。

**文件**: {file_path}
**错误位置**: 第 {error.line} 行，第 {error.column} 列
**错误类型**: {error.error_type}
**括号类型**: {error.bracket_type}
**错误信息**: {error.message}

**报告中的代码片段**:
```sqf
{error.code_snippet}
```

**实际文件中的第 {error.line} 行**:
```sqf
{actual_line}
```

**上下文代码** (第 {context_start+1}-{context_end} 行，带行号):
```
{context_code}
```

请分析这个错误：
1. 判断这是真实错误还是误报（检查脚本可能误判字符串中的括号，特别是 format 函数中的多行字符串）
2. 如果是真实错误，提供具体的修复建议，返回完整的修复后的行
3. 如果是误报，说明原因

**重要提示**：
- SQF 中的 format 函数可能包含多行字符串，括号检查脚本可能误判
- 字符串中的括号不应该被计算在内
- 如果错误代码片段看起来是完整的（如完整的数组定义），很可能是误报

请以 JSON 格式返回，格式如下：
{{
    "is_real_error": true/false,
    "explanation": "错误原因或误报原因（中文）",
    "fixed_code": "修复后的完整行代码（如果是真实错误，必须包含完整的行）",
    "confidence": 0.0-1.0,
    "suggested_line_number": {error.line}
}}

如果这是误报，fixed_code 必须为空字符串。"""
        
        response = self._call_api(prompt)
        if not response:
            return None
        
        # 解析响应
        try:
            # 尝试提取 JSON
            json_match = re.search(r'\{.*\}', response, re.DOTALL)
            if json_match:
                result = json.loads(json_match.group(0))
                
                if result.get('is_real_error', False):
                    return FixSuggestion(
                        file_path=file_path,
                        line=error.line,
                        original_code=error.code_snippet,
                        fixed_code=result.get('fixed_code', ''),
                        explanation=result.get('explanation', ''),
                        confidence=result.get('confidence', 0.5)
                    )
                else:
                    # 误报，记录但不修复
                    print(f"  [误报] {file_path}:{error.line} - {result.get('explanation', '')}")
                    return None
        except json.JSONDecodeError as e:
            print(f"  [解析错误] {file_path}:{error.line} - 无法解析 JSON: {e}")
            print(f"  响应: {response[:200]}")
            return None
        
        return None
    
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
                            "content": """你是一个 Arma 3 SQF 代码专家，擅长分析括号错误和提供修复建议。

你的任务：
1. 仔细分析括号错误，判断是真实错误还是误报
2. 对于真实错误，提供准确的修复建议
3. 对于误报，说明原因（通常是字符串中的括号被误判）
4. 始终以 JSON 格式返回结果

特别注意：
- SQF 中的 format 函数可能包含多行字符串
- 字符串中的括号不应该被计算
- 数组定义中的嵌套括号需要仔细检查"""
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
            # 处理文件路径
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
                # 读取文件
                with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                    lines = f.readlines()
                
                # 按行号倒序排序（从后往前修复，避免行号偏移）
                file_suggestions.sort(key=lambda x: x.line, reverse=True)
                
                # 应用修复
                for suggestion in file_suggestions:
                    if 0 < suggestion.line <= len(lines):
                        original_line = lines[suggestion.line - 1]
                        if suggestion.fixed_code and suggestion.fixed_code.strip():
                            # 确保修复后的代码以换行符结尾
                            fixed = suggestion.fixed_code.rstrip()
                            if not fixed.endswith('\n'):
                                fixed += '\n'
                            
                            # 替换整行
                            lines[suggestion.line - 1] = fixed
                            stats['applied'] += 1
                            print(f"  ✓ 修复 {file_path}:{suggestion.line}")
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

# ============================================================================
# 报告生成器
# ============================================================================

class FixReportGenerator:
    """生成修复报告"""
    
    def __init__(self, output_file: str = "bracket_fix_report.md"):
        self.output_file = output_file
    
    def generate(self, suggestions: List[FixSuggestion], stats: Dict) -> str:
        """生成修复报告"""
        report = f"""# 括号错误修复报告

生成时间: {time.strftime('%Y-%m-%d %H:%M:%S')}

## 统计信息

- **总错误数**: {stats.get('total', 0)}
- **已修复**: {stats.get('applied', 0)}
- **跳过**: {stats.get('skipped', 0)}
- **错误**: {stats.get('errors', 0)}

## 修复建议

"""
        
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
                report += f"#### 行 {suggestion.line}\n\n"
                report += f"**原始代码**:\n```sqf\n{suggestion.original_code}\n```\n\n"
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
    parser = argparse.ArgumentParser(description='使用 LM Studio 分析括号错误并生成修复建议')
    parser.add_argument('--report', type=str, default=BRACKET_REPORT,
                       help='括号检查报告文件（默认: bracket_check_report.md）')
    parser.add_argument('--root', type=str, default=PROJECT_ROOT,
                       help='项目根目录（默认: addons/mcc_sandbox_mod）')
    parser.add_argument('--output', type=str, default='bracket_fix_report.md',
                       help='输出报告文件（默认: bracket_fix_report.md）')
    parser.add_argument('--apply', action='store_true',
                       help='应用修复（默认: 仅生成报告）')
    parser.add_argument('--limit', type=int, default=None,
                       help='限制处理的文件数量（用于测试）')
    parser.add_argument('--max-workers', type=int, default=DEFAULT_MAX_WORKERS,
                       help=f'并发处理线程数（默认: {DEFAULT_MAX_WORKERS}，针对 7900 XT 优化）')
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("括号错误分析和修复工具")
    print("=" * 60)
    print(f"\n报告文件: {args.report}")
    print(f"项目根目录: {args.root}")
    print(f"输出文件: {args.output}")
    print(f"应用修复: {'是' if args.apply else '否（试运行）'}")
    print("\n[AMD Radeon RX 7900 XT 优化配置]")
    print(f"  最大上下文: {MAX_CONTEXT_TOKENS} tokens (输出) / {MAX_INPUT_TOKENS} tokens (输入)")
    print(f"  并发线程数: {args.max_workers}")
    print(f"  API 超时: {TIMEOUT} 秒")
    print(f"  上下文行数: {CONTEXT_LINES} 行")
    
    # 解析报告
    print("\n解析报告...")
    parser = ReportParser(args.report)
    files_errors = parser.parse()
    
    if args.limit:
        files_errors = files_errors[:args.limit]
        print(f"限制处理前 {args.limit} 个文件")
    
    print(f"找到 {len(files_errors)} 个有问题的文件")
    
    # 分析错误（使用并发处理以充分利用 7900 XT）
    print(f"\n分析错误（使用 LM Studio，{args.max_workers} 个并发线程）...")
    analyzer = LMStudioAnalyzer()
    all_suggestions = []
    
    # 使用线程池并发处理多个文件
    if args.max_workers > 1 and len(files_errors) > 1:
        print(f"使用 {args.max_workers} 个并发线程处理文件...")
        with ThreadPoolExecutor(max_workers=min(args.max_workers, len(files_errors))) as executor:
            futures = {
                executor.submit(analyzer.analyze_file_errors, file_errors, args.root, args.max_workers): file_errors
                for file_errors in files_errors
            }
            
            completed = 0
            for future in as_completed(futures):
                file_errors = futures[future]
                completed += 1
                try:
                    suggestions = future.result()
                    all_suggestions.extend(suggestions)
                    print(f"[{completed}/{len(files_errors)}] ✓ {file_errors.file_path}: 生成 {len(suggestions)} 个修复建议")
                except Exception as e:
                    print(f"[{completed}/{len(files_errors)}] ✗ {file_errors.file_path}: 错误 - {e}")
    else:
        # 串行处理
        for i, file_errors in enumerate(files_errors, 1):
            print(f"\n[{i}/{len(files_errors)}] 分析: {file_errors.file_path} ({file_errors.error_count} 个错误)")
            
            suggestions = analyzer.analyze_file_errors(file_errors, args.root, 1)
            all_suggestions.extend(suggestions)
            
            print(f"  生成 {len(suggestions)} 个修复建议")
            time.sleep(0.2)  # 短暂延迟避免 API 过载
    
    # 应用修复
    print(f"\n\n总共生成 {len(all_suggestions)} 个修复建议")
    
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
        print(f"总错误数: {stats['total']}")
        print(f"已修复: {stats['applied']}")
        print(f"跳过: {stats['skipped']}")
        print(f"错误: {stats['errors']}")
    else:
        print("\n没有生成修复建议")

if __name__ == "__main__":
    main()

