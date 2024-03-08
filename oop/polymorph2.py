from typing import Literal


class Cat:
    def __init__(self, lang: Literal['ru', 'jp']):
        self.language = lang
    
    def make_sound(self) -> None:
        match self.language:
            case 'ru':
                sound = 'мяу'
            case 'jp':
                sound = 'няя'
        print(sound)


class Dog:
    def make_sound(self) -> None:
        print('гав')


class Snake:
    def make_sound(self) -> None:
        print('шссс')


class Bird:
    def __init__(self, lang: Literal['ru', 'en']):
        self.language = lang
    
    def make_sound(self) -> None:
        match self.language:
            case 'ru':
                sound = 'чирик'
            case 'en':
                sound = 'твит'
        print(sound)


zoo = (Bird('ru'), Dog(), Bird('ru'), Cat('jp'), Snake(), Bird('en'), Cat('ru'))
for animal in zoo:
    # использование полиморфных методов без проверок классов
    animal.make_sound()


# чирик
# гав
# чирик
# няя
# шссс
# твит
# мяу
