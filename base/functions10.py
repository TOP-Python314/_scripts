def func(**kwargs):
    print(
        'ОТЛАДКА: переданные аргументы',
        f'  {kwargs = }',
        f'  {type(kwargs) = }',
        sep='\n'
    )


# >>> func()
# ОТЛАДКА: переданные аргументы
#   kwargs = {}
#   type(kwargs) = <class 'dict'>
# >>>
# >>> func(1)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: func() takes 0 positional arguments but 1 was given
# >>>
# >>> func(a=1)
# ОТЛАДКА: переданные аргументы
#   kwargs = {'a': 1}
#   type(kwargs) = <class 'dict'>
# >>>
# >>> func(par1=100, par2='wow')
# ОТЛАДКА: переданные аргументы
#   kwargs = {'par1': 100, 'par2': 'wow'}
#   type(kwargs) = <class 'dict'>
# >>>
# >>>
# >>> options = {'width': 20, 'height': 60, 'depth': 35}
# >>> func(**options)
# ОТЛАДКА: переданные аргументы
#   kwargs = {'width': 20, 'height': 60, 'depth': 35}
#   type(kwargs) = <class 'dict'>


def full(pos, /, pos_key, *args, key, **kwargs):
    print(
        'ОТЛАДКА: переданные аргументы',
        f'  {pos = }',
        f'  {pos_key = }',
        f'  {args = }',
        f'  {key = }',
        f'  {kwargs = }',
        sep='\n'
    )


# >>> full(1, 2, key=3)
# ОТЛАДКА: переданные аргументы
#   pos = 1
#   pos_key = 2
#   args = ()
#   key = 3
#   kwargs = {}
# >>>
# >>> full(1, pos_key=2, key=3)
# ОТЛАДКА: переданные аргументы
#   pos = 1
#   pos_key = 2
#   args = ()
#   key = 3
#   kwargs = {}
# >>>
# >>> full(*range(1, 10), key=0.1)
# ОТЛАДКА: переданные аргументы
#   pos = 1
#   pos_key = 2
#   args = (3, 4, 5, 6, 7, 8, 9)
#   key = 0.1
#   kwargs = {}
# >>>
# >>> options = {'pos_key': 22, 'key': 33, 'add1': 44, 'add2': 55}
# >>> full(11, **options)
# ОТЛАДКА: переданные аргументы
#   pos = 11
#   pos_key = 22
#   args = ()
#   key = 33
#   kwargs = {'add1': 44, 'add2': 55}
# >>>
# >>> full(6, **{0.1: 123})
# ...
# TypeError: keywords must be strings