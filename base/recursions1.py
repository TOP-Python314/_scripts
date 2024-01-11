def recursive_function(counter: int) -> int:
    if counter > 0:
        print(f'рекурсивный вызов: {counter=}')
        res = recursive_function(counter - 1)
        print(f'рекурсивный возврат: {res=}')
        return res
    else:
        print('последний рекурсивный вызов')
        res = counter
        print(f'первый возврат: {res=}')
        return res


# >>> recursive_function(0)
# последний рекурсивный вызов
# первый возврат: res=0
# 0

# >>> recursive_function(4)
# рекурсивный вызов: counter = 4
# рекурсивный вызов: counter = 3
# рекурсивный вызов: counter = 2
# рекурсивный вызов: counter = 1
# последний рекурсивный вызов
# первый возврат: res = 0
# рекурсивный возврат: res = 0
# рекурсивный возврат: res = 0
# рекурсивный возврат: res = 0
# рекурсивный возврат: res = 0
# 0
