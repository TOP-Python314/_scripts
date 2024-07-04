from pathlib import Path
from sys import path


base_dir = Path(path[0])

file1_path = base_dir / 'module2.py'
file2_path = base_dir.parent / 'git1.txt'

# >>> open(file1_path)
# <_io.TextIOWrapper name='C:\\Users\\Геннадий\\Documents\\_TOP\\314\\scripts\\base\\module2.py' mode='r' encoding='cp1251'>


# функция open() возвращает файлоподобный (file-like) объект
filein = open(file1_path, encoding='utf-8')
text1 = filein.read()

# ручное закрытие обращения к файлу (дескриптора)
filein.close()

# возвращаемое значение функции после with ассоциируется с идентификатором после as
with open(file2_path, encoding='utf-8') as filein:
    text2 = filein.read()
# завершение работы менеджера контекста автоматически закроет обращение к файлу (дескриптор)


