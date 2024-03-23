"""
Liskov Substitution Principle — Принцип Подстановки Лисков

Нижний уровень — модель данных, используемые объекты
"""


class Rectangle:
    """
    Определяет две стороны и площадь прямоугольника. При изменении каждой стороны, изменяется площадь.
    """
    def __init__(self, width: float, height: float):
        self._width = float(width)
        self._height = float(height)
        self._area = float(width * height)
    
    @property
    def width(self) -> float:
        return self._width
    
    @width.setter
    def width(self, new_width: float):
        self._width = float(new_width)
        self._area = float(new_width * self._height)
    
    @property
    def height(self) -> float:
        return self._height
    
    @height.setter
    def height(self, new_height: float):
        self._height = float(new_height)
        self._area = float(self._width * new_height)
    
    @property
    def area(self) -> float:
        return self._area


class Square(Rectangle):
    """
    Определяет две стороны и площадь квадрата. При изменении каждой стороны изменяются вторая сторона и площадь.
    """    
    def __init__(self, side: float):
        super().__init__(side, side)
    
    # нарушает LSP — создание между атрибутами _width и _height взаимозависимости, которой не было в базовом классе
    @Rectangle.width.setter
    def width(self, new_width: float):
        self._width = float(new_width)
        self._height = float(new_width)
        self._area = float(new_width ** 2)
    
    # нарушает LSP — создание между атрибутами _width и _height взаимозависимости, которой не было в базовом классе
    @Rectangle.height.setter
    def height(self, new_height: float):
        self._width = float(new_height)
        self._height = float(new_height)
        self._area = float(new_height ** 2)


# частичное решение — создать независимый класс Square 
# но для такого класса потребуется отдельный управляющий контур на верхнем уровне

class Square:
    """
    Определяет сторону и площадь квадрата. При изменении стороны изменяется площадь.
    """
    def __init__(self, side: float):
        self._side = float(side)
        self._area = float(side ** 2)
    
    @property
    def side(self) -> float:
        return self._side
    
    @side.setter
    def side(self, new_side: float):
        self._side = float(new_side)
        self._area = float(new_side ** 2)
    
    @property
    def area(self) -> float:
        return self._area

