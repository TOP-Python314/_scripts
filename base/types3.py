# допустимые аргументы для функции float()
print(
    f'{float(1) = }',
    f'{float(1.1) = }',
    f'{float(True) = }',
    f'{float(False) = }',
    f'{float("5") = }',
    f'{float("6.6") = }',
    f'{float("-7.7") = }',
    sep='\n',
    end='\n\n'
)

# недопустимые аргументы для функции float()
# print(float(None))
# print(float("8,8"))
# print(float("9 9"))
# print(float("11/10"))
