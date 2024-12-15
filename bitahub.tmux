#!/usr/bin/env python
"""Respect tmux plugin standard."""

import os
import sys

root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(root, "src"))

try:
    from tmux_bitahub.__main__ import main

    main()
except ImportError:
    if os.path.exists("/run/current-system/nixos-version"):
        from subprocess import run

        run(("nix-shell", "--run", os.path.join(root, "bitahub.tmux")))
