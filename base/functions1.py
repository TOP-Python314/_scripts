print('до объявления функции')

def test_func():
    print('работа функции')

print('после объявления функции')

test_func()

print('после вызова функции')

# до объявления функции
# после объявления функции
# работа функции
# после вызова функции


# >>> test_func
# <function test_func at 0x00000217ABCAEFC0>
# >>>
# >>> type(test_func)
# <class 'function'>
# >>>
# >>> test_func.__name__
# 'test_func'

# >>> print
# <built-in function print>
# >>>
# >>> type(print)
# <class 'builtin_function_or_method'>
# >>>
# >>> print.__name__
# 'print'
