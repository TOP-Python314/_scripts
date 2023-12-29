numbers1 = [13, 18, 4, 23, 0]
print(f'{numbers1 = }')
print(f'{id(numbers1) = }')


def sort_numbers():
    print(f'{id(numbers1) = }')
    numbers1.sort()
    

sort_numbers()
print(f'{id(numbers1) = }')
print(f'{numbers1 = }\n')


def change_numbers(numbers: list[int]):
    print(f'{id(numbers) = }')
    numbers.insert(0, -1)


numbers2 = list(range(2, 6))
print(f'{numbers2 = }')
print(f'{id(numbers2) = }')

change_numbers(numbers2)
print(f'{id(numbers2) = }')
print(f'{numbers2 = }')
