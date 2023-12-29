from pathlib import Path
from sys import path


file_path = Path(path[0]) / 'files2.txt'


text1 = 'тестовая строка для записи в файл'

with open(file_path, 'w', encoding='utf-8') as fileout:
    fileout.write(text1)

text2 = 'вторая тестовая строка для записи в файл'

with open(file_path, 'w', encoding='utf-8') as fileout:
    fileout.write(text2)

text3 = 'третья тестовая строка для записи в файл'

with open(file_path, 'a', encoding='utf-8') as fileout:
    fileout.write(text3)

text4 = 'четвёртая тестовая строка для записи в файл'

with open(file_path, 'a', encoding='utf-8') as out:
    print('\n', text4, file=out)


