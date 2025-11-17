#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Git 比对脚本：检查从注释状态变为非注释状态的行
用于检测不应该被取消注释的代码
"""

import subprocess
import re
import sys
from pathlib import Path
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import argparse

@dataclass
class UncommentedChange:
    """未注释变更数据模型"""
    file: str
    line_number: int
    old_line: str
    new_line: str
    context: List[str]

class GitDiffChecker:
    """Git 差异检查器"""
    
    def __init__(self, repo_path: str = "."):
        self.repo_path = Path(repo_path)
        self.comment_patterns = {
            '.sqf': r'^\s*//',  # SQF 文件：// 开头
            '.hpp': r'^\s*//',  # HPP 文件：// 开头
            '.cpp': r'^\s*//',  # CPP 文件：// 开头
            '.h': r'^\s*//',    # H 文件：// 开头
            '.py': r'^\s*#',    # Python 文件：# 开头
            '.js': r'^\s*//',   # JavaScript 文件：// 开头
            '.ts': r'^\s*//',   # TypeScript 文件：// 开头
        }
    
    def get_file_extension(self, file_path: str) -> str:
        """获取文件扩展名"""
        return Path(file_path).suffix.lower()
    
    def is_commented_line(self, line: str, file_path: str) -> bool:
        """检查行是否被注释"""
        ext = self.get_file_extension(file_path)
        pattern = self.comment_patterns.get(ext, r'^\s*//')
        return bool(re.match(pattern, line))
    
    def run_git_diff(self, base: str = "HEAD", target: str = None) -> str:
        """运行 git diff 命令"""
        if target is None:
            # 比较工作区和 HEAD
            cmd = ["git", "diff", "--no-color", base]
        else:
            # 比较两个提交
            cmd = ["git", "diff", "--no-color", base, target]
        
        try:
            result = subprocess.run(
                cmd,
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                encoding='utf-8',
                errors='ignore'
            )
            return result.stdout
        except Exception as e:
            print(f"错误: 无法运行 git diff: {e}")
            return ""
    
    def parse_diff(self, diff_output: str) -> List[Dict]:
        """解析 git diff 输出"""
        changes = []
        current_file = None
        current_hunk = None
        old_line_num = 0
        new_line_num = 0
        old_lines = []
        new_lines = []
        
        for line in diff_output.split('\n'):
            # 文件头
            if line.startswith('diff --git'):
                if current_file and current_hunk:
                    changes.append({
                        'file': current_file,
                        'hunk': current_hunk,
                        'old_lines': old_lines,
                        'new_lines': new_lines,
                        'old_start': old_line_num - len(old_lines),
                        'new_start': new_line_num - len(new_lines)
                    })
                old_lines = []
                new_lines = []
                old_line_num = 0
                new_line_num = 0
            
            # 文件路径
            elif line.startswith('---') or line.startswith('+++'):
                if line.startswith('+++'):
                    # 提取文件路径（去掉 b/ 前缀）
                    file_path = line[6:].strip()
                    if file_path != '/dev/null':
                        current_file = file_path
            
            # Hunk 头
            elif line.startswith('@@'):
                if current_file and current_hunk:
                    changes.append({
                        'file': current_file,
                        'hunk': current_hunk,
                        'old_lines': old_lines,
                        'new_lines': new_lines,
                        'old_start': old_line_num - len(old_lines),
                        'new_start': new_line_num - len(new_lines)
                    })
                
                # 解析 hunk 头：@@ -old_start,old_count +new_start,new_count @@
                match = re.match(r'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@', line)
                if match:
                    old_line_num = int(match.group(1))
                    new_line_num = int(match.group(3))
                    old_lines = []
                    new_lines = []
                    current_hunk = line
            
            # 删除的行（- 开头，但不在注释中）
            elif line.startswith('-') and not line.startswith('---'):
                content = line[1:]
                old_lines.append(('removed', content))
                old_line_num += 1
            
            # 添加的行（+ 开头，但不在注释中）
            elif line.startswith('+') and not line.startswith('+++'):
                content = line[1:]
                new_lines.append(('added', content))
                new_line_num += 1
            
            # 上下文行（空格开头）
            elif line.startswith(' '):
                old_lines.append(('context', line[1:]))
                new_lines.append(('context', line[1:]))
                old_line_num += 1
                new_line_num += 1
        
        # 处理最后一个 hunk
        if current_file and current_hunk:
            changes.append({
                'file': current_file,
                'hunk': current_hunk,
                'old_lines': old_lines,
                'new_lines': new_lines,
                'old_start': old_line_num - len(old_lines),
                'new_start': new_line_num - len(new_lines)
            })
        
        return changes
    
    def find_uncommented_changes(self, base: str = "HEAD", target: str = None) -> List[UncommentedChange]:
        """查找从注释变为非注释的变更"""
        diff_output = self.run_git_diff(base, target)
        if not diff_output:
            return []
        
        changes = self.parse_diff(diff_output)
        uncommented_changes = []
        
        for change in changes:
            file_path = change['file']
            if not file_path:
                continue
            
            old_lines = change['old_lines']
            new_lines = change['new_lines']
            old_start = change['old_start']
            new_start = change['new_start']
            
            # 对齐新旧行进行比较
            old_idx = 0
            new_idx = 0
            
            while old_idx < len(old_lines) or new_idx < len(new_lines):
                old_line = None
                new_line = None
                old_type = None
                new_type = None
                
                # 获取当前行
                if old_idx < len(old_lines):
                    old_type, old_line = old_lines[old_idx]
                
                if new_idx < len(new_lines):
                    new_type, new_line = new_lines[new_idx]
                
                # 检查是否是从注释变为非注释
                if old_type == 'removed' and new_type == 'added':
                    # 删除的行被注释，添加的行未注释
                    if old_line and new_line:
                        old_stripped = old_line.strip()
                        new_stripped = new_line.strip()
                        
                        # 检查是否是从注释变为非注释
                        if self.is_commented_line(old_line, file_path):
                            # 移除注释标记后比较内容
                            old_content = self.remove_comment_marker(old_line, file_path)
                            new_content = new_line
                            
                            # 如果内容相似（去除空白后），则认为是取消注释
                            if self.content_similar(old_content, new_content):
                                # 获取上下文
                                context = self.get_context(new_lines, new_idx, 3)
                                
                                uncommented_changes.append(UncommentedChange(
                                    file=file_path,
                                    line_number=new_start + new_idx,
                                    old_line=old_line,
                                    new_line=new_line,
                                    context=context
                                ))
                
                # 移动到下一行
                if old_type == 'removed' and new_type != 'added':
                    old_idx += 1
                elif new_type == 'added' and old_type != 'removed':
                    new_idx += 1
                else:
                    old_idx += 1
                    new_idx += 1
        
        return uncommented_changes
    
    def remove_comment_marker(self, line: str, file_path: str) -> str:
        """移除注释标记"""
        ext = self.get_file_extension(file_path)
        
        if ext in ['.sqf', '.hpp', '.cpp', '.h', '.js', '.ts']:
            # 移除 // 及其前面的空白
            return re.sub(r'^\s*//\s*', '', line)
        elif ext == '.py':
            # 移除 # 及其前面的空白
            return re.sub(r'^\s*#\s*', '', line)
        
        return line.strip()
    
    def content_similar(self, old_content: str, new_content: str, threshold: float = 0.8) -> bool:
        """检查两行内容是否相似"""
        old_stripped = old_content.strip()
        new_stripped = new_content.strip()
        
        # 完全匹配
        if old_stripped == new_stripped:
            return True
        
        # 计算相似度（简单的字符匹配）
        if len(old_stripped) == 0 or len(new_stripped) == 0:
            return False
        
        # 使用简单的包含关系检查
        if old_stripped in new_stripped or new_stripped in old_stripped:
            return True
        
        # 计算共同字符比例
        common_chars = sum(1 for c in old_stripped if c in new_stripped)
        similarity = common_chars / max(len(old_stripped), len(new_stripped))
        
        return similarity >= threshold
    
    def get_context(self, lines: List[Tuple], current_idx: int, context_size: int = 3) -> List[str]:
        """获取上下文行"""
        context = []
        start = max(0, current_idx - context_size)
        end = min(len(lines), current_idx + context_size + 1)
        
        for i in range(start, end):
            if i < len(lines):
                _, content = lines[i]
                marker = ">>> " if i == current_idx else "    "
                context.append(f"{marker}{content}")
        
        return context

def generate_report(uncommented_changes: List[UncommentedChange], output_file: str = None) -> str:
    """生成报告"""
    report = f"""# 未注释变更检查报告

## 统计信息

- **总变更数**: {len(uncommented_changes)}
- **涉及文件数**: {len(set(c.file for c in uncommented_changes))}

## 详细列表

"""
    
    if not uncommented_changes:
        report += "\n✅ 未发现从注释状态变为非注释状态的代码行。\n"
        return report
    
    # 按文件分组
    files_dict = {}
    for change in uncommented_changes:
        if change.file not in files_dict:
            files_dict[change.file] = []
        files_dict[change.file].append(change)
    
    for file, changes in sorted(files_dict.items()):
        report += f"\n### {file}\n\n"
        report += f"**变更数**: {len(changes)}\n\n"
        
        for change in changes:
            report += f"**行 {change.line_number}**:\n\n"
            report += f"**之前（已注释）**:\n```\n{change.old_line}\n```\n\n"
            report += f"**现在（未注释）**:\n```\n{change.new_line}\n```\n\n"
            
            if change.context:
                report += "**上下文**:\n```\n"
                report += "\n".join(change.context)
                report += "\n```\n\n"
            
            report += "---\n\n"
    
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"报告已保存到: {output_file}")
    
    return report

def main():
    parser = argparse.ArgumentParser(description='检查 Git 中从注释变为非注释的代码行')
    parser.add_argument('--base', type=str, default='HEAD', 
                       help='基准提交（默认: HEAD）')
    parser.add_argument('--target', type=str, default=None,
                       help='目标提交（默认: 工作区）')
    parser.add_argument('--repo', type=str, default='.',
                       help='Git 仓库路径（默认: 当前目录）')
    parser.add_argument('--output', type=str, default='uncommented_changes_report.md',
                       help='输出报告文件（默认: uncommented_changes_report.md）')
    parser.add_argument('--no-output-file', action='store_true',
                       help='不保存报告文件，只输出到控制台')
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("检查从注释状态变为非注释状态的代码行")
    print("=" * 60)
    
    if args.target:
        print(f"\n比较: {args.base} -> {args.target}")
    else:
        print(f"\n比较: {args.base} -> 工作区")
    
    checker = GitDiffChecker(args.repo)
    uncommented_changes = checker.find_uncommented_changes(args.base, args.target)
    
    print(f"\n找到 {len(uncommented_changes)} 处从注释变为非注释的变更")
    
    if uncommented_changes:
        print("\n前10个变更:")
        for i, change in enumerate(uncommented_changes[:10], 1):
            print(f"\n{i}. {change.file}:{change.line_number}")
            print(f"   之前: {change.old_line[:80]}...")
            print(f"   现在: {change.new_line[:80]}...")
    
    # 生成报告
    output_file = None if args.no_output_file else args.output
    report = generate_report(uncommented_changes, output_file)
    
    if args.no_output_file:
        print("\n" + "=" * 60)
        print(report)

if __name__ == "__main__":
    main()

