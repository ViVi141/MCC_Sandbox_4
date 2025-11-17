#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
检查项目中所有文件的括号嵌套是否正确
支持圆括号 ()、方括号 []、花括号 {}
"""

import re
from pathlib import Path
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
from enum import Enum
import argparse

# ============================================================================
# 配置
# ============================================================================

PROJECT_ROOT = "addons/mcc_sandbox_mod"

# 要检查的文件扩展名
CODE_FILE_EXTENSIONS = {'.sqf', '.hpp', '.cpp', '.h', '.ext', '.hpp'}

# 排除的目录
EXCLUDE_DIRS = {'.git', 'node_modules', '__pycache__', '.vscode', '.idea'}

# ============================================================================
# 数据模型
# ============================================================================

class BracketType(Enum):
    """括号类型"""
    PARENTHESIS = "()"  # 圆括号
    SQUARE = "[]"       # 方括号
    CURLY = "{}"        # 花括号

@dataclass
class BracketIssue:
    """括号问题"""
    line: int
    column: int
    bracket_type: BracketType
    issue_type: str  # "unclosed", "unopened", "mismatch"
    message: str
    code_snippet: str

@dataclass
class FileBracketCheck:
    """文件括号检查结果"""
    file_path: str
    total_lines: int
    issues: List[BracketIssue] = None
    has_errors: bool = False
    
    def __post_init__(self):
        if self.issues is None:
            self.issues = []

# ============================================================================
# 括号检查器
# ============================================================================

class BracketChecker:
    """括号检查器"""
    
    def __init__(self):
        # 定义括号对
        self.brackets = {
            '(': (')', BracketType.PARENTHESIS),
            '[': (']', BracketType.SQUARE),
            '{': ('}', BracketType.CURLY),
        }
        self.closing_brackets = {')': '(', ']': '[', '}': '{'}
    
    def check_file(self, file_path: Path) -> FileBracketCheck:
        """检查文件的括号"""
        try:
            # 读取文件
            content = self._read_file(file_path)
            if content is None:
                return FileBracketCheck(
                    file_path=str(file_path),
                    total_lines=0,
                    has_errors=True
                )
            
            lines = content.split('\n')
            result = FileBracketCheck(
                file_path=str(file_path),
                total_lines=len(lines)
            )
            
            # 检查括号
            result.issues = self._check_brackets(lines)
            result.has_errors = len(result.issues) > 0
        
        except Exception as e:
            result = FileBracketCheck(
                file_path=str(file_path),
                total_lines=0,
                has_errors=True
            )
            result.issues.append(BracketIssue(
                line=0,
                column=0,
                bracket_type=BracketType.PARENTHESIS,
                issue_type="error",
                message=f"检查文件时出错: {e}",
                code_snippet=""
            ))
        
        return result
    
    def _read_file(self, file_path: Path) -> Optional[str]:
        """读取文件内容"""
        encodings = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
        
        for encoding in encodings:
            try:
                with open(file_path, 'r', encoding=encoding, errors='ignore') as f:
                    return f.read()
            except Exception:
                continue
        
        return None
    
    def _check_brackets(self, lines: List[str]) -> List[BracketIssue]:
        """检查括号匹配"""
        issues = []
        
        # 使用栈来跟踪括号
        stack = []  # [(line, col, char, bracket_type), ...]
        
        for line_num, line in enumerate(lines, 1):
            # 处理字符串和注释
            processed_line, string_ranges, comment_ranges = self._process_line(line)
            
            for col, char in enumerate(processed_line, 1):
                # 检查是否在字符串或注释中
                if self._is_in_string_or_comment(col, string_ranges, comment_ranges):
                    continue
                
                # 检查开括号
                if char in self.brackets:
                    closing, bracket_type = self.brackets[char]
                    stack.append((line_num, col, char, bracket_type))
                
                # 检查闭括号
                elif char in self.closing_brackets:
                    expected_opening = self.closing_brackets[char]
                    
                    if not stack:
                        # 未匹配的闭括号
                        bracket_type = self._get_bracket_type(char)
                        issues.append(BracketIssue(
                            line=line_num,
                            column=col,
                            bracket_type=bracket_type,
                            issue_type="unopened",
                            message=f"未匹配的闭括号 '{char}'",
                            code_snippet=line.strip()
                        ))
                    else:
                        # 检查是否匹配
                        prev_line, prev_col, prev_char, prev_type = stack.pop()
                        if prev_char != expected_opening:
                            # 括号类型不匹配
                            issues.append(BracketIssue(
                                line=line_num,
                                column=col,
                                bracket_type=prev_type,
                                issue_type="mismatch",
                                message=f"括号类型不匹配: 期望 '{self.brackets[prev_char][0]}'，但找到 '{char}'（开括号在第 {prev_line} 行第 {prev_col} 列）",
                                code_snippet=line.strip()
                            ))
                            # 也记录开括号位置
                            issues.append(BracketIssue(
                                line=prev_line,
                                column=prev_col,
                                bracket_type=prev_type,
                                issue_type="mismatch",
                                message=f"括号类型不匹配: 开括号 '{prev_char}' 在第 {prev_line} 行第 {prev_col} 列",
                                code_snippet=lines[prev_line - 1].strip()
                            ))
        
        # 检查未闭合的括号
        for line_num, col, char, bracket_type in stack:
            closing = self.brackets[char][0]
            issues.append(BracketIssue(
                line=line_num,
                column=col,
                bracket_type=bracket_type,
                issue_type="unclosed",
                message=f"未闭合的括号 '{char}'（期望 '{closing}'）",
                code_snippet=lines[line_num - 1].strip()
            ))
        
        return issues
    
    def _process_line(self, line: str) -> Tuple[str, List[Tuple[int, int]], List[Tuple[int, int]]]:
        """处理行，识别字符串和注释，返回处理后的行和范围"""
        processed = []
        string_ranges = []
        comment_ranges = []
        
        i = 0
        in_string = False
        string_char = None
        string_start = None
        
        while i < len(line):
            char = line[i]
            
            # 检查字符串
            if not in_string:
                if char in ['"', "'"]:
                    in_string = True
                    string_char = char
                    string_start = i
                    processed.append(' ') 
                elif char == '/' and i + 1 < len(line) and line[i + 1] == '/':
                    # 单行注释
                    comment_start = i
                    comment_ranges.append((comment_start, len(line)))
                    break
                else:
                    processed.append(char)
            else:
                # 在字符串中
                if char == string_char:
                    # 检查是否是转义
                    if i > 0 and line[i - 1] == '\\':
                        processed.append(char)
                    else:
                        # 字符串结束
                        in_string = False
                        string_ranges.append((string_start, i + 1))
                        string_char = None
                        string_start = None
                        processed.append(' ')  # 用空格替换字符串内容
                else:
                    processed.append(' ')  # 用空格替换字符串内容
            
            i += 1
        
        # 如果字符串未闭合
        if in_string:
            string_ranges.append((string_start, len(line)))
        
        return ''.join(processed), string_ranges, comment_ranges
    
    def _is_in_string_or_comment(self, col: int, string_ranges: List[Tuple[int, int]], 
                                 comment_ranges: List[Tuple[int, int]]) -> bool:
        """检查列是否在字符串或注释中（1-based）"""
        col_0based = col - 1
        
        for start, end in string_ranges:
            if start <= col_0based < end:
                return True
        
        for start, end in comment_ranges:
            if start <= col_0based < end:
                return True
        
        return False
    
    def _get_bracket_type(self, char: str) -> BracketType:
        """获取括号类型"""
        if char in ['(', ')']:
            return BracketType.PARENTHESIS
        elif char in ['[', ']']:
            return BracketType.SQUARE
        elif char in ['{', '}']:
            return BracketType.CURLY
        return BracketType.PARENTHESIS

# ============================================================================
# 文件扫描器
# ============================================================================

class FileScanner:
    """扫描项目文件"""
    
    def __init__(self, root_dir: str = PROJECT_ROOT):
        self.root_dir = Path(root_dir)
    
    def scan_files(self) -> List[Path]:
        """扫描所有代码文件"""
        files = []
        
        if not self.root_dir.exists():
            print(f"错误: 项目根目录不存在: {self.root_dir}")
            return files
        
        for file_path in self.root_dir.rglob('*'):
            if file_path.is_file():
                # 跳过排除的目录
                if any(part in EXCLUDE_DIRS for part in file_path.parts):
                    continue
                
                # 检查扩展名
                if file_path.suffix.lower() in CODE_FILE_EXTENSIONS:
                    files.append(file_path)
        
        return sorted(files)

# ============================================================================
# 报告生成器
# ============================================================================

class ReportGenerator:
    """生成检查报告"""
    
    def __init__(self, output_file: str = "bracket_check_report.md"):
        self.output_file = output_file
    
    def generate_report(self, results: List[FileBracketCheck]) -> str:
        """生成 Markdown 报告"""
        total_files = len(results)
        files_with_issues = [r for r in results if r.has_errors]
        total_issues = sum(len(r.issues) for r in results)
        
        report = f"""# 括号嵌套检查报告

生成时间: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 统计信息

- **总文件数**: {total_files}
- **有问题的文件**: {len(files_with_issues)}
- **总问题数**: {total_issues}

## 详细结果

"""
        
        if not files_with_issues:
            report += "\n✅ **所有文件的括号嵌套都正确！**\n"
            return report
        
        # 按问题数量排序
        files_with_issues.sort(key=lambda x: len(x.issues), reverse=True)
        
        for result in files_with_issues:
            report += self._format_file_result(result)
        
        return report
    
    def _format_file_result(self, result: FileBracketCheck) -> str:
        """格式化单个文件结果"""
        output = f"### {result.file_path}\n\n"
        output += f"**总行数**: {result.total_lines}\n"
        output += f"**问题数**: {len(result.issues)}\n\n"
        
        # 按行号排序
        result.issues.sort(key=lambda x: (x.line, x.column))
        
        # 按问题类型分组
        unclosed = [i for i in result.issues if i.issue_type == "unclosed"]
        unopened = [i for i in result.issues if i.issue_type == "unopened"]
        mismatch = [i for i in result.issues if i.issue_type == "mismatch"]
        
        if unclosed:
            output += "#### ❌ 未闭合的括号\n\n"
            for issue in unclosed:
                output += self._format_issue(issue)
        
        if unopened:
            output += "#### ❌ 未匹配的闭括号\n\n"
            for issue in unopened:
                output += self._format_issue(issue)
        
        if mismatch:
            output += "#### ❌ 括号类型不匹配\n\n"
            for issue in mismatch:
                output += self._format_issue(issue)
        
        output += "---\n\n"
        return output
    
    def _format_issue(self, issue: BracketIssue) -> str:
        """格式化单个问题"""
        icon = {
            "unclosed": "🔴",
            "unopened": "🟡",
            "mismatch": "🟠"
        }.get(issue.issue_type, "⚪")
        
        bracket_name = {
            BracketType.PARENTHESIS: "圆括号",
            BracketType.SQUARE: "方括号",
            BracketType.CURLY: "花括号"
        }.get(issue.bracket_type, "括号")
        
        output = f"{icon} **行 {issue.line}，列 {issue.column}** ({bracket_name})\n\n"
        output += f"**问题**: {issue.message}\n\n"
        
        if issue.code_snippet:
            output += f"**代码**:\n```sqf\n{issue.code_snippet}\n```\n\n"
        
        return output
    
    def save_report(self, report: str):
        """保存报告到文件"""
        with open(self.output_file, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"\n报告已保存到: {self.output_file}")

# ============================================================================
# 主程序
# ============================================================================

def main():
    parser = argparse.ArgumentParser(description='检查项目中所有文件的括号嵌套')
    parser.add_argument('--root', type=str, default=PROJECT_ROOT,
                       help='项目根目录（默认: addons/mcc_sandbox_mod）')
    parser.add_argument('--output', type=str, default='bracket_check_report.md',
                       help='输出报告文件（默认: bracket_check_report.md）')
    parser.add_argument('--extensions', type=str, nargs='+',
                       default=['.sqf', '.hpp'],
                       help='要检查的文件扩展名（默认: .sqf .hpp）')
    parser.add_argument('--limit', type=int, default=None,
                       help='限制检查的文件数量（用于测试）')
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("括号嵌套检查工具")
    print("=" * 60)
    print(f"\n项目根目录: {args.root}")
    print(f"输出文件: {args.output}")
    print(f"文件扩展名: {', '.join(args.extensions)}")
    
    # 更新全局配置
    global CODE_FILE_EXTENSIONS
    CODE_FILE_EXTENSIONS = set(args.extensions)
    
    # 初始化组件
    scanner = FileScanner(args.root)
    checker = BracketChecker()
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
    print("检查括号嵌套...\n")
    results = []
    
    for file_path in files:
        result = checker.check_file(file_path)
        results.append(result)
        
        if result.has_errors:
            print(f"[ERROR] {file_path.name}: {len(result.issues)} 个问题")
        else:
            print(f"[OK] {file_path.name}: 通过")
    
    # 生成报告
    print("\n生成报告...")
    report = report_gen.generate_report(results)
    report_gen.save_report(report)
    
    # 打印摘要
    print("\n" + "=" * 60)
    print("检查完成")
    print("=" * 60)
    total_issues = sum(len(r.issues) for r in results)
    files_with_issues = sum(1 for r in results if r.has_errors)
    print(f"总文件数: {len(results)}")
    print(f"有问题的文件: {files_with_issues}")
    print(f"总问题数: {total_issues}")
    print(f"\n详细报告请查看: {args.output}")

if __name__ == "__main__":
    main()

