numbers = (1, 1, 2, 3, 5, 8, 13, 21)

# >>> id(numbers)
# 2185975337184
# >>>
# >>> sub = numbers[4:7]
# >>> sub
# (5, 8, 13)
# >>>
# >>> id(sub)
# 2185977734912
# >>>
# >>>
# >>> numbers_copy = numbers[:]
# >>> numbers_copy
# (1, 1, 2, 3, 5, 8, 13, 21)
# >>>
# >>> id(numbers_copy)
# 2185975337184


numbers = list(numbers)

# >>> numbers
# [1, 1, 2, 3, 5, 8, 13, 21]
# >>>
# >>> type(numbers)
# <class 'list'>
# >>>
# >>> id(numbers)
# 2185977726336
# >>>
# >>> numbers_copy = numbers[:]
# >>> numbers_copy
# [1, 1, 2, 3, 5, 8, 13, 21]
# >>>
# >>> type(numbers_copy)
# <class 'list'>
# >>>
# >>> id(numbers_copy)
# 2185975748800

