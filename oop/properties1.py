from collections.abc import Iterable


class Vector:
    def __init__(self, *numbers: int):
        self.__numbers: list[int] = list(numbers)
    
    # геттер
    @property
    def value(self) -> tuple[int]:
        print('работает геттер')
        return tuple(self.__numbers)
    
    # сеттер
    @value.setter
    def value(self, numbers: Iterable[int]) -> None:
        print('работает сеттер')
        if isinstance(numbers, Iterable):
            for n in numbers:
                if not isinstance(n, int):
                    break
            else:
                self.__numbers = list(numbers)
                return
        raise TypeError


v1 = Vector(1, 5, 2, 0, 3)

# >>> v1.__dict__
# {'_Vector__numbers': [1, 5, 2, 0, 3]}
# >>>
# >>> v1.value
# работает геттер
# (1, 5, 2, 0, 3)
# >>>
# >>> v1.value = (0, 0, 0, 0, 0)
# работает сеттер
# >>>
# >>> v1.value
# работает геттер
# (0, 0, 0, 0, 0)
# >>>
# >>> v1.__dict__
# {'_Vector__numbers': [0, 0, 0, 0, 0]}

# >>> v1.value = '01234'
# работает сеттер
# ...
# TypeError
# >>>
# >>> v1.value = {3, 'три', (0.1, 0.2)}
# работает сеттер
# ...
# TypeError
