# -*- coding: utf-8 -*-
import sys, io, re, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
root = r"addons\mcc_sandbox_mod"
# format "..." with %1..%N - check if the args after match count
# Simplified: find format strings with placeholders, count unique %N max, compare to following args count
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
            # single-line format calls: format["...%1...", a, b, c]
            for m in re.finditer(r'format\s*\[\s*"([^"]*)"\s*,(.*?)\]', line):
                fmt = m.group(1)
                args = m.group(2)
                # count placeholders
                phs = set(int(x) for x in re.findall(r'%(\d+)', fmt))
                if not phs: continue
                maxph = max(phs)
                # count args (crude: split by top-level commas)
                arg_count = args.count(',') + 1
                if arg_count == 0: continue
                if arg_count < maxph:
                    hits.append((p[len(root)+1:], i, 'missing args', fmt[:50], 'max=%d args=%d' % (maxph, arg_count)))
                elif arg_count > maxph + 2:
                    hits.append((p[len(root)+1:], i, 'too many args', fmt[:50], 'max=%d args=%d' % (maxph, arg_count)))
print("format mismatch candidates:", len(hits))
for h in hits[:40]:
    print("  %-50s L%-5d %-14s %-40s %s" % (h[0], h[1], h[2], h[3], h[4]))
