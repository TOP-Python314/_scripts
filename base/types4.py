def func():
    pass


print(
    f'{bool(None) = }',
    f'{bool(1) = }',
    f'{bool(-1) = }',
    f'{bool(0) = }',
    f'{bool(0.0000000000000000000000001) = }',
    f'{bool(0.0) = }',
    f'{bool("") = }',
    f'{bool(" ") = }',
    f'{bool([]) = }',
    f'{bool([""]) = }',
    f'{bool(func) = }',
    sep='\n'
)

