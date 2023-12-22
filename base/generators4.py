def test_generator():
    print('начало выполнения генераторной функции')
    print('первый шаг')
    yield 4
    print('второй шаг')
    yield 3
    print('третий шаг')
    yield 2
    print('четвёртый шаг')
    yield 1
    print('пятый шаг')
    yield 0
    print('конец выполнения генераторной функции')


# >>> generator_obj = test_generator()
# >>>
# >>> generator_obj
# <generator object test_generator at 0x000002B9C8B074C0>
# >>>
# >>> for elem in generator_obj:
# ...     print(f'\t{elem = }')
# ...
# начало выполнения генераторной функции
# первый шаг
#         elem = 4
# второй шаг
#         elem = 3
# третий шаг
#         elem = 2
# четвёртый шаг
#         elem = 1
# пятый шаг
#         elem = 0
# конец выполнения генераторной функции
# >>> 


# >>> generator_obj = test_generator()
# >>> generator_obj
# <generator object test_generator at 0x000002B9C8B07640>
# >>>
# >>> num = generator_obj.__next__()
# начало выполнения генераторной функции
# первый шаг
# >>> num
# 4
# >>> num = generator_obj.__next__()
# второй шаг
# >>> num
# 3
# >>> num = generator_obj.__next__()
# третий шаг
# >>> num
# 2
# >>> num = generator_obj.__next__()
# четвёртый шаг
# >>> num
# 1
# >>> num = generator_obj.__next__()
# пятый шаг
# >>> num
# 0
# >>> num = generator_obj.__next__()
# конец выполнения генераторной функции
# ...
# StopIteration
# >>>
# >>> num = generator_obj.__next__()
# ...
# StopIteration
