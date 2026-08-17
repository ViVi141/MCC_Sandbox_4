# -*- coding: utf-8 -*-
import sys, io, re, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
root = r"addons\mcc_sandbox_mod"
issues = []
checked = 0
for dirpath, dirs, files in os.walk(root):
    for fn in files:
        if fn.lower() != 'cfgfunctions.hpp': continue
        hpp_path = os.path.join(dirpath, fn)
        with open(hpp_path, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        # Find leaf function declarations: class fnName { ... } where block contains no nested "class "
        # Use regex to find class blocks at same level
        for m in re.finditer(r'class\s+(\w+)\s*\{([^{}]*)\}', content):
            name, body = m.group(1), m.group(2)
            if not body.strip():
                continue  # empty class like 'login {};'
            # find file = in surrounding context (nearest preceding file= at this scope)
            # get the segment from last '}' or 'class' boundary to here
            checked += 1
            seg_start = content.rfind('}', 0, m.start())
            seg = content[seg_start+1:m.start()]
            fm = re.search(r'file\s*=\s*"([^"]+)"', seg)
            file_path = fm.group(1) if fm else None
            # also check inside body
            if not file_path:
                fm2 = re.search(r'file\s*=\s*"([^"]+)"', body)
                file_path = fm2.group(1) if fm2 else None
            if not file_path:
                continue
            fp_norm = file_path.replace('\\', os.sep).replace(os.sep + os.sep, os.sep).lstrip(os.sep)
            # candidate files
            cands = [
                os.path.join(root, fp_norm, 'fn_' + name + '.sqf'),
                os.path.join(root, fp_norm, 'fn_' + name.lower() + '.sqf'),
                os.path.join(root, fp_norm, name + '.sqf'),
                os.path.join(root, fp_norm, name.lower() + '.sqf'),
            ]
            if not any(os.path.exists(c) for c in cands):
                issues.append((hpp_path[len(root)+1:], name, file_path))
print("leaf functions checked:", checked, "missing:", len(issues))
for it in issues:
    print("  %-42s %-30s file=%s" % (it[0], it[1], it[2]))
