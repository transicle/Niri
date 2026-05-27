#!/usr/bin/env python3

import sys
import subprocess

from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from programs import SCREENSHOT_TOOL

def run_text(cmd):
    return subprocess.check_output(cmd, text=True).strip()

region = run_text([SCREENSHOT_TOOL])

img = subprocess.run(
    ["grim", "-g", region, "-"],
    stdout=subprocess.PIPE,
    check=True,
    text=False  # IMPORTANT
).stdout

subprocess.run(
    ["wl-copy", "--type", "image/png"],
    input=img,
    check=True,
)
