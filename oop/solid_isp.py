"""Interface Segregation Principle — Принцип Разделения Интерфейсов"""

from abc import ABC, abstractmethod


class MultiFunctionalDevice(ABC):
    """
    Универсальные интерфейсы для многофункционального устройства.
    """
    @abstractmethod
    def print(self):
        """Взаимодействует с драйверами печатающего устройства."""
    
    @abstractmethod
    def scan(self):
        """Взаимодействует с драйверами сканирующего устройства."""
    
    @abstractmethod
    def fax(self):
        """Взаимодействует с драйверами факсимильного устройства."""


class XeroxML10(MultiFunctionalDevice):
    """
    Модель многофункционального устройства.
    """
    def print(self):
        ...
    
    def scan(self):
        ...
    
    def fax(self):
        ...


class Brother5250(MultiFunctionalDevice):
    """
    Модель принтера.
    """
    def print(self):
        ...
    
    # нарушает ISP — устройство Brother5250 не может и никогда не сможет работать как сканер, поэтому данный метод не должен появляться в пространстве имён соответствующего класса
    def scan(self):
        raise NotImplementedError
    
    # нарушает ISP — устройство Brother5250 не может и никогда не сможет работать как факс, поэтому данный метод не должен появляться в пространстве имён соответствующего класса
    def fax(self):
        raise NotImplementedError


# решение — создать раздельные интерфейсы

class Printer(ABC):
    """
    Интерфейс печатающего устройства.
    """
    @abstractmethod
    def print(self):
        """Взаимодействует с драйверами печатающего устройства."""


class Scanner(ABC):
    """
    Интерфейс сканирующего устройства.
    """
    @abstractmethod
    def scan(self):
        """Взаимодействует с драйверами сканирующего устройства."""


class Fax(ABC):
    """
    Интерфейс факсимильного устройства.
    """
    @abstractmethod
    def fax(self):
        """Взаимодействует с драйверами факсимильного устройства."""


class XeroxML10(Printer, Scanner, Fax):
    """
    Модель многофункционального устройства.
    """
    def print(self):
        ...
    
    def scan(self):
        ...
    
    def fax(self):
        ...


class Brother5250(Printer):
    """
    Модель принтера.
    """
    def print(self):
        ...

