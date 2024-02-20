from numbers import Number


class Rectangle:
    def __init__(self, side1: float, side2: float):
        self.width = max(side1, side2)
        self.height = min(side1, side2)
    
    @property
    def area(self) -> float:
        return self.width * self.height
    
    def __repr__(self):
        pad = len(str(self.height))
        line = f'{" "*pad}  ———— '
        return f'{self.width:>{pad+5}}\n{line}\n{self.height} |    |\n{line}'
    
    def __rec_or_number(self, other) -> Number:
        # проверка, что класс other это Rectangle
        # if isinstance(other, Rectangle):
        #     ...
        # проверка, что self и other одного класса
        if isinstance(other, self.__class__):
            return other.area
        elif isinstance(other, Number):
            return other
        else:
            raise TypeError
    
    # self == other
    def __eq__(self, other):
        return self.area == self.__rec_or_number(other)
    
    # self != other
    def __ne__(self, other):
        return self.area != self.__rec_or_number(other)
    
    # self < other
    def __lt__(self, other):
        return self.area < self.__rec_or_number(other)
    
    # self <= other
    def __le__(self, other):
        return self.area <= self.__rec_or_number(other)
    
    # self > other
    def __gt__(self, other):
        return self.area > self.__rec_or_number(other)
    
    # self >= other
    def __ge__(self, other):
        return self.area >= self.__rec_or_number(other)


r1 = Rectangle(5, 10)
r2 = Rectangle(7, 7)

# >>> r1 == r2   # будет выполнен вызов r1.__eq__(r2)
# False
# >>> r1 != r2   # будет выполнен вызов r1.__ne__(r2)
# True
# >>> r1 < r2   # будет выполнен вызов r1.__lt__(r2)
# False
# >>> r1 <= r2   # будет выполнен вызов r1.__le__(r2)
# False
# >>> r1 > r2   # будет выполнен вызов r1.__gt__(r2)
# True
# >>> r1 >= r2   # будет выполнен вызов r1.__ge__(r2)
# True

# >>> r1 > 25
# True
# >>> r1 > 100
# False
# >>> r2 <= 49
# True
# >>> r2 <= 48
# False

# >>> 49 >= r2
# True

# порядок выполнения выражения выше:
# 49.__ge__(r2)  -->  TypeError  -->  тогда:
# r2.__le__(49)
