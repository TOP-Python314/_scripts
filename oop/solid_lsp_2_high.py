"""
Liskov Substitution Principle — Принцип Подстановки Лисков

Верхний уровень — управляющий контур, использование модели данных
"""

import solid_lsp_2_low as model


class Test:
    """
    Тестирование согласованности моделей.
    """
    def test_model(rectangle: model.Rectangle) -> None:
        """Проверка взаимозависимости атрибутов width и height класса Rectangle."""
        width = rectangle.width
        rectangle.height *= 2
        expected_area = width * rectangle.height
        calculated_area = rectangle.area
        assert expected_area == calculated_area


rc1 = model.Rectangle(5, 10)

try:
    Test.test_model(rc1)
except AssertionError:
    print('test failed')
else:
    print('test succeeded')

# test succeeded
# >>>
# >>> rc1.width
# 5.0
# >>> rc1.height
# 20.0
# >>> rc1.area
# 100.0


sq1 = model.Square(6)

try:
    Test.test_model(sq1)
except AssertionError:
    print('test failed')
else:
    print('test succeeded')

# test failed
# >>>
# >>> sq1.width
# 12.0
# >>> sq1.height
# 12.0
# >>> sq1.area
# 144.0
