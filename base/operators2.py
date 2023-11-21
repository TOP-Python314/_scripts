# сравнение чисел

# >>> 2 == 2
# True
# >>> 2 == -2
# False
# >>>
# >>> 4 != 0
# True
# >>> 4 != 4
# False
# >>>
# >>> 5 > 5
# False
# >>>
# >>> 5 >= 5
# True
# >>>
# >>> 7 < 7
# False
# >>>
# >>> 7 <= 7
# True


# сравнение строк

# >>> 'abc' == 'ABC'
# False
# >>> 'abc' == 'ab'
# False
# >>>
# >>> 'a' < 'b'
# True
# >>>
# >>> 'aa' < 'b'
# True
# >>>
# >>> 'aca' > 'abz'
# True
# >>>
# >>> '12' > '2'
# False
# >>>
# >>> 12 > 2
# True
# >>>
# >>> 61 < 'b'
# ...
# TypeError: '<' not supported between instances of 'int' and 'str'
# >>>
# >>> 'aaa' > 'aa'
# True


# функции ord() и chr()

# >>> ord('a')
# 97
# >>> ord(' ')
# 32
# >>> ord('\n')
# 10
# >>>
# >>> chr(1041)
# 'Б'
# >>> chr(1092)
# 'ф'


# сравнение прочих последовательностей

# >>> (1, 2) < (1, 9)
# True
# >>>
# >>> (1, 2) < (1, 'abc')
# ...
# TypeError: '<' not supported between instances of 'int' and 'str'
# >>>
# >>> ['ab', 'abc', 'abcd'] < ['аб', 'абв', 'абвг']
# True

