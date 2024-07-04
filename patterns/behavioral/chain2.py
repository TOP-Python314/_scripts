"""Демонстратор цепочки ответственности: брокеры событий и сообщений."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


class Parameter(Enum):
    ATTACK = 0
    DEFENSE = 1


class Modifiers(list):
    """Брокер сообщений.
    Вызываемый список методов handle() модификаторов."""
    def __call__(self, *args, **kwargs):
        # событие: получено сообщение о необходимости вычисления модцифицированных атриубтов
        # реакция: перебор всех обработчиков
        for function in self:
            function(*args, **kwargs)


@dataclass
class Query:
    """Запрос, в котором вычисляются модифицируемые значения. 
    Форма сообщений от инициатора к брокеру и от брокера к управлению обработкой."""
    creature: 'Creature'
    parameter: Parameter
    value: int


class Game:
    """Брокер событий."""
    def __init__(self):
        self.modifiers = Modifiers()
    
    def calc_modified_value(
            self,
            sender: 'Creature',
            query: Query
    ) -> None:
        self.modifiers(sender, query)


@dataclass
class Creature:
    """Инициатор сообщений."""
    game: 'Game'
    name: str
    initial_attack: int
    initial_defense: int
    
    @property
    def attack(self) -> int:
        # реакция иницииатора: создание сообщения
        q = Query(self, Parameter.ATTACK, self.initial_attack)
        # отправка сообщения брокеру сообщений
        self.game.calc_modified_value(self, q)
        return q.value
    
    @property
    def defense(self) -> int:
        # реакция иницииатора: создание сообщения
        q = Query(self, Parameter.DEFENSE, self.initial_defense)
        # отправка сообщения брокеру сообщений
        self.game.calc_modified_value(self, q)
        return q.value
    
    def __str__(self):
        # событие: запрос вычисления модифицированных атрибутов
        return f'{self.name}: A={self.attack} / D={self.defense}'


class CreatureModifier(ABC):
    """Инициатор подписок."""
    def __init__(self, game: Game, creature: Creature):
        # событие: инициализация объекта модификатора
        self.game = game
        self.creature = creature
        # реакция брокера событий: объект метода handle добавляется в список обработчиков — подписка
        self.game.modifiers.append(self.handle)
    
    @abstractmethod
    def handle(self, sender: Creature, query: Query) -> None:
        pass
    
    def remove(self) -> None:
        self.game.modifiers.remove(self.handle)
    
    # для входа в блок with
    def __enter__(self):
        return self
    
    # для выхода из блока with
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.game.modifiers.remove(self.handle)


class DoubleAttackModifier(CreatureModifier):
    def handle(self, sender: Creature, query: Query) -> None:
        if self.creature is sender:
            if query.parameter is Parameter.ATTACK:
                query.value *= 2


class IncreaseDefenseModifier(CreatureModifier):
    def handle(self, sender: Creature, query: Query) -> None:
        if self.creature is sender:
            if query.parameter is Parameter.DEFENSE:
                if self.creature.attack <= 3 * query.value:
                    query.value += 1



if __name__ == '__main__':
    
    new_game = Game()
    goblin = Creature(new_game, 'Гоблин-воин', 3, 2)
    print(goblin)
    
    # breakpoint()
    
    dam = DoubleAttackModifier(new_game, goblin)
    print(goblin)
    
    idm = IncreaseDefenseModifier(new_game, goblin)
    print(goblin)
    
    dam.remove()
    print(goblin)
    
    with DoubleAttackModifier(new_game, goblin):
        print(goblin)
    
    print(goblin)

