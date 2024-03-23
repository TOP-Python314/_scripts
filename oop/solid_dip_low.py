"""
Dependencies Inversion Principle — Принцип Инверсии Зависимостей

Нижний уровень — модель данных
"""

from collections.abc import Generator
from dataclasses import dataclass, field
from enum import Enum
from typing import Self
from uuid import UUID, uuid4


@dataclass
class Person:
    """Информация о человеке."""
    name: str
    __id: UUID = field(default_factory=uuid4)
    
    def __hash__(self):
        return self.__id.int
    
    def __eq__(self, other: Self):
        if isinstance(other, self.__class__):
            return self.__id == other.__id
        else:
            raise TypeError
    
    def __repr__(self):
        return self.name


class Relation(Enum):
    PARENT = 0
    CHILD = 1


class Relationship:
    """
    Определяет вид и формат хранения информации о связях между людьми. 
    """
    def __init__(self):
        self.storage: set[tuple[Person, Relation, Person]] = set()
    
    def add_relation(
            self,
            parent: Person,
            child: Person,
    ) -> None:
        self.storage.add((parent, Relation.PARENT, child))
        self.storage.add((child, Relation.CHILD, parent))
    
    # решение — предоставить интерфейс для верхнего уровня
    def find_all_children(self, person: Person) -> Generator[Person]:
        """С помощью генератора возвращает всех людей, являющихся детьми переданного Person."""
        for pers1, rel, pers2 in self.storage:
            if pers1 == person:
                if rel is Relation.PARENT:
                    yield pers2

