from dill import load

from pathlib import Path
from pprint import pprint
from sys import path


script_dir = Path(path[0])
cls_file = script_dir / 'cls'
inst_file = script_dir / 'inst'

with open(cls_file, 'rb') as filein:
    Test = load(filein)

with open(inst_file, 'rb') as filein:
    obj = load(filein)


# >>> pprint(globals(), sort_dicts=False)
# {...
#  'Test': <class '__main__.Test'>,
#  'obj': <__main__.Test object at 0x000001A6B25E0DD0>}
# >>>
# >>> pprint(Test.__dict__, sort_dicts=False)
# mappingproxy({'__module__': '__main__',
#               '__init__': <function Test.__init__ at 0x000002B5C200EFC0>,
#               '__doc__': None,
#               '__dict__': <attribute '__dict__' of 'Test' objects>,
#               '__weakref__': <attribute '__weakref__' of 'Test' objects>})
# >>>
# >>> obj.__dict__
# {'attr': 357}
# >>>
# >>> obj.__class__ is Test
# True

