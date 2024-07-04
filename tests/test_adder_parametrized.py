from pytest import mark

from pathlib import Path
from sys import path

root_dir = Path(path[0]).parent
path.insert(1, str(root_dir / 'base'))

import functions3


test_data = [
    (10, 3),
    (1, 7),
    (12, 6.0),
    (12.0, 6),
]


@mark.parametrize('n1, n2', test_data)
def test_type(n1, n2):
    if type(n1) is type(n2) is int:
        assert type(functions3.adder(n1, n2)) is int
    
    elif type(n1) is float or type(n2) is float:
        assert type(functions3.adder(n1, n2)) is float


# > pytest -v tests\test_adder_parametrized.py
# ================================= test session starts =================================
# platform win32 -- Python 3.12.0, pytest-8.1.1, pluggy-1.4.0 -- C:\Python312\python.exe
# cachedir: .pytest_cache
# rootdir: D:\G-Doc\TOP Academy\Python web\314\scripts
# collected 4 items
# 
# tests/test_adder_parametrized.py::test_type[10-3] PASSED                         [ 25%]
# tests/test_adder_parametrized.py::test_type[1-7] PASSED                          [ 50%]
# tests/test_adder_parametrized.py::test_type[12-6.0] PASSED                       [ 75%]
# tests/test_adder_parametrized.py::test_type[12.0-6] PASSED                       [100%]
# 
# ================================== 4 passed in 0.04s ==================================

