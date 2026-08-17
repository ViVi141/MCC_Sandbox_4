# -*- coding: utf-8 -*-
import sys, io, re, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
root = r"addons\mcc_sandbox_mod"
# For each cfgFunctions.hpp, check that each function's file exists
# Format: class fncName { file = "..."; } or inherited from parent scope file =
issues = []
checked = 0
for dirpath, dirs, files in os.walk(root):
    for fn in files:
        if fn.lower() != 'cfgfunctions.hpp': continue
        hpp_path = os.path.join(dirpath, fn)
        with open(hpp_path, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        # find file = "..." at each scope
        # simple: match class X { ... } blocks with optional file =
        # Approach: for each 'class <name>' followed by '{', search for 'file = "..."' before matching close
        # Simplified: find all file = paths and all class names with their file
        scope_stack = []  # (name, file)
        current_file = None
        lines = content.split('\n')
        brace_depth = 0
        class_stack = []
        for i, l in enumerate(lines):
            # track class declarations and file= assignments
            cm = re.match(r'\s*class\s+(\w+)', l)
            if cm and '{' in l:
                class_stack.append((cm.group(1), current_file))
            fm = re.search(r'file\s*=\s*"([^"]+)"', l)
            if fm:
                current_file = fm.group(1)
            # crude: after a file= line, subsequent class declarations use it
            # better: reset current_file when we hit a closing of the file-owner scope
            # This is getting complex; use a regex-based approach instead
        break

# Simpler robust approach: use regex to find "class fncName" and the nearest preceding "file =" within same scope
# Parse with a stack
def parse_cfgfns(content):
    classes = []
    stack = []
    # tokenize braces
    tokens = re.findall(r'class\s+(\w+)|\{|\}|file\s*=\s*"([^"]+)"', content)
    cur_file = None
    scope = []
    for t in tokens:
        if t[0]:  # class name
            scope.append(('class', t[0]))
            classes.append({'name': t[0], 'file': cur_file, 'scope_depth': len([s for s in scope if s[0]=='class'])})
        elif t[1]:  # file =
            cur_file = t[1]
        elif t == '{':
            scope.append(('{', None))
        elif t == '}':
            # pop back to last class
            while scope and scope[-1][0] != 'class':
                scope.pop()
            if scope and scope[-1][0] == 'class':
                scope.pop()
    return classes

for dirpath, dirs, files in os.walk(root):
    for fn in files:
        if fn.lower() != 'cfgfunctions.hpp': continue
        hpp_path = os.path.join(dirpath, fn)
        with open(hpp_path, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        classes = parse_cfgfns(content)
        for c in classes:
            checked += 1
            name = c['name']
            file_path = c['file']
            if not file_path: continue
            # resolve fn file: <file>\fn_<name>.sqf
            fn_file = os.path.join(root, 'mcc') if False else None
            # file path in config uses backslashes relative to addon root
            candidate = os.path.normpath(os.path.join(root, file_path.replace('\\', os.sep), 'fn_' + name + '.sqf'))
            if not os.path.exists(candidate):
                # also try fn_<lower>.sqf
                candidate2 = os.path.normpath(os.path.join(root, file_path.replace('\\', os.sep), 'fn_' + name.lower() + '.sqf'))
                if not os.path.exists(candidate2):
                    issues.append((hpp_path[len(root)+1:], name, file_path))
print("functions checked:", checked, "missing files:", len(issues))
for it in issues[:30]:
    print("  %-40s fn_%-25s file=%s" % (it[0], it[1], it[2]))
