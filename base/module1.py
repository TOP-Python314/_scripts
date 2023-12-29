"""
Главный модуль. Точка входа.
"""

print('начало выполнения главного модуля')

import module2

print('окончание выполнения главного модуля')


# >>> globals()
# {'__name__': '__main__', '__doc__': '\nГлавный модуль. Точка входа.\n', ..., 'module2': <module 'module2' from 'c:\\Users\\Геннадий\\Documents\\_TOP\\314\\scripts\\base\\module2.py'>}
# >>> 
# >>> module2
# <module 'module2' from 'c:\\Users\\Геннадий\\Documents\\_TOP\\314\\scripts\\base\\module2.py'>
# >>>
# >>> type(module2)
# <class 'module'>
# >>>
# >>> module2.__name__
# 'module2'
# >>>
# >>> module2.__doc__
# '\nДополнительный модуль 2.\n'
# >>>
# >>> module2.words
# ['additional', 'module', '2']
# >>>
# >>> module2.module3
# <module 'module3' from 'c:\\Users\\Геннадий\\Documents\\_TOP\\314\\scripts\\base\\module3.py'>
# >>>
# >>> module2.module3.percent
# 0.05


# >>> from module4 import product
# начало выполнения дополнительного модуля 4
# окончание выполнения дополнительного модуля 4
# >>>
# >>> globals()
# {'__name__': '__main__', '__doc__': '\nГлавный модуль. Точка входа.\n', ..., 'module2': <module 'module2' from 'c:\\Users\\Геннадий\\Documents\\_TOP\\314\\scripts\\base\\module2.py'>, 'product': <function product at 0x0000015E82BBF060>}
# >>>
# >>> product(4, 4, 4)
# 64
# >>> 
# >>> import sys
# >>>
# >>> sys
# <module 'sys' (built-in)>
# >>> 
# >>> from pprint import pprint
# >>> 
# >>> pprint
# <function pprint at 0x0000015E82BBF1A0>
# >>>
# >>> pprint(sys.modules, sort_dicts=False)
# {...
#  '__main__': <module '__main__' (<_frozen_importlib_external.SourceFileLoader object at 0x0000015E82949FD0>)>,
#  'module3': <module 'module3' from 'c:\\Users\\Геннадий\\Documents\\_TOP\\314\\scripts\\base\\module3.py'>,
#  'module2': <module 'module2' from 'c:\\Users\\Геннадий\\Documents\\_TOP\\314\\scripts\\base\\module2.py'>,
#  'module4': <module 'module4' from 'c:\\Users\\Геннадий\\Documents\\_TOP\\314\\scripts\\base\\module4.py'>,
#  ...,
#  'pprint': <module 'pprint' from 'C:\\Python312\\Lib\\pprint.py'>}
# >>>
# >>> sys.modules['module4']
# <module 'module4' from 'c:\\Users\\Геннадий\\Documents\\_TOP\\314\\scripts\\base\\module4.py'>
# >>>
# >>> sys.modules['module4'].numbers
# [4, 9, 1, 3, 5]
# >>>
# >>>
# >>> from module4 import numbers as main_numbers
# >>>
# >>> main_numbers
# [4, 9, 1, 3, 5]
# >>>
# >>> main_numbers[0] = 4000
# >>> main_numbers
# [4000, 9, 1, 3, 5]
# >>>
# >>> sys.modules['module4'].numbers
# [4000, 9, 1, 3, 5]
