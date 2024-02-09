from pathlib import Path
from sys import path


class TextFileReader:
    default_path = Path(path[0]) / 'methods3.py'
    
    @classmethod
    def read_file(cls, file_path: str | Path = None) -> str:
        if file_path is None:
            file_path = cls.default_path
        return file_path.read_text(encoding='utf-8')


# 1. связанный метод - нельзя использовать от объекта класса
# >>> TextFileReader.read_file()
# ...
# TypeError: TextFileReader.read_file() missing 1 required positional argument: 'self'
# >>>
# >>> t1 = TextFileReader()
# >>> t1.read_file()
# "from pathlib import Path\n ... "


# 2. статический метод - можно использовать от класса и экземпляра, не подходит для наследования
# >>> TextFileReader.read_file()
# "from pathlib import Path\n ... "
# >>>
# >>> t1 = TextFileReader()
# >>> t1.read_file()
# "from pathlib import Path\n ... "


# 3. классовый метод - можно использовать от класса и экземпляра, удобен для наследования
# >>> TextFileReader.read_file()
# "from pathlib import Path\n ... "
# >>>
# >>> t1 = TextFileReader()
# >>> t1.read_file()
# "from pathlib import Path\n ... "


# при вызове классового метода от экземпляра происходит подмена вызова
# t1.read_file() --> TextFileReader.read_file(TextFileReader)

# в общем виде
# instance.method(*args, **kwargs) --> Class.method(Class, *args, **kwargs)

