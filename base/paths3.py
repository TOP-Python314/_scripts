from pathlib import Path
from sys import path

# >>> type(path)
# <class 'list'>
# >>>
# >>> print(*path, sep='\n')
# C:\Users\Геннадий\Documents\_TOP\314\scripts\base
# C:\Python312\python312.zip
# C:\Python312\DLLs
# C:\Python312\Lib
# C:\Python312
# C:\Python312\Lib\site-packages
# >>>
# >>> from pprint import pprint
# >>>
# >>> pprint
# <function pprint at 0x000001D5A7CBF100>

# после добавления файла:
# C:\Users\Геннадий\Documents\_TOP\314\scripts\base\pprint.py

# >>> print(*path, sep='\n')
# C:\Users\Геннадий\Documents\_TOP\314\scripts\base
# C:\Python312\python312.zip
# C:\Python312\DLLs
# C:\Python312\Lib
# C:\Python312
# C:\Python312\Lib\site-packages
# >>>
# >>> from pprint import pprint
# >>>
# >>> pprint
# 'фиг тебе а не функция!'

