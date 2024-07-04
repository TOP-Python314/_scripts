from dill import dump

from pathlib import Path
from sys import path


script_dir = Path(path[0])
cls_file = script_dir / 'cls'
inst_file = script_dir / 'inst'


class Test:
    def __init__(self, value):
        self.attr = value


t1 = Test(357)


with open(cls_file, 'wb') as fileout:
    dump(Test, fileout)

with open(inst_file, 'wb') as fileout:
    dump(t1, fileout)

