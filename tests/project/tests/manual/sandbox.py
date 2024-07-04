from pathlib import Path
from sys import path

ROOT_DIR = Path(path[0]).parent.parent
SRC_DIR = ROOT_DIR / 'src'

path.insert(0, str(SRC_DIR))

import tic_tac_toe


