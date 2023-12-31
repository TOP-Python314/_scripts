text = '''Проходит полчаса… час… Уф!
— Наконец—то! — вздыхаете вы, садясь через полтора часа на извозчика. — Уходил, мерзавец! Извозчик, езжай в Хамовники! Ах, проклятый, душу вытянул политикой!
В Хамовниках вас ожидает свидание с полковником Федором Николаичем, у которого в прошлом году вы взяли взаймы шестьсот рублей…
— Спасибо, спасибо, милый мой, — отвечает он на ваше поздравление, ласково заглядывая вам в глаза. — И вам того же желаю… Очень рад, очень рад… Давно ждал вас… Там ведь у нас, кажется, с прошлого года какие—то счеты есть… Не помню, сколько там… Впрочем, это пустяки, я ведь это только так… между прочим… Не желаете ли с дорожки?'''


stops = '.…!?'

replics = text.count('\n—')

# менее оптимальный способ — много итераций по text 
# sentences = sum(text.count(char) for char in stops)

# более оптимальный способ — одна итерация по text
sentences = sum(1 for char in text if char in stops)

print(f'реплики составляют {replics / sentences:.0%} от общего объёма текста')
