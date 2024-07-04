from pathlib import Path
from sys import path

root_dir = Path(path[0]).parent
path.insert(1, str(root_dir / 'base'))

import functions3


def test_returns_int():
    assert type(functions3.adder(10, 6)) is int


def test_returns_float():    
    assert type(functions3.adder(12.0, 6)) is float


# > pytest tests\test_adder.py
# ================================ test session starts ==================================
# platform win32 -- Python 3.12.0, pytest-8.1.1, pluggy-1.4.0
# rootdir: D:\G-Doc\TOP Academy\Python web\314\scripts
# collected 2 items
# 
# tests\test_adder.py ..                                                           [100%]
# 
# ================================= 2 passed in 0.03s ===================================


# > pytest -v tests\test_adder.py
# ================================ test session starts ==================================
# platform win32 -- Python 3.12.0, pytest-8.1.1, pluggy-1.4.0 -- C:\Python312\python.exe
# cachedir: .pytest_cache
# rootdir: D:\G-Doc\TOP Academy\Python web\314\scripts
# collected 2 items
# 
# tests/test_adder.py::test_returns_int PASSED                                     [ 50%]
# tests/test_adder.py::test_returns_float PASSED                                   [100%]
# 
# ================================= 2 passed in 0.03s ===================================

