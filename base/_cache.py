# объект, который точно не возвращает ни одна функция
class NoResult:
    pass


# размещение словаря в глобальном пространстве имён необходимо в демонстрационных целях
cached = {}


def cache(func_obj: 'function') -> 'function':
    # словарь с сохранёнными наборами аргументов и значениями должен находиться в локальном пространстве имён - чтобы сохранённые аргументы и значения различных декорируемых функций не конфликтовали между собой
    # cached = {}
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        res = cached.get(key, NoResult)
        if res is NoResult:
            res = func_obj(*args, **kwargs)
            cached[key] = res
        return res
    return wrapper


@cache
def factorial(number: int) -> int:
    res = 1
    for n in range(2, number+1):
        res *= n
    return res


# >>> cached
# {}
# >>> factorial(4)
# 24
# >>> cached
# {((4,), ()): 24}

# при повторном вызове декорированной функции будет возвращено сохранённое значение, а декорируемая функция вызываться не будет
# >>> factorial(4)
# 24
