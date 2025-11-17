#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用 LM Studio 对每个项目文件进行 Arma 3 语法检查
"""

import re
import json
import requests
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
import argparse
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# ============================================================================
# 配置
# ============================================================================

LM_STUDIO_API_URL = "http://localhost:1234/v1/chat/completions"
MODEL_NAME = "qwen/qwen2.5-coder-14b"
PROJECT_ROOT = "addons/mcc_sandbox_mod"

# Qwen2.5-Coder-14B 配置 - 针对 AMD Radeon RX 7900 XT (20GB VRAM) 优化
# 7900 XT 有足够的 VRAM 运行 14B 模型，但需要合理配置上下文以避免内存溢出
MAX_CONTEXT_TOKENS = 6000   # 最大输出 tokens（响应长度）- 保守设置以确保稳定性
MAX_FILE_LINES = 3500       # 单次检查的最大行数（约 5000-7000 tokens）
MAX_INPUT_TOKENS = 16000    # 最大输入 tokens（提示词+代码）- 充分利用 20GB VRAM
CHUNK_OVERLAP = 150         # 分片重叠行数（避免在分片边界遗漏问题）
ENABLE_CHUNKING = True      # 是否启用分片处理

# Arma 3 相关文件扩展名
ARMA3_FILE_EXTENSIONS = {'.sqf', '.hpp', '.cpp', '.h', '.ext'}

# ============================================================================
# 数据模型
# ============================================================================

class SyntaxCheckStatus(Enum):
    """语法检查状态"""
    PENDING = "pending"
    CHECKING = "checking"
    PASSED = "passed"
    FAILED = "failed"
    ERROR = "error"
    SKIPPED = "skipped"

@dataclass
class SyntaxIssue:
    """语法问题"""
    line: int
    column: Optional[int] = None
    severity: str = "error"  # error, warning, info
    message: str = ""
    code_snippet: str = ""
    suggestion: str = ""

@dataclass
class FileSyntaxCheck:
    """文件语法检查结果"""
    file_path: str
    status: SyntaxCheckStatus = SyntaxCheckStatus.PENDING
    issues: List[SyntaxIssue] = None
    total_lines: int = 0
    checked_lines: int = 0
    llm_response: str = ""
    error_message: str = ""
    check_time: float = 0.0
    chunks_processed: int = 0  # 处理的分片数量
    
    def __post_init__(self):
        if self.issues is None:
            self.issues = []

# ============================================================================
# 文件扫描器
# ============================================================================

class FileScanner:
    """扫描项目中的 Arma 3 文件"""
    
    def __init__(self, root_dir: str = PROJECT_ROOT):
        self.root_dir = Path(root_dir)
        self.encodings = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
        self.exclude_dirs = {'.git', 'node_modules', '__pycache__', '.vscode', '.idea'}
        self.exclude_files = {'.bak', '.orig', '.tmp', '.log'}
    
    def is_arma3_file(self, file_path: Path) -> bool:
        """检查是否是 Arma 3 相关文件"""
        # 检查扩展名
        if file_path.suffix.lower() in ARMA3_FILE_EXTENSIONS:
            return True
        
        # 检查特定文件名
        if file_path.name.lower() in {'config.cpp', 'description.ext', 'stringtable.xml'}:
            return True
        
        return False
    
    def should_skip_file(self, file_path: Path) -> bool:
        """判断是否应该跳过文件"""
        # 跳过排除的目录
        for part in file_path.parts:
            if part in self.exclude_dirs:
                return True
        
        # 跳过备份文件
        if any(file_path.name.endswith(ext) for ext in self.exclude_files):
            return True
        
        return False
    
    def scan_files(self) -> List[Path]:
        """扫描所有 Arma 3 文件"""
        files = []
        
        if not self.root_dir.exists():
            print(f"错误: 项目根目录不存在: {self.root_dir}")
            return files
        
        for file_path in self.root_dir.rglob('*'):
            if file_path.is_file():
                if self.should_skip_file(file_path):
                    continue
                
                if self.is_arma3_file(file_path):
                    files.append(file_path)
        
        return sorted(files)
    
    def read_file(self, file_path: Path) -> Optional[str]:
        """读取文件内容"""
        for encoding in self.encodings:
            try:
                with open(file_path, 'r', encoding=encoding, errors='ignore') as f:
                    return f.read()
            except Exception:
                continue
        
        return None

# ============================================================================
# LM Studio API 调用
# ============================================================================

class LMStudioChecker:
    """使用 LM Studio 进行语法检查"""
    
    def __init__(self, api_url: str = LM_STUDIO_API_URL, model: str = MODEL_NAME):
        self.api_url = api_url
        self.model = model
        self.timeout = 180  # Qwen2.5-Coder-14B 可能需要更长的处理时间
    
    def check_syntax(self, file_path: Path, file_content: str) -> FileSyntaxCheck:
        """检查文件语法（支持分片处理）"""
        result = FileSyntaxCheck(
            file_path=str(file_path),
            status=SyntaxCheckStatus.CHECKING
        )
        
        start_time = time.time()
        
        try:
            # 计算文件行数
            lines = file_content.split('\n')
            result.total_lines = len(lines)
            
            # 判断是否需要分片处理
            if ENABLE_CHUNKING and len(lines) > MAX_FILE_LINES:
                # 分片处理大文件
                result = self._check_syntax_chunked(file_path, lines, result, start_time)
            else:
                # 单次处理小文件
                result = self._check_syntax_single(file_path, lines, result, start_time)
        
        except Exception as e:
            result.status = SyntaxCheckStatus.ERROR
            result.error_message = str(e)
            result.check_time = time.time() - start_time
        
        return result
    
    def _check_syntax_single(self, file_path: Path, lines: List[str], 
                            result: FileSyntaxCheck, start_time: float) -> FileSyntaxCheck:
        """单次检查（小文件）"""
        content_to_check = '\n'.join(lines)
        result.checked_lines = len(lines)
        result.chunks_processed = 1
        
        # 构建提示词
        prompt = self._build_prompt(file_path, content_to_check, chunk_info=None)
        
        # 调用 LM Studio API
        response = self._call_api(prompt)
        
        if response:
            result.llm_response = response
            result.status, result.issues = self._parse_response(response, lines)
        else:
            result.status = SyntaxCheckStatus.ERROR
            result.error_message = "无法连接到 LM Studio API"
        
        result.check_time = time.time() - start_time
        return result
    
    def _check_syntax_chunked(self, file_path: Path, lines: List[str], 
                             result: FileSyntaxCheck, start_time: float) -> FileSyntaxCheck:
        """分片检查（大文件）"""
        all_issues = []
        chunks = self._split_into_chunks(lines)
        result.chunks_processed = len(chunks)
        
        print(f"  文件较大 ({len(lines)} 行)，分成 {len(chunks)} 个片段处理...")
        
        for chunk_idx, (chunk_lines, start_line, end_line) in enumerate(chunks, 1):
            print(f"    处理片段 {chunk_idx}/{len(chunks)} (行 {start_line+1}-{end_line})...")
            
            chunk_content = '\n'.join(chunk_lines)
            chunk_info = {
                'chunk_num': chunk_idx,
                'total_chunks': len(chunks),
                'start_line': start_line + 1,  # 转换为1-based
                'end_line': end_line,
                'total_file_lines': len(lines)
            }
            
            # 构建提示词
            prompt = self._build_prompt(file_path, chunk_content, chunk_info=chunk_info)
            
            # 调用 LM Studio API
            response = self._call_api(prompt)
            
            if response:
                chunk_status, chunk_issues = self._parse_response(response, chunk_lines)
                
                # 调整行号（从片段相对行号转换为文件绝对行号）
                for issue in chunk_issues:
                    issue.line = start_line + issue.line
                    all_issues.append(issue)
            else:
                print(f"      警告: 片段 {chunk_idx} 检查失败")
        
        # 去重：合并重叠区域中的重复问题
        all_issues = self._deduplicate_issues(all_issues)
        
        # 设置结果
        result.issues = all_issues
        result.checked_lines = len(lines)
        result.status = SyntaxCheckStatus.FAILED if all_issues else SyntaxCheckStatus.PASSED
        result.check_time = time.time() - start_time
        
        return result
    
    def _split_into_chunks(self, lines: List[str]) -> List[Tuple[List[str], int, int]]:
        """将文件分割成多个片段"""
        chunks = []
        total_lines = len(lines)
        
        if total_lines <= MAX_FILE_LINES:
            return [(lines, 0, total_lines)]
        
        start = 0
        while start < total_lines:
            # 计算片段结束位置
            end = min(start + MAX_FILE_LINES, total_lines)
            
            # 提取片段
            chunk_lines = lines[start:end]
            
            chunks.append((chunk_lines, start, end))
            
            # 下一个片段开始位置（考虑重叠）
            if end < total_lines:
                start = end - CHUNK_OVERLAP
            else:
                break
        
        return chunks
    
    def _deduplicate_issues(self, issues: List[SyntaxIssue]) -> List[SyntaxIssue]:
        """去重：合并相似的问题"""
        if not issues:
            return []
        
        # 按行号排序
        issues.sort(key=lambda x: x.line)
        
        deduplicated = []
        seen = set()
        
        for issue in issues:
            # 创建唯一标识（行号+消息）
            key = (issue.line, issue.message[:50])  # 使用前50个字符作为消息摘要
            
            if key not in seen:
                seen.add(key)
                deduplicated.append(issue)
            # 如果行号相同但消息不同，保留更详细的
            else:
                # 找到已存在的相似问题
                for existing in deduplicated:
                    if existing.line == issue.line:
                        # 保留消息更详细的那个
                        if len(issue.message) > len(existing.message):
                            deduplicated.remove(existing)
                            deduplicated.append(issue)
                            break
        
        return deduplicated
    
    def _build_prompt(self, file_path: Path, content: str, chunk_info: Optional[Dict] = None) -> str:
        """构建检查提示词"""
        file_type = file_path.suffix.lower()
        file_name = file_path.name
        
        # 构建文件信息
        file_info = f"""文件路径: {file_path}
文件名: {file_name}"""
        
        # 如果是分片，添加分片信息
        if chunk_info:
            file_info += f"""
片段信息: 这是文件的第 {chunk_info['chunk_num']}/{chunk_info['total_chunks']} 个片段
片段范围: 第 {chunk_info['start_line']} 行到第 {chunk_info['end_line']} 行（共 {chunk_info['total_file_lines']} 行）
注意: 请使用文件中的绝对行号报告问题"""
        
        prompt = f"""请检查以下 Arma 3 {file_type.upper().lstrip('.')} 文件的语法是否正确。

{file_info}

请检查以下方面：
1. **基本语法错误**：括号匹配、引号匹配、分号使用、逗号使用
2. **SQF 语法规范**：
   - 变量声明和使用
   - 函数调用语法
   - 数组和哈希表语法
   - 控制流语句（if/else, switch, while, for）
   - 操作符使用
3. **Arma 3 特定语法**：
   - remoteExec 调用格式
   - BIS_fnc_* 函数调用
   - 配置类语法（CfgPatches, CfgFunctions 等）
   - 事件处理器语法
4. **常见错误**：
   - 未闭合的括号或引号
   - 错误的数组语法
   - 函数参数不匹配
   - 变量作用域问题

请以 JSON 格式返回结果，格式如下：
{{
    "status": "passed" | "failed" | "error",
    "issues": [
        {{
            "line": 行号,
            "column": 列号（可选）,
            "severity": "error" | "warning" | "info",
            "message": "问题描述",
            "code_snippet": "相关代码片段",
            "suggestion": "修复建议（可选）"
        }}
    ],
    "summary": "总体评估"
}}

如果语法完全正确，返回 status: "passed" 和空的 issues 数组。

文件内容：
```
{content}
```"""
        
        return prompt
    
    def _call_api(self, prompt: str, max_tokens: int = MAX_CONTEXT_TOKENS) -> Optional[str]:
        """调用 LM Studio API"""
        try:
            response = requests.post(
                self.api_url,
                json={
                    "model": self.model,
                    "messages": [
                        {
                            "role": "system",
                            "content": """你是一个 Arma 3 SQF 代码语法检查专家。你需要仔细检查代码的语法正确性，包括：
1. 括号、引号、分号等基本语法
2. SQF 语言规范
3. Arma 3 特定语法和函数调用
4. 常见错误和最佳实践

请以 JSON 格式返回检查结果，确保 JSON 格式正确。"""
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    "temperature": 0.1,
                    "max_tokens": max_tokens
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
    
    def _parse_response(self, response: str, lines: List[str]) -> Tuple[SyntaxCheckStatus, List[SyntaxIssue]]:
        """解析 LLM 响应"""
        issues = []
        status = SyntaxCheckStatus.PASSED
        
        try:
            # 尝试提取 JSON 部分
            json_match = re.search(r'\{.*\}', response, re.DOTALL)
            if json_match:
                json_str = json_match.group(0)
                data = json.loads(json_str)
                
                # 解析状态
                status_str = data.get('status', 'passed').lower()
                if status_str == 'failed' or status_str == 'error':
                    status = SyntaxCheckStatus.FAILED
                elif status_str == 'passed':
                    status = SyntaxCheckStatus.PASSED
                else:
                    status = SyntaxCheckStatus.ERROR
                
                # 解析问题
                for issue_data in data.get('issues', []):
                    issue = SyntaxIssue(
                        line=issue_data.get('line', 0),
                        column=issue_data.get('column'),
                        severity=issue_data.get('severity', 'error'),
                        message=issue_data.get('message', ''),
                        code_snippet=issue_data.get('code_snippet', ''),
                        suggestion=issue_data.get('suggestion', '')
                    )
                    issues.append(issue)
                    
                    # 如果代码片段为空，尝试从行号获取
                    if not issue.code_snippet and 0 < issue.line <= len(lines):
                        issue.code_snippet = lines[issue.line - 1].strip()
        
        except json.JSONDecodeError as e:
            # 如果 JSON 解析失败，尝试从文本中提取信息
            print(f"JSON 解析失败，尝试文本解析: {e}")
            status = SyntaxCheckStatus.ERROR
            # 可以添加文本解析逻辑
        
        except Exception as e:
            print(f"解析响应时出错: {e}")
            status = SyntaxCheckStatus.ERROR
        
        return status, issues

# ============================================================================
# 报告生成器
# ============================================================================

class ReportGenerator:
    """生成检查报告"""
    
    def __init__(self, output_file: str = "arma3_syntax_check_report.md"):
        self.output_file = output_file
    
    def generate_report(self, results: List[FileSyntaxCheck]) -> str:
        """生成 Markdown 报告"""
        report = f"""# Arma 3 语法检查报告

生成时间: {time.strftime('%Y-%m-%d %H:%M:%S')}

## 统计信息

- **总文件数**: {len(results)}
- **已检查**: {sum(1 for r in results if r.status != SyntaxCheckStatus.PENDING)}
- **通过**: {sum(1 for r in results if r.status == SyntaxCheckStatus.PASSED)}
- **失败**: {sum(1 for r in results if r.status == SyntaxCheckStatus.FAILED)}
- **错误**: {sum(1 for r in results if r.status == SyntaxCheckStatus.ERROR)}
- **跳过**: {sum(1 for r in results if r.status == SyntaxCheckStatus.SKIPPED)}

## 详细结果

"""
        
        # 按状态分组
        passed_files = [r for r in results if r.status == SyntaxCheckStatus.PASSED]
        failed_files = [r for r in results if r.status == SyntaxCheckStatus.FAILED]
        error_files = [r for r in results if r.status == SyntaxCheckStatus.ERROR]
        
        # 失败的文件
        if failed_files:
            report += f"\n### ❌ 语法错误文件 ({len(failed_files)})\n\n"
            for result in failed_files:
                report += self._format_file_result(result)
        
        # 检查错误的文件
        if error_files:
            report += f"\n### ⚠️ 检查错误文件 ({len(error_files)})\n\n"
            for result in error_files:
                report += f"**{result.file_path}**\n\n"
                report += f"错误: {result.error_message}\n\n"
                report += "---\n\n"
        
        # 通过的文件（可选，如果文件不多）
        if len(results) < 50 and passed_files:
            report += f"\n### ✅ 通过检查的文件 ({len(passed_files)})\n\n"
            for result in passed_files:
                report += f"- `{result.file_path}` ({result.total_lines} 行, {result.check_time:.2f}秒)\n"
        
        return report
    
    def _format_file_result(self, result: FileSyntaxCheck) -> str:
        """格式化单个文件结果"""
        output = f"### {result.file_path}\n\n"
        output += f"**状态**: {result.status.value}\n\n"
        output += f"**总行数**: {result.total_lines}\n"
        output += f"**已检查行数**: {result.checked_lines}\n"
        if result.chunks_processed > 1:
            output += f"**分片数量**: {result.chunks_processed}\n"
        output += f"**检查时间**: {result.check_time:.2f}秒\n\n"
        
        if result.issues:
            output += f"**问题数**: {len(result.issues)}\n\n"
            output += "**问题列表**:\n\n"
            
            for issue in result.issues:
                severity_icon = {
                    'error': '🔴',
                    'warning': '🟡',
                    'info': '🔵'
                }.get(issue.severity, '⚪')
                
                output += f"{severity_icon} **行 {issue.line}**"
                if issue.column:
                    output += f" (列 {issue.column})"
                output += f": {issue.message}\n\n"
                
                if issue.code_snippet:
                    output += f"```sqf\n{issue.code_snippet}\n```\n\n"
                
                if issue.suggestion:
                    output += f"💡 **建议**: {issue.suggestion}\n\n"
        
        if result.error_message:
            output += f"**错误信息**: {result.error_message}\n\n"
        
        output += "---\n\n"
        return output
    
    def save_report(self, report: str):
        """保存报告到文件"""
        with open(self.output_file, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"\n报告已保存到: {self.output_file}")

# ============================================================================
# 主程序
# ============================================================================

def check_file(file_path: Path, scanner: FileScanner, checker: LMStudioChecker) -> FileSyntaxCheck:
    """检查单个文件"""
    print(f"检查: {file_path}")
    
    content = scanner.read_file(file_path)
    if content is None:
        result = FileSyntaxCheck(
            file_path=str(file_path),
            status=SyntaxCheckStatus.ERROR,
            error_message="无法读取文件"
        )
        return result
    
    return checker.check_syntax(file_path, content)

def main():
    parser = argparse.ArgumentParser(description='使用 LM Studio 检查 Arma 3 代码语法')
    parser.add_argument('--root', type=str, default=PROJECT_ROOT,
                       help='项目根目录（默认: addons/mcc_sandbox_mod）')
    parser.add_argument('--output', type=str, default='arma3_syntax_check_report.md',
                       help='输出报告文件（默认: arma3_syntax_check_report.md）')
    parser.add_argument('--max-workers', type=int, default=3,
                       help='并发检查线程数（默认: 3）')
    parser.add_argument('--limit', type=int, default=None,
                       help='限制检查的文件数量（用于测试）')
    parser.add_argument('--extensions', type=str, nargs='+',
                       default=['.sqf', '.hpp'],
                       help='要检查的文件扩展名（默认: .sqf .hpp）')
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("Arma 3 语法检查工具")
    print("=" * 60)
    print(f"\n项目根目录: {args.root}")
    print(f"输出文件: {args.output}")
    print(f"并发线程: {args.max_workers}")
    print(f"文件扩展名: {', '.join(args.extensions)}")
    
    # 更新全局配置
    global ARMA3_FILE_EXTENSIONS
    ARMA3_FILE_EXTENSIONS = set(args.extensions)
    
    # 初始化组件
    scanner = FileScanner(args.root)
    checker = LMStudioChecker()
    report_gen = ReportGenerator(args.output)
    
    # 扫描文件
    print("\n扫描文件...")
    files = scanner.scan_files()
    
    if args.limit:
        files = files[:args.limit]
        print(f"限制检查前 {args.limit} 个文件")
    
    print(f"找到 {len(files)} 个文件需要检查\n")
    
    if not files:
        print("没有找到需要检查的文件")
        return
    
    # 检查文件
    results = []
    
    if args.max_workers > 1:
        # 并发检查
        print(f"使用 {args.max_workers} 个线程并发检查...\n")
        with ThreadPoolExecutor(max_workers=args.max_workers) as executor:
            futures = {
                executor.submit(check_file, file_path, scanner, checker): file_path
                for file_path in files
            }
            
            for future in as_completed(futures):
                file_path = futures[future]
                try:
                    result = future.result()
                    results.append(result)
                    
                    status_icon = {
                        SyntaxCheckStatus.PASSED: '✅',
                        SyntaxCheckStatus.FAILED: '❌',
                        SyntaxCheckStatus.ERROR: '⚠️',
                        SyntaxCheckStatus.SKIPPED: '⏭️'
                    }.get(result.status, '❓')
                    
                    print(f"{status_icon} {file_path.name}: {result.status.value}")
                    if result.issues:
                        print(f"   发现 {len(result.issues)} 个问题")
                except Exception as e:
                    print(f"❌ {file_path}: 检查出错 - {e}")
                    results.append(FileSyntaxCheck(
                        file_path=str(file_path),
                        status=SyntaxCheckStatus.ERROR,
                        error_message=str(e)
                    ))
    else:
        # 串行检查
        print("串行检查文件...\n")
        for file_path in files:
            result = check_file(file_path, scanner, checker)
            results.append(result)
            
            status_icon = {
                SyntaxCheckStatus.PASSED: '✅',
                SyntaxCheckStatus.FAILED: '❌',
                SyntaxCheckStatus.ERROR: '⚠️',
                SyntaxCheckStatus.SKIPPED: '⏭️'
            }.get(result.status, '❓')
            
            print(f"{status_icon} {file_path.name}: {result.status.value}")
            if result.issues:
                print(f"   发现 {len(result.issues)} 个问题")
    
    # 生成报告
    print("\n生成报告...")
    report = report_gen.generate_report(results)
    report_gen.save_report(report)
    
    # 打印摘要
    print("\n" + "=" * 60)
    print("检查完成")
    print("=" * 60)
    print(f"总文件数: {len(results)}")
    print(f"通过: {sum(1 for r in results if r.status == SyntaxCheckStatus.PASSED)}")
    print(f"失败: {sum(1 for r in results if r.status == SyntaxCheckStatus.FAILED)}")
    print(f"错误: {sum(1 for r in results if r.status == SyntaxCheckStatus.ERROR)}")
    print(f"\n详细报告请查看: {args.output}")

if __name__ == "__main__":
    main()

