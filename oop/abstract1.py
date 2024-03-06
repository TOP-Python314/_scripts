from abc import ABC, abstractmethod


class Test(ABC):
    
    @abstractmethod
    def method_to_be_released_in_subclass(self):
        pass


# до объявления абстрактного метода
# >>> Test()
# <__main__.Test object at 0x000001ADE796BCE0>


# после объявления абстрактного метода
# >>> Test()
# ...
# TypeError: Can't instantiate abstract class Test without an implementation for abstract method 'method_to_be_released_in_subclass'


class SubTest(Test):
    
    def method_to_be_released_in_subclass(self):
        print('реализация метода')


# до реализации (переопределения) абстрактного метода
# >>> SubTest()
# ...
# TypeError: Can't instantiate abstract class SubTest without an implementation for abstract method 'method_to_be_released_in_subclass'

# после реализации (переопределения) абстрактного метода
# >>> SubTest()
# <__main__.SubTest object at 0x00000203B2CEB830>


# >>> Test.__subclasses__()
# [<class '__main__.SubTest'>]
# >>>
# >>> SubTest.__subclasses__()
# []

