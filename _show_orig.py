# -*- coding: utf-8 -*-
import sys, io, subprocess
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
# Get original region from e2904c0
out = subprocess.run(['git', 'show', 'e2904c0:addons/mcc_sandbox_mod/mcc/dialogs/mcc_boxGen_change.sqf'],
                     capture_output=True, text=True, encoding='utf-8', errors='replace')
orig = out.stdout.split('\n')
# original lines 196-218 (0-based 195-217)
print("=== ORIGINAL L196-218 ===")
for i in range(195, min(218, len(orig))):
    print(i+1, orig[i])
