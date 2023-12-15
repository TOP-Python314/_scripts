def product(num1: float, num2: float, *numbers: float):
    print(
        'ОТЛАДКА: переданные аргументы',
        f'  {num1 = }',
        f'  {num2 = }',
        f'  {numbers = }',
        f'  {type(numbers) = }',
        sep='\n'
    )
    numbers = num1, num2, *numbers
    print(
        'ОТЛАДКА: после пересоздания numbers',
        f'  {numbers = }',
        sep='\n'
    )
    
    if 0 in numbers:
        return 0
    
    result = 1
    for n in numbers:
        result *= n
    return result


# >>> product()
# ...
# TypeError: product() missing 2 required positional arguments: 'num1' and 'num2'
# >>>
# >>> product(1, 2)
# ОТЛАДКА: переданные аргументы
#   num1 = 1
#   num2 = 2
#   numbers = ()
#   type(numbers) = <class 'tuple'>
# ОТЛАДКА: после пересоздания numbers
#   numbers = (1, 2)
# 2
# >>> product(1, 2, 3)
# ОТЛАДКА: переданные аргументы
#   num1 = 1
#   num2 = 2
#   numbers = (3,)
#   type(numbers) = <class 'tuple'>
# ОТЛАДКА: после пересоздания numbers
#   numbers = (1, 2, 3)
# 6
# >>> product(1, 2, 3, 4, 5)
# ОТЛАДКА: переданные аргументы
#   num1 = 1
#   num2 = 2
#   numbers = (3, 4, 5)
#   type(numbers) = <class 'tuple'>
# ОТЛАДКА: после пересоздания numbers
#   numbers = (1, 2, 3, 4, 5)
# 120
# >>> product(*range(2, 10))
# ОТЛАДКА: переданные аргументы
#   num1 = 2
#   num2 = 3
#   numbers = (4, 5, 6, 7, 8, 9)
#   type(numbers) = <class 'tuple'>
# ОТЛАДКА: после пересоздания numbers
#   numbers = (2, 3, 4, 5, 6, 7, 8, 9)
# 362880

