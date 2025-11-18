#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SQF 文件括号嵌套修复脚本

检测和修复 SQF 文件中的括号嵌套问题：
1. 括号匹配检查（圆括号、方括号、花括号）
2. 重复的 if 语句嵌套
3. 不正确的缩进和嵌套结构
"""

import re
from pathlib import Path
from typing import List, Dict, Optional
from datetime import datetime
import time


class SQFBracketFixer:
    """SQF 文件括号嵌套修复器"""
    
    def __init__(self, project_root: str = "addons/mcc_sandbox_mod", 
                 backup_dir: str = "backups", dry_run: bool = False):
        """
        初始化修复器
        
        Args:
            project_root: 项目根目录
            backup_dir: 备份目录
            dry_run: 是否为试运行（不实际修改文件）
        """
        self.project_root = Path(project_root)
        self.backup_dir = Path(backup_dir)
        self.dry_run = dry_run
        self.stats = {
            "total_files": 0,
            "files_with_issues": 0,
            "bracket_mismatches": 0,
            "duplicate_ifs": 0,
            "fixed_files": 0,
            "errors": 0
        }
        self.log = []
        self.issues = []  # 存储发现的问题
        
    def log_message(self, message: str, level: str = "INFO"):
        """记录日志消息"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message}"
        self.log.append(log_entry)
        print(log_entry)
    
    def check_bracket_balance(self, content: str) -> List[Dict]:
        """
        检查括号是否匹配
        
        Returns:
            不匹配的括号位置列表
        """
        issues = []
        stack = []
        
        # 定义括号对
        brackets = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        closing_brackets = {v: k for k, v in brackets.items()}
        
        # 全文件扫描（但限制最大行数，避免超大文件卡住）
        lines = content.split('\n')
        max_lines = 50000  # 最多检查50000行
        if len(lines) > max_lines:
            lines = lines[:max_lines]
        
        in_string = False
        string_char = None
        in_comment = False
        
        for line_num, line in enumerate(lines, 1):
            i = 0
            while i < len(line):
                char = line[i]
                
                # 处理字符串
                if not in_comment:
                    if char in ['"', "'"]:
                        # 检查是否是转义的引号（需要检查前一个字符是否是反斜杠，且不是转义的反斜杠）
                        is_escaped = False
                        if i > 0 and line[i-1] == '\\':
                            # 检查是否是转义的反斜杠（即 \\）
                            backslash_count = 0
                            for k in range(i-1, -1, -1):
                                if line[k] == '\\':
                                    backslash_count += 1
                                else:
                                    break
                            # 如果反斜杠数量是奇数，则引号被转义
                            is_escaped = (backslash_count % 2 == 1)
                        
                        if not is_escaped:
                            if not in_string:
                                in_string = True
                                string_char = char
                            elif char == string_char:
                                in_string = False
                                string_char = None
                        i += 1
                        continue
                
                # 处理注释
                if not in_string:
                    if i < len(line) - 1 and line[i:i+2] == '//':
                        break  # 单行注释，跳过该行剩余部分
                    if i < len(line) - 1 and line[i:i+2] == '/*':
                        in_comment = True
                        i += 2
                        continue
                    if in_comment and i < len(line) - 1 and line[i:i+2] == '*/':
                        in_comment = False
                        i += 2
                        continue
                
                if in_string or in_comment:
                    i += 1
                    continue
                
                # 检查开括号
                if char in brackets:
                    stack.append({
                        'type': char,
                        'line': line_num,
                        'col': i + 1,
                        'expected': brackets[char]
                    })
                # 检查闭括号
                elif char in closing_brackets:
                    if not stack:
                        issues.append({
                            'type': 'unexpected_closing',
                            'bracket': char,
                            'line': line_num,
                            'col': i + 1
                        })
                    else:
                        last = stack.pop()
                        if last['expected'] != char:
                            issues.append({
                                'type': 'mismatch',
                                'opening': last,
                                'closing': {
                                    'bracket': char,
                                    'line': line_num,
                                    'col': i + 1
                                }
                            })
                
                i += 1
        
        # 检查未闭合的括号
        for unclosed in stack:
            issues.append({
                'type': 'unclosed',
                'bracket': unclosed['type'],
                'line': unclosed['line'],
                'col': unclosed['col']
            })
        
        return issues
    
    def find_duplicate_if_nesting(self, content: str) -> List[Dict]:
        """
        查找重复的 if 语句嵌套
        
        例如：
        if (!(isNull _var)) then {
        if (!(isNull _var)) then {
            // code
        };
        };
        """
        issues = []
        lines = content.split('\n')
        
        # 性能优化：如果文件太大，限制搜索范围（避免卡住）
        max_search_lines = 20000  # 最多搜索20000行
        search_lines = lines[:max_search_lines] if len(lines) > max_search_lines else lines
        
        # 全文件扫描（但限制搜索范围）
        i = 0
        max_iterations = len(search_lines) * 2  # 防止无限循环
        iteration_count = 0
        
        while i < len(search_lines) - 1 and iteration_count < max_iterations:
            iteration_count += 1
            line = search_lines[i].strip()
            
            # 查找 if 语句（支持多行格式）
            if_match = re.match(r'^if\s*\((.+?)\)\s*then\s*\{', line)
            if if_match:
                condition = if_match.group(1).strip()
                
                # 检查下一行是否也是相同的 if 语句
                if i + 1 < len(search_lines):
                    next_line = search_lines[i + 1].strip()
                    next_if_match = re.match(r'^if\s*\((.+?)\)\s*then\s*\{', next_line)
                    
                    if next_if_match:
                        next_condition = next_if_match.group(1).strip()
                        # 比较条件（忽略空白差异）
                        if self._normalize_condition(condition) == self._normalize_condition(next_condition):
                            # 找到重复的 if，查找对应的闭合括号
                            brace_count = 2  # 两个开括号
                            first_close_line = None
                            
                            # 查找第一个闭合 };（限制搜索范围，避免卡住）
                            max_search_ahead = min(500, len(search_lines) - i - 2)  # 最多向前搜索500行
                            for j in range(i + 2, i + 2 + max_search_ahead):
                                if j >= len(search_lines):
                                    break
                                line_content = search_lines[j]
                                brace_count += line_content.count('{') - line_content.count('}')
                                
                                # 检查是否找到第一个闭合
                                if brace_count == 1 and '};' in line_content:
                                    first_close_line = j
                                    # 检查下一行是否是另一个闭合
                                    if j + 1 < len(search_lines):
                                        next_close = search_lines[j + 1].strip()
                                        if next_close == '};' or (next_close and '};' in next_close):
                                            issues.append({
                                                'type': 'duplicate_if',
                                                'start_line': i + 1,
                                                'end_line': j + 2,
                                                'condition': condition,
                                                'lines': lines[i:min(j+3, len(lines))]
                                            })
                                            i = j + 2
                                            break
                                    break
                            
                            if first_close_line is not None:
                                continue
            
            i += 1
        
        return issues
    
    def _normalize_condition(self, condition: str) -> str:
        """标准化条件字符串以便比较"""
        # 移除所有空白字符
        return re.sub(r'\s+', '', condition)
    
    def fix_bracket_issues(self, content: str, issues: List[Dict]) -> str:
        """
        修复括号不匹配问题
        
        Args:
            content: 文件内容
            issues: 括号问题列表
            
        Returns:
            修复后的内容
        """
        if not issues:
            return content
        
        lines = content.split('\n')
        # 按行号从后往前排序，避免修改影响行号
        sorted_issues = sorted(issues, key=lambda x: (x.get('line', 0), x.get('col', 0)), reverse=True)
        
        for issue in sorted_issues:
            issue_type = issue.get('type')
            line_num = issue.get('line', 0) - 1  # 转换为0-based索引
            col_num = issue.get('col', 0) - 1
            
            if line_num < 0 or line_num >= len(lines):
                continue
            
            line = lines[line_num]
            
            if issue_type == 'unexpected_closing':
                # 删除意外的闭合括号
                bracket = issue.get('bracket', '')
                if col_num < len(line):
                    # 检查是否是独立的闭合括号（如 }; 或 ] 或 )）
                    char_at_pos = line[col_num] if col_num < len(line) else ''
                    if char_at_pos == bracket:
                        # 删除这个字符
                        if bracket == '}' and col_num + 1 < len(line) and line[col_num + 1] == ';':
                            # 处理 }; 的情况
                            lines[line_num] = line[:col_num] + line[col_num + 2:].lstrip()
                        else:
                            # 单独删除括号
                            lines[line_num] = line[:col_num] + line[col_num + 1:].lstrip()
                        self.log_message(
                            f"删除意外的闭合括号 {bracket} 在行 {line_num + 1}, 列 {col_num + 1}",
                            "INFO"
                        )
            
            elif issue_type == 'unclosed':
                # 添加缺失的闭合括号
                bracket = issue.get('bracket', '')
                closing_bracket = {
                    '(': ')',
                    '[': ']',
                    '{': '}'
                }.get(bracket, '')
                
                if closing_bracket:
                    # 在文件末尾或当前块的末尾添加闭合括号
                    # 先尝试在当前行末尾添加
                    if bracket == '{':
                        # 对于花括号，检查是否是 if/while/for 等语句
                        # 如果是，添加 };
                        if 'then {' in line or 'do {' in line:
                            # 在行末添加 };
                            if not line.rstrip().endswith(';'):
                                lines[line_num] = line.rstrip() + ';'
                            # 在下一行添加 }
                            if line_num + 1 < len(lines):
                                # 检查下一行是否已有闭合
                                next_line = lines[line_num + 1].strip()
                                if not next_line.startswith('}'):
                                    # 插入闭合括号行
                                    indent = len(line) - len(line.lstrip())
                                    lines.insert(line_num + 1, ' ' * indent + closing_bracket + ';')
                            else:
                                # 文件末尾，添加闭合括号
                                indent = len(line) - len(line.lstrip())
                                lines.append(' ' * indent + closing_bracket + ';')
                        else:
                            # 普通花括号，添加 }
                            if line_num + 1 < len(lines):
                                next_line = lines[line_num + 1].strip()
                                if not next_line.startswith('}'):
                                    indent = len(line) - len(line.lstrip())
                                    lines.insert(line_num + 1, ' ' * indent + closing_bracket)
                            else:
                                indent = len(line) - len(line.lstrip())
                                lines.append(' ' * indent + closing_bracket)
                    else:
                        # 对于圆括号和方括号，在行末添加
                        if col_num < len(line):
                            # 在指定位置后添加闭合括号
                            lines[line_num] = line[:col_num + 1] + closing_bracket + line[col_num + 1:]
                        else:
                            lines[line_num] = line + closing_bracket
                    
                    self.log_message(
                        f"添加缺失的闭合括号 {closing_bracket} 在行 {line_num + 1}",
                        "INFO"
                    )
            
            elif issue_type == 'mismatch':
                # 替换不匹配的括号类型
                opening = issue.get('opening', {})
                closing = issue.get('closing', {})
                expected_closing = opening.get('expected', '')
                actual_closing = closing.get('bracket', '')
                
                if expected_closing and actual_closing and col_num < len(line):
                    # 替换闭合括号
                    char_at_pos = line[col_num] if col_num < len(line) else ''
                    if char_at_pos == actual_closing:
                        # 替换为正确的括号
                        if actual_closing == '}' and col_num + 1 < len(line) and line[col_num + 1] == ';':
                            # 处理 }; 的情况
                            lines[line_num] = line[:col_num] + expected_closing + line[col_num + 2:]
                        else:
                            lines[line_num] = line[:col_num] + expected_closing + line[col_num + 1:]
                        self.log_message(
                            f"替换不匹配的括号 {actual_closing} -> {expected_closing} 在行 {line_num + 1}, 列 {col_num + 1}",
                            "INFO"
                        )
        
        return '\n'.join(lines)
    
    def fix_duplicate_if_nesting(self, content: str, issue: Dict) -> str:
        """
        修复重复的 if 语句嵌套
        
        移除重复的 if 语句，只保留一个
        """
        lines = content.split('\n')
        start_idx = issue['start_line'] - 1
        end_idx = issue['end_line'] - 1
        
        if start_idx >= len(lines) or end_idx >= len(lines):
            return content
        
        # 找到第一个 if 的结束位置（第一个 };）
        first_close_idx = None
        brace_count = 0
        for i in range(start_idx, min(end_idx + 1, len(lines))):
            line = lines[i]
            brace_count += line.count('{') - line.count('}')
            if brace_count == 1 and '};' in line:
                first_close_idx = i
                break
        
        if first_close_idx is None:
            # 如果找不到第一个闭合，尝试更宽松的匹配
            for i in range(start_idx + 2, min(end_idx + 1, len(lines))):
                if '};' in lines[i]:
                    first_close_idx = i
                    break
        
        if first_close_idx is None:
            return content
        
        # 构建新内容
        new_lines = []
        
        # 保留第一个 if 之前的行
        new_lines.extend(lines[:start_idx])
        
        # 添加第一个 if 语句
        new_lines.append(lines[start_idx])
        
        # 跳过第二个 if，直接添加内容（去除一层缩进）
        for i in range(start_idx + 2, first_close_idx + 1):
            line = lines[i]
            # 减少一层缩进（智能检测缩进方式）
            # 先尝试移除tab
            if line.startswith('\t'):
                line = line[1:]
            # 再尝试移除空格（4的倍数）
            elif line.startswith('    '):  # 至少4个空格
                # 计算开头的空格数
                space_count = 0
                for char in line:
                    if char == ' ':
                        space_count += 1
                    else:
                        break
                # 移除4个空格（或所有空格如果少于4个）
                remove_count = min(4, space_count)
                line = line[remove_count:]
            new_lines.append(line)
        
        # 添加第一个闭合 };
        new_lines.append(lines[first_close_idx])
        
        # 跳过第二个闭合 };（first_close_idx + 1），添加剩余内容
        if first_close_idx + 1 < len(lines):
            # 跳过第二个闭合行，从 first_close_idx + 2 开始
            if first_close_idx + 2 < len(lines):
                new_lines.extend(lines[first_close_idx + 2:])
        
        return '\n'.join(new_lines)
    
    def read_file_with_encoding(self, file_path: Path) -> Optional[str]:
        """
        尝试使用多种编码读取文件
        
        Returns:
            文件内容，如果无法读取则返回 None
        """
        encodings = ['utf-8', 'utf-8-sig', 'latin-1', 'cp1252', 'iso-8859-1']
        
        for encoding in encodings:
            try:
                with open(file_path, 'r', encoding=encoding) as f:
                    return f.read()
            except (UnicodeDecodeError, UnicodeError):
                continue
            except Exception as e:
                self.log_message(f"读取文件 {file_path} 时出错 ({encoding}): {e}", "WARNING")
                continue
        
        self.log_message(f"无法读取文件 {file_path}（尝试了所有编码）", "ERROR")
        return None
    
    def analyze_file(self, file_path: Path) -> Dict:
        """
        分析单个文件
        
        Returns:
            分析结果字典
        """
        content = self.read_file_with_encoding(file_path)
        if content is None:
            return None
        
        result = {
            'file': str(file_path.relative_to(self.project_root)),
            'bracket_issues': [],
            'duplicate_if_issues': [],
            'needs_fix': False
        }
        
        # 检查括号匹配
        bracket_issues = self.check_bracket_balance(content)
        if bracket_issues:
            result['bracket_issues'] = bracket_issues
            result['needs_fix'] = True
            self.stats['bracket_mismatches'] += len(bracket_issues)
        
        # 检查重复的 if 嵌套
        duplicate_ifs = self.find_duplicate_if_nesting(content)
        if duplicate_ifs:
            result['duplicate_if_issues'] = duplicate_ifs
            result['needs_fix'] = True
            self.stats['duplicate_ifs'] += len(duplicate_ifs)
        
        return result
    
    def fix_file(self, file_path: Path, analysis: Dict) -> bool:
        """
        修复文件中的问题
        
        Returns:
            True 如果成功，False 如果失败
        """
        content = self.read_file_with_encoding(file_path)
        if content is None:
            return False
        
        original_content = content
        
        # 修复括号不匹配问题（从后往前修复，避免行号变化）
        if analysis.get('bracket_issues'):
            content = self.fix_bracket_issues(content, analysis['bracket_issues'])
            self.log_message(
                f"修复括号问题: {file_path} ({len(analysis['bracket_issues'])} 个问题)",
                "INFO"
            )
        
        # 修复重复的 if 嵌套（从后往前修复，避免行号变化）
        for issue in sorted(analysis['duplicate_if_issues'], 
                           key=lambda x: x['start_line'], reverse=True):
            content = self.fix_duplicate_if_nesting(content, issue)
            self.log_message(
                f"修复重复 if 嵌套: {file_path} 行 {issue['start_line']}-{issue['end_line']}",
                "INFO"
            )
        
        # 如果内容有变化，写回文件
        if content != original_content:
            if not self.dry_run:
                try:
                    # 尝试使用UTF-8写入，如果失败则使用原始编码
                    with open(file_path, 'w', encoding='utf-8', errors='replace') as f:
                        f.write(content)
                    self.log_message(f"[成功] 已修复 {file_path}", "SUCCESS")
                    return True  # 实际修改了文件
                except Exception as e:
                    self.log_message(f"无法写入文件 {file_path}: {e}", "ERROR")
                    return False
            else:
                self.log_message(f"[试运行] 将修复 {file_path}", "INFO")
                return True  # 试运行模式，标记为将修复
        else:
            # 内容没有变化，说明没有需要修复的问题（或问题已修复）
            if analysis.get('duplicate_if_issues') or analysis.get('bracket_issues'):
                # 有问题但修复后内容未变化（可能是修复逻辑无法处理的情况）
                if analysis.get('bracket_issues'):
                    self.log_message(f"[警告] {file_path} 有括号问题但可能无法自动修复", "WARNING")
                if analysis.get('duplicate_if_issues'):
                    self.log_message(f"[警告] {file_path} 有重复if问题但修复失败", "WARNING")
            return False  # 没有实际修改文件
    
    def backup_file(self, file_path: Path) -> bool:
        """备份文件"""
        if self.dry_run:
            return True
        
        try:
            self.backup_dir.mkdir(parents=True, exist_ok=True)
            relative_path = file_path.relative_to(self.project_root)
            backup_path = self.backup_dir / relative_path
            backup_path.parent.mkdir(parents=True, exist_ok=True)
            import shutil
            shutil.copy2(file_path, backup_path)
            return True
        except Exception as e:
            self.log_message(f"备份文件失败 {file_path}: {e}", "ERROR")
            return False
    
    def scan_and_fix(self):
        """扫描并修复所有 SQF 文件"""
        self.log_message("开始扫描 SQF 文件...")
        
        # 查找所有 SQF 文件
        sqf_files = list(self.project_root.rglob('*.sqf'))
        self.stats['total_files'] = len(sqf_files)
        
        self.log_message(f"找到 {len(sqf_files)} 个 SQF 文件")
        
        # 分析每个文件（带进度显示）
        files_to_fix = []
        total = len(sqf_files)
        import sys
        
        for idx, file_path in enumerate(sqf_files, 1):
            # 每10个文件显示一次进度（更频繁的反馈）
            if idx % 10 == 0 or idx == total:
                percent = idx * 100 // total
                self.log_message(f"正在分析: {idx}/{total} ({percent}%) - {file_path.name[:50]}")
                sys.stdout.flush()  # 强制刷新输出
            
            try:
                start_time = time.time()
                analysis = self.analyze_file(file_path)
                elapsed = time.time() - start_time
                
                # 如果单个文件处理超过5秒，记录警告
                if elapsed > 5:
                    self.log_message(f"文件 {file_path.name} 处理耗时 {elapsed:.2f}秒", "WARNING")
                
                if analysis and analysis['needs_fix']:
                    files_to_fix.append((file_path, analysis))
                    self.stats['files_with_issues'] += 1
                    self.issues.append(analysis)
            except Exception as e:
                self.log_message(f"分析文件 {file_path} 时出错: {e}", "ERROR")
                self.stats['errors'] += 1
                continue
        
        self.log_message(f"分析完成，发现 {len(files_to_fix)} 个文件需要修复")
        
        # 修复文件
        if files_to_fix:
            self.log_message(f"开始修复 {len(files_to_fix)} 个文件...")
            for idx, (file_path, analysis) in enumerate(files_to_fix, 1):
                self.log_message(f"修复进度: {idx}/{len(files_to_fix)} - {file_path.name}")
                
                # 备份文件
                if not self.backup_file(file_path):
                    self.log_message(f"跳过文件 {file_path}（备份失败）", "WARNING")
                    continue
                
                # 修复文件
                fix_result = self.fix_file(file_path, analysis)
                if fix_result is True:
                    # 只有实际修改了文件才计入修复数
                    self.stats['fixed_files'] += 1
                elif fix_result is False:
                    # 没有修改文件（可能是没有需要修复的问题）
                    pass  # 不增加错误数，因为可能只是没有需要修复的问题
                else:
                    # 其他错误
                    self.stats['errors'] += 1
        else:
            self.log_message("没有需要修复的文件")
    
    def generate_report(self, report_path: str = "sqf_bracket_fix_report.md"):
        """生成修复报告"""
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write("# SQF 文件括号嵌套修复报告\n\n")
            f.write(f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            f.write("## 统计信息\n\n")
            f.write(f"- **总文件数**: {self.stats['total_files']}\n")
            f.write(f"- **有问题文件数**: {self.stats['files_with_issues']}\n")
            f.write(f"- **括号不匹配数**: {self.stats['bracket_mismatches']}\n")
            f.write(f"- **重复 if 嵌套数**: {self.stats['duplicate_ifs']}\n")
            f.write(f"- **已修复文件数**: {self.stats['fixed_files']}\n")
            f.write(f"- **错误数**: {self.stats['errors']}\n\n")
            
            if self.issues:
                f.write("## 详细问题列表\n\n")
                for issue in self.issues:
                    f.write(f"### {issue['file']}\n\n")
                    
                    if issue['bracket_issues']:
                        f.write("#### 括号不匹配问题\n\n")
                        for bracket_issue in issue['bracket_issues']:
                            issue_type = bracket_issue.get('type', 'unknown')
                            
                            # 根据问题类型获取行号和列号
                            if issue_type == 'mismatch':
                                opening = bracket_issue.get('opening', {})
                                closing = bracket_issue.get('closing', {})
                                line = opening.get('line', closing.get('line', '?'))
                                col = opening.get('col', closing.get('col', '?'))
                                f.write(f"- 行 {line}, 列 {col}: ")
                                f.write(f"括号不匹配 (开括号: {opening.get('type', '?')}, 闭括号: {closing.get('bracket', '?')})\n")
                            else:
                                line = bracket_issue.get('line', '?')
                                col = bracket_issue.get('col', '?')
                                bracket = bracket_issue.get('bracket', '?')
                                f.write(f"- 行 {line}, 列 {col}: ")
                                f.write(f"{issue_type} (括号: {bracket})\n")
                        f.write("\n")
                    
                    if issue['duplicate_if_issues']:
                        f.write("#### 重复 if 嵌套问题\n\n")
                        for dup_issue in issue['duplicate_if_issues']:
                            f.write(f"- 行 {dup_issue['start_line']}-{dup_issue['end_line']}: ")
                            f.write(f"条件: `{dup_issue['condition']}`\n")
                            f.write("\n**原始代码**:\n```sqf\n")
                            for line in dup_issue['lines']:
                                f.write(f"{line}\n")
                            f.write("```\n\n")
            
            f.write("\n## 日志\n\n")
            f.write("```\n")
            for log_entry in self.log:
                f.write(f"{log_entry}\n")
            f.write("```\n")
        
        self.log_message(f"报告已保存到 {report_path}")
    
    def run(self):
        """运行修复流程"""
        self.log_message("=" * 60)
        self.log_message("SQF 文件括号嵌套修复脚本")
        self.log_message("=" * 60)
        
        if self.dry_run:
            self.log_message("模式: 试运行（不会实际修改文件）")
        else:
            self.log_message("模式: 实际应用修复")
        
        # 扫描并修复
        self.scan_and_fix()
        
        # 打印统计信息
        self.log_message("=" * 60)
        self.log_message("统计信息:")
        self.log_message(f"  总文件数: {self.stats['total_files']}")
        self.log_message(f"  有问题文件数: {self.stats['files_with_issues']}")
        self.log_message(f"  括号不匹配数: {self.stats['bracket_mismatches']}")
        self.log_message(f"  重复 if 嵌套数: {self.stats['duplicate_ifs']}")
        self.log_message(f"  已修复文件数: {self.stats['fixed_files']}")
        self.log_message(f"  错误数: {self.stats['errors']}")
        self.log_message("=" * 60)
        
        # 生成报告
        self.generate_report()


def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description='修复 SQF 文件中的括号嵌套问题')
    parser.add_argument(
        '--project-root',
        default='addons/mcc_sandbox_mod',
        help='项目根目录（默认: addons/mcc_sandbox_mod）'
    )
    parser.add_argument(
        '--backup-dir',
        default='backups',
        help='备份目录（默认: backups）'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='试运行模式（不实际修改文件）'
    )
    
    args = parser.parse_args()
    
    fixer = SQFBracketFixer(
        project_root=args.project_root,
        backup_dir=args.backup_dir,
        dry_run=args.dry_run
    )
    
    fixer.run()


if __name__ == '__main__':
    main()

