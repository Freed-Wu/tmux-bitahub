"""``{docs,tests}/__init__.py``."""
import sys
import os
from os.path import dirname as dirn
from typing import Final

__all__ = []

ROOTPATH: Final = dirn(dirn(os.path.abspath(__file__)))
path = os.path.join(ROOTPATH, "scripts")
sys.path.insert(0, path)
