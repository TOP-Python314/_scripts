"""OCP — Open–Close Principle — Принцип Открытости–Закрытости"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


class Color(Enum):
    BLACK = 'чёрная'
    RED = 'красная'
    BLUE = 'синяя'


class Size(Enum):
    SM = 'small'
    M = 'medium'
    L = 'large'


@dataclass
class Product:
    """Информация о товаре."""
    name: str
    color: Color
    size: Size


class Catalog(list):
    """
    Класс для работы с каталогом товаров.
    
    self: list[Product]
    """
    def filter_by_color(self, color: Color):
        for product in self:
            if product.color is color:
                yield product
    
    def filter_by_size(self, size: Size):
        for product in self:
            if product.size is size:
                yield product
    
    def filter_by_color_and_size(self, color: Color, size: Size):
        for product in self:
            if product.color is color and product.size is size:
                yield product


# текущая реализация фильтрации (методы в Catalog) нарушает OCP — так как не учитывает увеличения количества критериев для фильтрации
# a b ab
# a b c ab ac bc abc
# a b c d ab ac ad bc bd cd abc abd acd bcd abcd
# в данной реализации количество методов для фильтрации будет расти экспоненциальным образом с увеличением количества критериев


# решение — реализовать цепочку классов для критериев и комбинаций с использованием абстракции и наследования
# с увеличением количества критериев потребуется дополнительно определить новый класс для нового критерия

class Criteria(ABC):
    """
    Определяет конкретную характеристику товара.
    """
    @abstractmethod
    def match(self, product: Product) -> bool:
        """Проверяет соответствие конкретного товара данной характеристике."""


@dataclass
class ColorCriteria(Criteria):
    color: Color
    
    def match(self, product: Product) -> bool:
        return product.color is self.color


@dataclass
class SizeCriteria(Criteria):
    size: Size
    
    def match(self, product: Product) -> bool:
        return product.size is self.size


class AndCriteria(Criteria, list):
    """
    Комбинирует несколько произвольных характеристик товаров.
    """
    def __init__(
            self, 
            criteria1: Criteria, 
            criteria2: Criteria, 
            *criterias: Criteria
    ):
        """Принимает от двух и больше различных характеристик товара."""
        criterias = criteria1, criteria2, *criterias
        if len(criterias) == len({crit.__class__ for crit in criterias}):
            super().__init__(criterias)
        else:
            raise TypeError('характеристики одного класса не могут быть скомбинированы')
    
    def match(self, product: Product) -> bool:
        """Проверяет соответствие конкретного товара всем характеристикам одновременно."""
        # более оптимальный вариант — прерывает проверку на первом несоответствии
        for criteria in self:
            if not criteria.match(product):
                return False
        return True
        # менее оптимальный вариант — обязательно выполнит все проверки
        # return all(map(
        #     lambda crit: crit.match(product),
        #     self
        # ))


class Catalog(list):
    """
    Класс для работы с каталогом товаров.
    
    self: list[Product]
    """
    def filter(self, criteria: Criteria):
        for product in self:
            if criteria.match(product):
                yield product


catalog = Catalog([
    Product('футболка чёрная', Color.BLACK, Size.M),
    Product('футболка чёрная', Color.BLACK, Size.L),
    Product('футболка красная', Color.RED, Size.SM),
    Product('футболка красная с треугольным вырезом', Color.RED, Size.SM),
    Product('футболка красная с треугольным вырезом', Color.RED, Size.M),
    Product('футболка красная с треугольным вырезом', Color.RED, Size.L),
    Product('футболка синяя', Color.BLUE, Size.L),
])

# >>> black = ColorCriteria(Color.BLACK)
# >>> red = ColorCriteria(Color.RED)
# >>> blue = ColorCriteria(Color.BLUE)
# >>>
# >>> sm = SizeCriteria(Size.SM)
# >>> m = SizeCriteria(Size.M)
# >>> l = SizeCriteria(Size.L)
# >>>
# >>> red_and_sm = AndCriteria(red, sm)
# >>>
# >>>
# >>> print(*catalog.filter(black), sep='\n')
# Product(name='футболка чёрная', color=<Color.BLACK: 'чёрная'>, size=<Size.M: 'medium'>)
# Product(name='футболка чёрная', color=<Color.BLACK: 'чёрная'>, size=<Size.L: 'large'>)
# >>>
# >>> print(*catalog.filter(m), sep='\n')
# Product(name='футболка чёрная', color=<Color.BLACK: 'чёрная'>, size=<Size.M: 'medium'>)
# Product(name='футболка красная с треугольным вырезом', color=<Color.RED: 'красная'>, size=<Size.M: 'medium'>)
# >>>
# >>> print(*catalog.filter(red), sep='\n')
# Product(name='футболка красная', color=<Color.RED: 'красная'>, size=<Size.SM: 'small'>)
# Product(name='футболка красная с треугольным вырезом', color=<Color.RED: 'красная'>, size=<Size.SM: 'small'>)
# Product(name='футболка красная с треугольным вырезом', color=<Color.RED: 'красная'>, size=<Size.M: 'medium'>)
# Product(name='футболка красная с треугольным вырезом', color=<Color.RED: 'красная'>, size=<Size.L: 'large'>)
# >>>
# >>> print(*catalog.filter(red_and_sm), sep='\n')
# Product(name='футболка красная', color=<Color.RED: 'красная'>, size=<Size.SM: 'small'>)
# Product(name='футболка красная с треугольным вырезом', color=<Color.RED: 'красная'>, size=<Size.SM: 'small'>)
