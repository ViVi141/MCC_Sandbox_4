# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
p = r"addons\mcc_sandbox_mod\definesMod.hpp"
with open(p, 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()
import re
for m in re.finditer(r'#include\s+"([^"]*[Rr]emote[Ee]xec[^"]*)"', content):
    print("include:", m.group(1))
    # find enclosing context - what class block are we in?
    before = content[:m.start()]
    # count braces to determine nesting
    print("  brace depth:", before.count('{') - before.count('}'))
