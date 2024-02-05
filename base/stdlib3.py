from random import sample, randrange as rr
from string import ascii_lowercase as letters


random_words = [
    ''.join(sample(letters, k=6))
    for _ in range(rr(2, 7))
]
print(*random_words, sep='\n')

# тест 1:
# xsowyk
# ejdykf

# тест 2:
# uwgjms
# aslqwe

# тест 3:
# lsmdyp
# ymhfdw
# nosmxy
