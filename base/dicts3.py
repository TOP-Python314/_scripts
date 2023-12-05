strings = {'e': 10, 'B': 14, 'G': 23, 'D': 30, 'A': 39, 'E': 47}

# >>> strings.keys()
# dict_keys(['e', 'B', 'G', 'D', 'A', 'E'])
# >>>
# >>> strings.values()
# dict_values([10, 14, 23, 30, 39, 47])
# >>>
# >>> strings.items()
# dict_items([('e', 10), ('B', 14), ('G', 23), ('D', 30), ('A', 39), ('E', 47)])


for val in strings.values():
    print(f'{val / 10:.1f}', end=' ')
print('\n')

# 1.0 1.4 2.3 3.0 3.9 4.7

for item in strings.items():
    print(f'{item = }')
print()

# item = ('e', 10)
# item = ('B', 14)
# item = ('G', 23)
# item = ('D', 30)
# item = ('A', 39)
# item = ('E', 47)

for key, val in strings.items():
    print(f'{key = }  {val = }')

# key = 'e'  val = 10
# key = 'B'  val = 14
# key = 'G'  val = 23
# key = 'D'  val = 30
# key = 'A'  val = 39
# key = 'E'  val = 47
