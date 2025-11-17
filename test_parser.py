#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from analyze_bracket_errors_with_lmstudio import ReportParser

parser = ReportParser('bracket_check_report.md')
files = parser.parse()
print(f'解析到 {len(files)} 个文件')
if files:
    print(f'第一个文件: {files[0].file_path}')
    print(f'第一个文件的错误数: {len(files[0].errors)}')
    if files[0].errors:
        print(f'第一个错误: 行 {files[0].errors[0].line}, {files[0].errors[0].message}')

