from abc import ABC, abstractmethod
from decimal import Decimal


class Money(ABC, Decimal):
    def __new__(cls, value):
        return super().__new__(cls, f'{float(value):.2f}')
    
    @abstractmethod
    def __repr__(self):
        """Возвращает строковое представление, содержащее международный символ соответствующей валюты."""
    
    @abstractmethod
    def __str__(self):
        """Возвращает строковое представление, содержащее локальные наименования денежных единиц."""


# >>> Money.__mro__
# (<class '__main__.Money'>, <class 'abc.ABC'>, <class 'decimal.Decimal'>, <class 'object'>)


class USD(Money):
    def __repr__(self):
        return f'${super(ABC, self).__str__()}'
    
    def __str__(self):
        _, digits, exp = self.as_tuple()
        dollars = sum(d*10**n for n, d in enumerate(digits[exp-1::-1]))
        cents = sum(d*10**n for n, d in enumerate(digits[:exp-1:-1]))
        return f'{dollars} dollars {cents} cents'


class Rub(Money):
    def __repr__(self):
        return f'{super(ABC, self).__str__()} ₽'
    
    def __str__(self):
        rub, kop = super(ABC, self).__str__().split('.')
        return f'{rub} руб. {kop} коп.'


# >>> Money(100)
# ...
# TypeError: __repr__ returned non-string (type NoneType)

# >>> v1 = Rub(23500)
# >>> v1
# 23500.00 ₽
# >>> print(v1)
# 23500 руб. 00 коп.

# >>> v2 = USD(315.7)
# >>> v2
# $315.70
# >>> print(v2)
# 315 dollars 70 cents

