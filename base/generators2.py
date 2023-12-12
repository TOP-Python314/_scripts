words = ['красный', 'белый', 'фиолетовый']

words_letters1 = []
for word in words:
    words_letters1.append(len(word))

words_letters2 = list(len(word) for word in words)

words_letters3 = [len(word) for word in words]

# >>> words_letters1
# [7, 5, 10]
# >>> words_letters2
# [7, 5, 10]
# >>> words_letters3
# [7, 5, 10]
# >>> 
# >>> type(words_letters1)
# <class 'list'>
# >>> type(words_letters2)
# <class 'list'>
# >>> type(words_letters3)
# <class 'list'>
# >>>
# >>> words_letters1 == words_letters2 == words_letters3
# True
# >>>
# >>> words_letters1 is words_letters2
# False
# >>> words_letters2 is words_letters3
# False
