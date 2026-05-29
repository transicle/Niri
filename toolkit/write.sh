#!/usr/bin/env bash
set -euo pipefail

rm -rf ~/.config/niri/*
cp -r ~/Projects/niri/* ~/.config/niri/

bash ~/.config/niri/toolkit/lazy-git.sh