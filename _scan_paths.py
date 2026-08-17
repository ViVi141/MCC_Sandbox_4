# -*- coding: utf-8 -*-
import sys, io, re, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
root = r"addons\mcc_sandbox_mod"
# execVM / execVM paths
issues = []
checked = 0
for dirpath, dirs, files in os.walk(root):
    for fn in files:
        if not fn.endswith('.sqf'): continue
        p = os.path.join(dirpath, fn)
        try:
            with open(p, 'r', encoding='utf-8', errors='replace') as f:
                lines = f.readlines()
        except Exception: continue
        for i, line in enumerate(lines, 1):
            # execVM "path" - literal paths (not variables/MCC_path concat)
            for m in re.finditer(r'execVM\s+"((?:[^"]+))"', line):
                path = m.group(1)
                if path.startswith(('\\', 'a3', 'A3')): continue
                # resolve relative to addon root; also strip leading \mcc_sandbox_mod\
                rel = path.replace('\\', os.sep).replace('//', os.sep).lstrip(os.sep)
                if rel.startswith('mcc_sandbox_mod' + os.sep):
                    rel = rel[len('mcc_sandbox_mod' + os.sep):]
                cand = os.path.join(root, rel)
                checked += 1
                if not os.path.exists(cand):
                    issues.append((p[len(root)+1:], i, path, 'execVM'))
            # preprocessFile / preprocessFileLineNumbers
            for m in re.finditer(r'preprocessFile(?:LineNumbers)?\s+"((?:[^"]+))"', line):
                path = m.group(1)
                if path.startswith(('\\', 'a3', 'A3')): continue
                rel = path.replace('\\', os.sep).lstrip(os.sep)
                if rel.startswith('mcc_sandbox_mod' + os.sep):
                    rel = rel[len('mcc_sandbox_mod' + os.sep):]
                cand = os.path.join(root, rel)
                checked += 1
                if not os.path.exists(cand):
                    issues.append((p[len(root)+1:], i, path, 'preprocess'))
print("paths checked:", checked, "missing:", len(issues))
for it in issues[:40]:
    print("  %-50s L%-5d %-30s %s" % (it[0], it[1], it[2][:28], it[3]))
