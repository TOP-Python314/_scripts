from pathlib import Path
from sys import path

# конструирование путей

# >>> dir_path = Path(r'C:\Users\Геннадий\Documents\_TOP')
# >>> 
# >>> type(dir_path)
# <class 'pathlib.WindowsPath'>
# >>>
# >>> str(dir_path)
# 'C:\\Users\\Геннадий\\Documents\\_TOP'
# >>>
# >>> dir_path
# WindowsPath('C:/Users/Геннадий/Documents/_TOP')
# >>>
# >>> dir_path / '321'
# WindowsPath('C:/Users/Геннадий/Documents/_TOP/321')
# >>>
# >>> dir_path / '321/scripts'
# WindowsPath('C:/Users/Геннадий/Documents/_TOP/321/scripts')
# >>> 
# >>> 
# >>> file_path = dir_path / '321/scripts/base/function2.py'
# >>> 
# >>> file_path
# WindowsPath('C:/Users/Геннадий/Documents/_TOP/321/scripts/base/function2.py')
# >>>
# >>> file_path.name
# 'function2.py'
# >>>
# >>> dir_path.name
# '_TOP'
# >>>
# >>> file_path.suffix
# '.py'
# >>>
# >>> dir_path.suffix
# ''
# >>>
# >>> file_path.stem
# 'function2'
# >>>
# >>> dir_path.stem
# '_TOP'
# >>>
# >>> file_path.parent
# WindowsPath('C:/Users/Геннадий/Documents/_TOP/321/scripts/base')
# >>>
# >>> dir_path.parent
# WindowsPath('C:/Users/Геннадий/Documents')
# >>>
# >>> dir_path.parents
# <WindowsPath.parents>
# >>>
# >>> print(*dir_path.parents, sep='\n')
# C:\Users\Геннадий\Documents
# C:\Users\Геннадий
# C:\Users
# C:\


# подключение к файловой системе

# >>> for path_ in dir_path.iterdir():
# ...     print(path_)
# ...
# C:\Users\Геннадий\Documents\_TOP\314
# C:\Users\Геннадий\Documents\_TOP\321
# C:\Users\Геннадий\Documents\_TOP\328
# C:\Users\Геннадий\Documents\_TOP\git_connect.py
# C:\Users\Геннадий\Documents\_TOP\hw_send.py
# C:\Users\Геннадий\Documents\_TOP\hw_update.py
# >>>
# >>> dir_path.is_dir()
# True
# >>> dir_path.is_file()
# False
# >>> dir_path.exists()
# True
# >>>
# >>> file_path.is_dir()
# False
# >>> file_path.is_file()
# True
# >>> file_path.exists()
# True

base_dir = Path(path[0])

for path_ in base_dir.glob('module*.py'):
    print(path_)

# C:\Users\Геннадий\Documents\_TOP\314\scripts\base\module1.py
# C:\Users\Геннадий\Documents\_TOP\314\scripts\base\module2.py
# C:\Users\Геннадий\Documents\_TOP\314\scripts\base\module3.py
# C:\Users\Геннадий\Documents\_TOP\314\scripts\base\module4.py

for path_ in base_dir.iterdir():
    if path_.is_dir():
        print(path_)

# C:\Users\Геннадий\Documents\_TOP\314\scripts\base\__pycache__


# >>> base_dir
# WindowsPath('C:/Users/Геннадий/Documents/_TOP/314/scripts/base')
# >>>
# >>> group_dir = base_dir.parent.parent
# >>> group_dir
# WindowsPath('C:/Users/Геннадий/Documents/_TOP/314')
# >>>
# >>> wrong_path = group_dir / 'images'
# >>> wrong_path
# WindowsPath('C:/Users/Геннадий/Documents/_TOP/314/images')
# >>>
# >>> wrong_path.exists()
# False
# >>>
# >>> wrong_path.iterdir()
# <generator object Path.iterdir at 0x000001EEA933B850>
# >>>
# >>> print(*wrong_path.iterdir(), sep='\n')
# ...
# FileNotFoundError: [WinError 3] Системе не удается найти указанный путь: 'C:\\Users\\Геннадий\\Documents\\_TOP\\314\\images'
