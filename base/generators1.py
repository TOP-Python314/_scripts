generator_object = (n**3 for n in range(2, 10))

# >>> generator_object
# <generator object <genexpr> at 0x0000028B449B0520>
# >>>
# >>> type(generator_object)
# <class 'generator'>
# >>> 
# >>> for elem in generator_object:
# ...     print(elem)
# ...
# 8
# 27
# 64
# 125
# 216
# 343
# 512
# 729
# >>> for elem in generator_object:
# ...     print(elem)
# ...
# >>>
# >>> list(generator_object)
# []
# >>>


generator_object = (n**3 for n in range(2, 10))

# >>> list(generator_object)
# [8, 27, 64, 125, 216, 343, 512, 729]
# >>>
# >>> list(generator_object)
# []


generator_object = (n**3 for n in range(2, 10))

# >>> generator_object.__next__()
# 8
# >>> generator_object.__next__()
# 27
# >>> generator_object.__next__()
# 64
# >>> generator_object.__next__()
# 125
# >>> generator_object.__next__()
# 216
# >>> generator_object.__next__()
# 343
# >>> generator_object.__next__()
# 512
# >>> generator_object.__next__()
# 729
# >>> generator_object.__next__()
# ...
# StopIteration