#!/usr/bin/env python3

import sys
import subprocess

from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from programs import TERMINAL_EMULATOR as program

subprocess.run([program])
