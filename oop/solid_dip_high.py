"""
Dependencies Inversion Principle — Принцип Инверсии Зависимостей

Верхний уровень — использование хранилища и модели данных
"""

from collections.abc import Generator

import solid_dip_low as model
import solid_dip_med as storage


class Research:
    """
    Фасад для взаимодействия с хранилищем информации о связях между людьми.
    """
    def __init__(self, storage: model.Relationship):
        self.db = storage
    
    # нарушает DIP — ...
    # def find_all_children(self, person: model.Person) -> Generator[model.Person]:
    #     """С помощью генератора возвращает всех людей, являющихся детьми переданного Person."""
    #     for pers1, rel, pers2 in self.db.storage:
    #         if pers1 == person:
    #             if rel is model.Relation.PARENT:
    #                 yield pers2


r1 = Research(storage.db)

# с нарушением: 
# >>> print(*r1.find_all_children(storage.__ivan), sep=', ')
# Елена, Михаил
# >>>

# без нарушения: 
# >>> print(*r1.db.find_all_children(storage.__ivan), sep=', ')
# Елена, Михаил
