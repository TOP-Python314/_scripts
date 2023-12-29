print(f'\nдо создания функции\n\t{globals() = }')


def function(param: int):
    print(f'\nвнутри функции: перед выполнением\n\t{globals() = }')
    print(f'\nвнутри функции: перед выполнением\n\t{locals() = }')
    local_var = param ** (1/3)
    param = int(local_var)
    try:
        local_var2 = var * 2
    except NameError:
        print('\nпеременной var не существует')
    print(f'\nвнутри функции: перед возвратом\n\t{globals() = }')
    print(f'\nвнутри функции: перед возвратом\n\t{locals() = }')
    return local_var


print(f'\nпосле создания функции\n\t{globals() = }')

var = function(27)

print(f'\nпосле первого вызова функции\n\t{locals() = }')

var = function(125)

print(f'\nпосле второго вызова функции\n\t{locals() = }')
