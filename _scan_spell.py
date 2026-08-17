# -*- coding: utf-8 -*-
import sys, io, re, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
root = r"addons\mcc_sandbox_mod"
# Known SQF command/variable spelling errors seen in this project or common
patterns = {
    'isnil (should be isNil)': r'\bisnil\b',
    'isnull (should be isNull)': r'\bisnull\b',
    'isclass (should be isClass)': r'\bisclass\b',
    'getvariable (should be getVariable)': r'\bgetvariable\b',
    'setvariable (should be setVariable)': r'\bsetvariable\b',
    'getpos (should be getPos)': r'\bgetpos\b',
    'setpos (should be setPos)': r'\bsetpos\b',
    'getposatl': r'\bgetposatl\b',
    'typeof (should be typeOf)': r'\btypeof\b',
    'createvehicle': r'\bcreatevehicle\b',
    'deletevehicle': r'\bdeletevehicle\b',
    'creategroup': r'\bcreategroup\b',
    'createunit': r'\bcreateunit\b',
    'setdamage': r'\bsetdamage\b',
    'setdir': r'\bsetdir\b',
    'getdir': r'\bgetdir\b',
    'setvelocity': r'\bsetvelocity\b',
    'setposatl': r'\bsetposatl\b',
    'ctrlsettext': r'\bctrlsettext\b',
    'ctrlcreate': r'\bctrlcreate\b',
    'displayctrl': r'\bdisplayctrl\b',
    'finddisplay': r'\bfinddisplay\b',
    'remotexec': r'\bremotexec\b',
    'preprocessfile': r'\bpreprocessfile\b',
    'preprocessfilelinenumbers': r'\bpreprocessfilelinenumbers\b',
    'execvm': r'\bexecvm\b',
    'execv': r'\bexecv\b',
    'compil': r'\bcompil\b',
    'exitwith': r'\bexitwith\b',
    'waituntil': r'\bwaituntil\b',
    'sleep': r'\bsleep\b',
    'foreach': r'\bforeach\b',
}
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
            for label, pat in patterns.items():
                for m in re.finditer(pat, line):
                    hits.append((p[len(root)+1:], i, label, m.group(0)))
print("spelling candidates:", len(hits))
# group by label
from collections import Counter
c = Counter(h[2] for h in hits)
print(dict(c))
for h in hits[:50]:
    print("  %-50s L%-5d %-35s %s" % (h[0], h[1], h[2], h[3]))
