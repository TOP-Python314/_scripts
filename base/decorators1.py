def decorator(func_obj: 'function') -> 'function':
    print('начало работы функции-декоратора')
    
    def wrapper(*args, **kwargs):
        """Обёртка декорируемой функции."""
        print('начало работы функции-обёртки')
        result = func_obj(*args, **kwargs)
        print('конец работы функции-обёртки')
        return result
    
    print('конец работы функции-декоратора')
    return wrapper


def test_func() -> None:
    """Тестовая функция."""
    print('декорируемая функция')


# >>> test_func
# <function test_func at 0x000001E8CAEFF060>
# >>>
# >>> test_func.__name__
# 'test_func'
# >>>
# >>> test_func.__doc__
# 'Тестовая функция.'
# >>>
# >>> test_func()
# декорируемая функция

test_func = decorator(test_func)

# начало работы функции-декоратора
# конец работы функции-декоратора

# >>> test_func
# <function decorator.<locals>.wrapper at 0x000001E8CAEFF1A0>
# >>>
# >>> test_func.__name__
# 'wrapper'
# >>>
# >>> test_func.__doc__
# 'Обёртка декорируемой функции.'
# >>>
# >>> test_func()
# начало работы функции-обёртки
# декорируемая функция
# конец работы функции-обёртки

# "синтаксический сахар" для декорирования функции
@decorator
def test_func2():
    return 123

# декорирование функции
# test_func2 = decorator(test_func2)

# >>> test_func2()
# начало работы функции-обёртки
# конец работы функции-обёртки
# 123

