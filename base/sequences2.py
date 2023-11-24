words = ['кот', 'пёс', 'рыб']
syllables = ('ма', 'ми', 'му', 'мэ', 'мо')
vowels = 'аеёиоуыэюя'

# изменение объекта list

# >>> id(words)
# 2783602659584
# >>>
# >>> words[2]
# 'рыб'
# >>>
# >>> words[2] = 'ёж'
# >>>
# >>> words
# ['кот', 'пёс', 'ёж']
# >>>
# >>> id(words)
# 2783602659584


# объекты tuple и str являются неизменяемыми

# >>> syllables
# ('ма', 'ми', 'му', 'мэ', 'мо')
# >>>
# >>> syllables[-1] = 'мё'
# ...
# TypeError: 'tuple' object does not support item assignment
# >>>
# >>>
# >>> vowels
# 'аеёиоуыэюя'
# >>>
# >>> vowels[2] = 'е'
# ...
# TypeError: 'str' object does not support item assignment


# ассоциация переменной с новым объектом (пересоздание) возможна всегда

# >>> syllables = (1, 2, 3, 4)
# >>> syllables
# (1, 2, 3, 4)
# >>>
# >>>
# >>> vowels = 'aeiou'
# >>> vowels
# 'aeiou'

