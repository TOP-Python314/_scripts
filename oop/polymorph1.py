elements1 = [1, 2, '3', '4', 5.6]
elements2 = [7, '8', '9', 10, 11+1j]


for item1, item2 in zip(elements1, elements2):
    try:
        # использование полиморфного метода __add__()
        print(item1 + item2)
    except TypeError as exc:
        print(exc)


# 8
# unsupported operand type(s) for +: 'int' and 'str'
# 39
# can only concatenate str (not "int") to str
# (16.6+1j)
