from pathlib import Path
from sys import path


print(f'текущий рабочий каталог\n{Path.cwd()}')
print(f'каталог, в котором находится скрипт\n{Path(path[0])}')


# C:\Users\Геннадий\Documents\_TOP\314\scripts\base
#  21:06:39 > cd ..\..


# C:\Users\Геннадий\Documents\_TOP\314
#  21:05:22 > python scripts\base\paths2.py
# текущий рабочий каталог
# C:\Users\Геннадий\Documents\_TOP\314
# каталог, в котором находится скрипт
# C:\Users\Геннадий\Documents\_TOP\314\scripts\base


# C:\Users\Геннадий\Documents\_TOP\314
#  21:05:24 > cd scripts\base\


# C:\Users\Геннадий\Documents\_TOP\314\scripts\base
#  21:06:03 > python paths2.py
# текущий рабочий каталог
# C:\Users\Геннадий\Documents\_TOP\314\scripts\base
# каталог, в котором находится скрипт
# C:\Users\Геннадий\Documents\_TOP\314\scripts\base

