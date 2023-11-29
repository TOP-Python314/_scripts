range_object = range(1, 5)

for n1 in range(1, 6):
    print(f'\nначало выполнения {n1} итерации внешнего цикла')
    for n2 in range_object:
        print(f'\t{n2 = }')
    print(f'конец выполнения {n1} итерации внешнего цикла')

