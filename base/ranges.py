# >>> type(range(5))
# <class 'range'>


# >>> tuple(range(5))
# (0, 1, 2, 3, 4)
# >>>
# >>> tuple(range(10))
# (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# >>>
# >>> tuple(range(1))
# (0,)
# >>>
# >>> tuple(range(0))
# ()
# >>>
# >>> tuple(range(-10))
# ()
# >>>
# >>> tuple(range(25))
# (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24)


# >>> list(range(5, 10))
# [5, 6, 7, 8, 9]
# >>>
# >>> list(range(-10, 11))
# [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# >>>
# >>> list(range(5, 6))
# [5]
# >>>
# >>> list(range(5, 5))
# []
# >>>
# >>> list(range(5, -5))
# []


# >>> list(range(0, 30, 2))
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
# >>>
# >>> list(range(0, 29, 2))
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
# >>>
# >>> list(range(0, 28, 2))
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26]
# >>>
# >>> list(range(5, -5, -1))
# [5, 4, 3, 2, 1, 0, -1, -2, -3, -4]
# >>>
# >>> list(range(10, 100, 10))
# [10, 20, 30, 40, 50, 60, 70, 80, 90]


# >>> range_object = range(10, 100, 10)
# >>>
# >>> range_object[0]
# 10
# >>> range_object[1]
# 20
# >>> range_object[2]
# 30
# >>> range_object[-1]
# 90
# >>> range_object[2:6]
# range(30, 70, 10)

