#!/usr/bin/env python
"""Respect tmux plugin standard."""
import os
import sys

sys.path.insert(
    0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src")
)

from tmux_bitahub.__main__ import main

main()
