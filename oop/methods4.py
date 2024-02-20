class Person:
    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name
    
    # машиночитаемое строковое представление
    def __repr__(self):
        return f'{self.first_name[0]}. {self.last_name}'
    
    # человекочитаемое строковое представление
    def __str__(self):
        return f'{self.last_name} {self.first_name}'


ivan = Person('Иванов', 'Иван')
artem = Person('Артёмов', 'Артём')

# машиночитаемое строковое представление объекта ivan отправляется в stdout
# >>> ivan
# И. Иванов
# >>>
# >>> artem
# А. Артёмов

# машиночитаемые строковые представления строк, возвращаемых методами __repr__() и __str__(), отправляются в stdout
# >>> ivan.__repr__()
# 'И. Иванов'
# >>>
# >>> artem.__repr__()
# 'А. Артёмов'
# >>>
# >>>
# >>> ivan.__str__()
# 'Иванов Иван'
# >>>
# >>> artem.__str__()
# 'Артёмов Артём'

# встроенные функции вызывают одноимённый метод от переданного объекта
# >>> repr(ivan)
# 'И. Иванов'
# >>>
# >>> str(ivan)
# 'Иванов Иван'

# функция print() для каждго объекта вызывает метод __str__() и отправляет возвращаемое значение в stdout
# >>> print(ivan, artem, sep='\n')
# Иванов Иван
# Артёмов Артём
# >>>

# >>> f'{ivan}'
# 'Иванов Иван'
# >>>
# >>> f'{ivan!r}'
# 'И. Иванов'
