# -*- coding: utf-8 -*-
import sys, io, re, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
root = r"addons\mcc_sandbox_mod"
# isNull applied to clearly non-object expressions: strings, numbers, array literals, configs
patterns = [
    (r'isNull\s+"[^"]*"', 'string literal'),
    (r'isNull\s+\d+', 'number'),
    (r'isNull\s+\{', 'code/array'),
    (r'isNull\s+\w+\s*select\s+0\b', 'select 0 result'),
    (r'isNull\s+\(?\w+\)?\s*==', 'comparison'),
]
hits = []
for dirpath, dirs, files in os.walk(root):
    for fn in files:
        if not fn.endswith('.sqf'): continue
        p = os.path.join(dirpath, fn)
        try:
            with open(p, 'r', encoding='utf-8', errors='replace') as f:
                lines = f.readlines()
        except Exception: continue
        for i, line in enumerate(lines, 1):
            for pat, label in patterns:
                for m in re.finditer(pat, line):
                    hits.append((p[len(root)+1:], i, label, line.strip()[:100]))
print("isNull misuse candidates:", len(hits))
for h in hits[:60]:
    print("  %-50s L%-5d %-18s %s" % (h[0], h[1], h[2], h[3]))
