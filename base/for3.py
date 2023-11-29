right = int(input(' > '))

range_object = range(right)
print(list(range_object))

total = 0
for num in range_object:
    total += num
    # эквивалентно
    # total = total + num

print(f'{total = }')
