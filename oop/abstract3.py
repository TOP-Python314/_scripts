from abc import ABC, abstractmethod
from json import loads
from pathlib import Path
from sys import path


notes_path = Path(path[0]) / 'notes.json'


# абстрактный базовый класс: первый (корневой) уровень абстракции
class VirtualInstrument(ABC):
    notes: dict[str, float] = loads(notes_path.read_text(encoding='utf-8'))
    
    @abstractmethod
    def play(self, tone: str) -> bytes:
        pass


# абстрактный производный класс: второй уровень абстракции
class Acoustic(VirtualInstrument):
    def __init__(self, lowest: str, highest: str):
        self.lowest_tone = lowest
        self.highest_tone = highest
    
    @abstractmethod
    def attack(self, value: int) -> bytes:
        pass
    
    def tone_in_range(self, tone: str) -> bool:
        return self.notes[self.lowest_tone] <= self.notes[tone] <= self.notes[self.highest_tone]


# абстрактный производный класс: второй уровень абстракции
class Synthetic(VirtualInstrument):
    @abstractmethod
    def modulate(self, shift: int) -> bytes:
        pass


# абстрактный производный класс: третий уровень абстракции
class Keyboard(Acoustic):
    def __init__(self, lowest: str, highest: str, mechanics: str):
        super().__init__(lowest, highest)
        self.mechanics = mechanics
    
    def attack(self, value: int) -> bytes:
        ...


# абстрактный производный класс: третий уровень абстракции
class String(Acoustic):
    def __init__(self, lowest: str, highest: str, *strings: str):
        super().__init__(lowest, highest)
        self.strings = strings
    
    def attack(self, value: int) -> bytes:
        ...



# класс-реализация
class Piano(Keyboard):
    def __init__(self, lowest: str, highest: str, mechanics: str):
        super().__init__(lowest, highest, mechanics)
        self.__samples_dir_path: Path = Path('')
    
    def play(self, tone: str) -> bytes:
        with open(self.__samples_dir_path / f'{tone}.wav', 'rb') as wavfile:
            raw_audio = wavfile.read()
        return attack(raw_audio)



# класс верхнего уровня, использующий интерфейс виртуальных музыкальных инструментов
class Player:
    """
    Проигрыватель.
    """
    def __init__(self, instrument: VirtualInstrument):
        self.instrument = instrument
    
    def play(self, melody: list[str], **options) -> None:
        for tone in melody:
            self.instrument.play(tone)

