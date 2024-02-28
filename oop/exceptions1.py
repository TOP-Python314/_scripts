class KeyFormatError(Exception):
    def __init__(self):
        super().__init__("'DictOfRange' keys must be tuples of two numbers")


class KeyOutOfRangeError(LookupError):
    def __init__(self, key: int):
        super().__init__(f'{key} does not match any range of dict')


def test():
    raise KeyFormatError


try:
    test()
except KeyFormatError:
    print('перехвачено пользовательское исключение')


def test2():
    raise KeyOutOfRangeError(60)


try:
    test2()
except LookupError:
    print('перехвачено пользовательское или встроенное исключение')

