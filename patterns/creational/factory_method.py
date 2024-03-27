"""Демонстратор фабричный метод."""

from enum import Enum
from math import cos, sin, pi
from numbers import Real
from typing import Self


class CoordinateSystem(Enum):
    CARTESIAN = 0
    POLAR = 1


class Point:
    """
    Описывает точку на плоскости в декартовой системе координат.
    
    Целевой класс.
    """
    # не оптимальный вариант
    # def __init__(
    #         self, 
    #         a: Real, 
    #         b: Real, 
    #         system: CoordinateSystem = CoordinateSystem.CARTESIAN
    # ):
    #     if system is CoordinateSystem.CARTESIAN:
    #         self.x = a
    #         self.y = b
    #     elif system is CoordinateSystem.POLAR:
    #         self.x = a * cos(b)
    #         self.y = a * sin(b)
    
    # оптимальный вариант
    def __init__(self, x: Real, y: Real):
        self.x = x
        self.y = y
    
    @classmethod
    def cartesian(cls, x: Real, y: Real) -> Self:
        """Создаёт экземпляр точки с помощью координат декартовой системы.
        Фабричный метод.
        
        :param x: координата оси абсцисс
        :param y: координата оси ординат
        """
        return cls(x, y)
    
    @classmethod
    def polar(cls, rho: Real, phi: Real) -> Self:
        """Создаёт экземпляр точки с помощью координат полярной системы.
        Фабричный метод.
        
        :param rho: (ρ) радиус-вектор
        :param phi: (φ) азимут (в радианах)
        """
        x = rho * cos(phi)
        y = rho * sin(phi)
        return cls(x, y)
    
    def __repr__(self):
        return f"<{self.__class__.__name__}: x={self.x:.2f}, y={self.y:.2f}>"
    
    def __str__(self):
        return f'({self.x:.2f}; {self.y:.2f})'



if __name__ == '__main__':
    
    p0 = Point(0, 0)
    
    # >>> p0
    # <Point: x=0, y=0>
    
    p1 = Point.cartesian(-2, -2)
    p2 = Point.cartesian(4, 1.5)
    
    # >>> p1
    # <Point: x=-2, y=-2>
    # >>> print(p2)
    # (4.00; 1.50)
    
    p3 = Point.polar(3.46, pi/6)
    p4 = Point.polar(-6, 3*pi/4)
    
    # >>> p3
    # <Point: x=3.00, y=1.73>
    # >>> print(p4)
    # (4.24; -4.24)

