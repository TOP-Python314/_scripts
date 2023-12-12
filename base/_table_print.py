#  1   4
# 17 100
#  3  12

table_of_numbers = [
    list(range(i, i+200, 25)) 
    for i in range(-2, 6)
]

width = max(len(str(n)) for row in table_of_numbers for n in row)

for row in table_of_numbers:
    print(*(f'{n:>{width}}' for n in row))
    # то же самое с помощью строковых методов
    # print(*(str(n).rjust(width) for n in row))

