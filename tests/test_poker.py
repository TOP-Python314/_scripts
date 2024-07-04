from pytest import mark, fixture

from pathlib import Path
from sys import path

root_dir = Path(path[0]).parent
path.insert(1, str(root_dir / 'base'))

from _poker import combination


# предустановочные функции (жарг.: фикстуры), вызываемые и выполняемые до запуска тестов

@fixture
def all_names():
    return {'старшая карта', 'пара', 'две пары', 'сет', 'стрит', 'фулл-хаус', 'каре'}


@fixture
def all_combinations():
    return [
        (2, 4, 10, 14, 5),
        (5, 7, 10, 4, 5),
        (4, 5, 6, 6, 5),
        (7, 7, 2, 14, 7),
        (4, 5, 6, 7, 8),
        (4, 5, 4, 4, 5),
        (5, 5, 5, 4, 5),
    ]


def test_comb_names(all_combinations, all_names):
    names = set()
    for comb in all_combinations:
        names.add(combination(comb))
    assert names == all_names



raw_data = (root_dir / 'tests/poker.data').read_text(encoding='utf-8')
test_data = []
for line in raw_data.strip().splitlines():
    comb, name = line.split(' - ')
    comb = map(int, comb.split())
    test_data.append((tuple(comb), name))


@mark.parametrize('comb, comb_name', test_data)
def test_combination(comb, comb_name):
    assert combination(comb) == comb_name


# > pytest -v tests\test_poker.py
# ================================= test session starts =================================
# platform win32 -- Python 3.12.0, pytest-8.2.2, pluggy-1.5.0 -- C:\Python312\python.exe
# cachedir: .pytest_cache
# rootdir: D:\G-Doc\TOP Academy\Python web\314\scripts
# configfile: pytest.ini
# collected 24 items
# 
# tests/test_poker.py::test_comb_names PASSED                                      [  4%]
# tests/test_poker.py::test_combination[comb0-старшая карта] PASSED                [  8%]
# tests/test_poker.py::test_combination[comb1-старшая карта] PASSED                [ 12%]
# tests/test_poker.py::test_combination[comb2-пара] PASSED                         [ 16%]
# tests/test_poker.py::test_combination[comb3-пара] PASSED                         [ 20%]
# tests/test_poker.py::test_combination[comb4-пара] PASSED                         [ 25%]
# tests/test_poker.py::test_combination[comb5-старшая карта] PASSED                [ 29%]
# tests/test_poker.py::test_combination[comb6-пара] PASSED                         [ 33%]
# tests/test_poker.py::test_combination[comb7-старшая карта] PASSED                [ 37%]
# tests/test_poker.py::test_combination[comb8-пара] PASSED                         [ 41%]
# tests/test_poker.py::test_combination[comb9-пара] PASSED                         [ 45%]
# tests/test_poker.py::test_combination[comb10-пара] PASSED                        [ 50%]
# tests/test_poker.py::test_combination[comb11-старшая карта] PASSED               [ 54%]
# tests/test_poker.py::test_combination[comb12-старшая карта] PASSED               [ 58%]
# tests/test_poker.py::test_combination[comb13-две пары] PASSED                    [ 62%]
# tests/test_poker.py::test_combination[comb14-старшая карта] PASSED               [ 66%]
# tests/test_poker.py::test_combination[comb15-старшая карта] PASSED               [ 70%]
# tests/test_poker.py::test_combination[comb16-две пары] PASSED                    [ 75%]
# tests/test_poker.py::test_combination[comb17-пара] PASSED                        [ 79%]
# tests/test_poker.py::test_combination[comb18-сет] PASSED                         [ 83%]
# tests/test_poker.py::test_combination[comb19-старшая карта] PASSED               [ 87%]
# tests/test_poker.py::test_combination[comb20-фулл-хаус] PASSED                   [ 91%]
# tests/test_poker.py::test_combination[comb21-стрит] PASSED                       [ 95%]
# tests/test_poker.py::test_combination[comb22-каре] PASSED                        [100%]
# 
# ================================= 24 passed in 0.09s ==================================

