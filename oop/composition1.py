from typing import Literal


class Person:
    
    class Sex:
        __repr: dict[str, str] = {
            'мужской': 'М', 
            'женский': 'Ж'
        }
        def __init__(self, sex: Literal['мужской', 'женский']):
            self.value: str = sex
        def __repr__(self):
            return self.__repr[self.value]
    
    def __init__(
            self, 
            first_name: str, 
            last_name: str,
            sex: Literal['мужской', 'женский']
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = self.__class__.Sex(sex)
    
    def __repr__(self):
        return f'{self.last_name} {self.first_name} ({self.sex})'


ilya = Person('Илья', 'Ладогин', 'мужской')
olga = Person('Ольга', 'Зимина', 'женский')

# >>> Person
# <class '__main__.Person'>
# >>>
# >>> Person.Sex
# <class '__main__.Person.Sex'>

# >>> Person.Sex('мужской')
# М
# >>> Person.Sex('женский')
# Ж

# >>> ilya
# Ладогин Илья (М)
# >>>
# >>> olga
# Зимина Ольга (Ж)
