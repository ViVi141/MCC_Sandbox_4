# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
p = r"addons\mcc_sandbox_mod\mcc\pv_handling\mcc_extras_pv_handler.sqf"
with open(p, 'r', encoding='utf-8', errors='replace') as f:
    lines = f.readlines()

# Remove the 4 erroneous if-blocks (0-based indices):
# block1: 15-17 (L16-18) highCommand
# block2: 26-28 (L27-29) boxGenerator
# block3: 41-43 (L42-44) placeConvoy
# block4: 56-58 (L57-59) startConvoy
blocks = [(15, 18), (26, 29), (41, 44), (56, 59)]
# remove from bottom to top to keep indices valid
for start, end in sorted(blocks, reverse=True):
    # verify content
    seg = lines[start:end]
    assert any('isNull' in l for l in seg), "block not as expected at %d" % start
    del lines[start:end]
with open(p, 'w', encoding='utf-8', errors='replace') as f:
    f.writelines(lines)
print("removed 4 erroneous blocks, now", len(lines), "lines")
# verify
def check(content):
    stack = []; issues = []; i, line = 0, 1; n = len(content)
    in_str = None; in_comment = False
    pairs = {'(':')', '[':']', '{':'}'}
    closers = {')':'(', ']':'[', '}':'{'}
    while i < n:
        c = content[i]
        if c == '\n': line += 1; i += 1; continue
        if in_comment:
            if c == '*' and i+1 < n and content[i+1] == '/': in_comment = False; i += 2; continue
            i += 1; continue
        if in_str:
            if c == in_str:
                if i+1 < n and content[i+1] == in_str: i += 2; continue
                in_str = None
            i += 1; continue
        if c in ('"', "'"): in_str = c; i += 1; continue
        if c == '/' and i+1 < n and content[i+1] == '/':
            while i < n and content[i] != '\n': i += 1
            continue
        if c == '/' and i+1 < n and content[i+1] == '*':
            in_comment = True; i += 2; continue
        if c in pairs: stack.append((c, line)); i += 1; continue
        if c in closers:
            if not stack: issues.append((c, line, 'unexpected'))
            else:
                top, tline = stack.pop()
                if top != closers[c]: issues.append((top, tline, c, line, 'mismatch'))
            i += 1; continue
        i += 1
    for s, l in stack: issues.append((s, l, 'unclosed'))
    return issues
with open(p, 'r', encoding='utf-8', errors='replace') as f:
    print("extras check:", check(f.read()) or "CLEAN")
