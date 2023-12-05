mutable_set = {1, 1, 2, 4, 3, 2, 1, 5, 6, 5}

# >>> type(mutable_set)
# <class 'set'>

# >>> mutable_set
# {1, 2, 3, 4, 5, 6}

for n in mutable_set:
    print(n, end=' ')
print()

# 1 2 3 4 5 6


immutable_set = frozenset((1, 1, 2, 4, 3, 2, 1, 5, 6, 5))

# >>> type(immutable_set)
# <class 'frozenset'>

# >>> immutable_set
# frozenset({1, 2, 3, 4, 5, 6})

for n in immutable_set:
    print(n, end=' ')

# 1 2 3 4 5 6

# >>> d = {}
# >>> type(d)
# <class 'dict'>
# >>> 
# >>> s = set()
# >>> type(s)
# <class 'set'>

