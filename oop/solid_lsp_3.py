"""Liskov Substitution Principle — Принцип Подстановки Лисков"""

from collections.abc import Iterable
from numbers import Real


class DictOfRanges(dict):
    """
    Словарь диапазонов: при использовании объекта Real в качестве ключа, возвращает значение, соответствующее кортежу, в диапазон которого попадает объект Real.
    """
    @staticmethod
    def __check_key(key) -> bool:
        if isinstance(key, tuple):
            if len(key) == 2:
                n1, n2 = key
                if isinstance(n1, Real) and isinstance(n2, Real):
                    if n1 < n2:
                        return True
        return False
    
    def __new__(cls, *args, **kwargs):
        if kwargs:
            raise ValueError
        if isinstance(args[0], dict):
            items = args[0].items()
        elif isinstance(args[0], Iterable):
            items = args[0]
        else:
            raise ValueError
        for key, val in items:
            if not cls.__check_key(key):
                raise ValueError
        return super().__new__(cls, *args, **kwargs)
    
    def __getitem__(self, user_key: Real | tuple[Real, Real]):
        if isinstance(user_key, Real):
            for true_key, value in self.items():
                n1, n2 = true_key
                if n1 <= user_key <= n2:
                    return value
            else:
                raise KeyError
        else:
            # нарушает LSP — не позволяет обратиться по истинному ключу
            # raise TypeError
            
            # решение — позволить по истинному ключу 
            return super().__getitem__(user_key)


dict_of_ranges = DictOfRanges({
    (1, 10): 'первый диапазон',
    (11, 20): 'второй диапазон',
    (21, 30): 'третий диапазон',
})

# с нарушением:
# >>> dict_of_ranges[5]
# 'первый диапазон'
# >>>
# >>> dict_of_ranges[(1, 10)]
# ...
# TypeError

# без нарушения:
# >>> dict_of_ranges[5]
# 'первый диапазон'
# >>>
# >>> dict_of_ranges[(1, 10)]
# 'первый диапазон'
