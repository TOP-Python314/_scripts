def concatenate(str1, str2, separator=' ') -> str:
    # return str1 + separator + str2
    # f-строки вычисляются быстрее, чем явная конкатенация строк с помощью оператора +
    return f'{str1}{separator}{str2}'


# >>> concatenate('cool', 'python')
# 'cool python'
# >>>
# >>> concatenate('5', '4', ' + ')
# '5 + 4'
# >>>
# >>> concatenate(
# ...     separator='_',
# ...     str2='O',
# ...     str1='o'
# ... )
# 'o_O'
# >>> 
# >>> concatenate('test', separator='word')
# ...
# TypeError: concatenate() missing 1 required positional argument: 'str2'


# приведёт к выбросу SyntaxError
# def list_extend(list1: list = [], list2: list) -> list:
def list_extend(list1: list, list2: list = []) -> list:
    list1.extend(list2)
    return list1


data = (
    ([1, 2], [3, 4]),
    ([0.1, 0.2, 0.3], [-0.1]),
    (['a', 'ab', 'abc'], )
)
for lists in data:
    print(list_extend(*lists))

# [1, 2, 3, 4]
# [0.1, 0.2, 0.3, -0.1]
# ['a', 'ab', 'abc']
