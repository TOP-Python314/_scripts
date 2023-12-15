def printer() -> None:
    print('..|....|...|.|...')


# >>> returned_value = printer()
# ..|....|...|.|...
# >>>
# >>> type(returned_value)
# <class 'NoneType'>
# >>>
# >>> returned_value is None
# True


def adder() -> int:
    return 4 + 5


# >>> adder()
# 9
# >>>
# >>> n1 = adder()
# >>> n1
# 9
# >>>
# >>> type(adder())
# <class 'int'>


def commander() -> str:
    while True:
        command = input('\n > ')
        if command == 'line':
            return '-' * 50
        elif command == 'square':
            return (
                '|--------|\n'
                '|        |\n'
                '|        |\n'
                '|        |\n'
                '|--------|'
            )
        else:
            print(' неизвестная команда')
    # данное выражение никогда не будет достигнуто
    print('конец вызова функции')


# >>> commander()
# 
#  > line
# '--------------------------------------------------'
# >>>
# >>> commander()
# 
#  > square
# '|--------|\n|        |\n|        |\n|        |\n|--------|'
# >>>
# >>> commander()
# 
#  > circle
#  неизвестная команда
# 
#  > quit
#  неизвестная команда
# 
#  > line
# '--------------------------------------------------'
# >>>
