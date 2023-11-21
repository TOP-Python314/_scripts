n1 = int(input('\nвведите число > '))

if n1 % 2 == 1:
    print('n1 нечётное')
elif n1 % 3 == 0:
    print('n1 кратно трём')
else:
    print('n1 чётное')


n2 = int(input('\nвведите число > '))

if n2 % 2 == 1:
    print('n2 нечётное')
else:
    print('n1 чётное')

if n2 % 3 == 0:
    print('n2 кратно трём')
else:
    print('n2 не кратно трём')

