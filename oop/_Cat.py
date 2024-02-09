from random import randrange as rr, choice
from typing import Self


class Cat:
    names = ['Барсик', 'Мурка', 'Прыгунья', 'Рыжик', 'Нюрка']
    colors = ['чёрный', 'чёрно-белый', 'серый', 'пятнистый', 'черепаховый', 'рыжий']
    
    def __init__(self, name: str = None, color: str = None):
        self.name = name or choice(self.names)
        self.color = color or choice(self.colors)
    
    def __str__(self):
        return self.name
    
    @staticmethod
    def meow() -> str:
        return 'мяу'
    
    def ask_food(self) -> str:
        return '-'.join([self.meow()]*rr(2, 6))
    
    @classmethod
    def reproduce(cls) -> list[Self]:
        return [cls() for _ in range(rr(3, 6))]


yara = Cat('Яра', 'пятнистый')

# >>> yara
# <__main__.Cat object at 0x000001F5179742C0>

# >>> yara.name
# 'Яра'
# >>> yara.color
# 'пятнистый'

# >>> yara.meow()
# 'мяу'

# >>> yara.ask_food()
# 'мяу-мяу-мяу-мяу-мяу'
# >>> yara.ask_food()
# 'мяу-мяу-мяу-мяу'
# >>> yara.ask_food()
# 'мяу-мяу-мяу-мяу-мяу'
# >>> yara.ask_food()
# 'мяу-мяу-мяу-мяу'
# >>> yara.ask_food()
# 'мяу-мяу-мяу'
# >>> yara.ask_food()
# 'мяу-мяу'

# >>> kittens = yara.reproduce()
# >>>
# >>> for kitten in kittens:
# ...     print(kitten, kitten.color)
# ...
# Прыгунья чёрно-белый
# Нюрка рыжий
# Прыгунья черепаховый
# Барсик черепаховый
