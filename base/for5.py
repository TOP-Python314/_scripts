random_objects = ['слово', 100, (0.1, 0.2)]


for elem in random_objects:
    print(
        '',
        f'элемент списка: {elem!r}',
        f'тип элемента: {type(elem)}',
        sep='\n'
    )
print()

# элемент списка: 'слово'
# тип элемента: <class 'str'>
# 
# элемент списка: 100
# тип элемента: <class 'int'>
# 
# элемент списка: (0.1, 0.2)
# тип элемента: <class 'tuple'>


for i in range(len(random_objects)):
    print(
        '',
        f'элемент списка с индексом {i}: {random_objects[i]!r}',
        f'тип элемента: {type(random_objects[i])}',
        sep='\n'
    )
print()

# элемент списка с индексом 0: 'слово'
# тип элемента: <class 'str'>
# 
# элемент списка с индексом 1: 100
# тип элемента: <class 'int'>
# 
# элемент списка с индексом 2: (0.1, 0.2)
# тип элемента: <class 'tuple'>


# enumerate(random_objects) -> enumerate((0, 'слово'), (1, 100), (2, (0.1, 0.2)))
for i, elem in enumerate(random_objects):
    print(
        '',
        f'элемент списка с индексом {i}: {elem!r}',
        f'тип элемента: {type(elem)}',
        sep='\n'
    )
print()

# элемент списка с индексом 0: 'слово'
# тип элемента: <class 'str'>
# 
# элемент списка с индексом 1: 100
# тип элемента: <class 'int'>
# 
# элемент списка с индексом 2: (0.1, 0.2)
# тип элемента: <class 'tuple'>


# enumerate(random_objects) -> enumerate((1, 'слово'), (2, 100), (3, (0.1, 0.2)))
for n, elem in enumerate(random_objects, 1):
    print(
        '',
        f'{n} по счёту элемент списка: {elem!r}',
        f'тип элемента: {type(elem)}',
        sep='\n'
    )
print()

# 1 по счёту элемент списка: 'слово'
# тип элемента: <class 'str'>
# 
# 2 по счёту элемент списка: 100
# тип элемента: <class 'int'>
# 
# 3 по счёту элемент списка: (0.1, 0.2)
# тип элемента: <class 'tuple'>
