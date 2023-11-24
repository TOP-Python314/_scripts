numbers = [1, 2, 3]

# >>> id(numbers)
# 2345882800384

numbers_copy = numbers

# >>> id(numbers_copy)
# 2345882800384


numbers_copy[0] = 1000

# >>> numbers_copy
# [1000, 2, 3]
# >>>
# >>> numbers
# [1000, 2, 3]

