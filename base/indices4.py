word = 'индексация'

chars = len(word)
# >>> chars
# 10

# >>> word[chars-1]
# 'я'
# >>> word[chars-2]
# 'и'
# >>> word[chars-3]
# 'ц'
# >>> word[len(word)-9]
# 'н'
# >>> word[len(word)-10]
# 'и'

# >>> word[-1]
# 'я'
# >>> word[-2]
# 'и'
# >>> word[-3]
# 'ц'
# >>> word[-4]
# 'а'
# >>> word[-9]
# 'н'
# >>> word[-10]
# 'и'
# >>> word[-11]
# ...
# IndexError: string index out of range
