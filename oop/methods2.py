class Monitor:
    """
    Набор уведомлений.
    """
    def info() -> None:
        print('информация обычного уровня важности')
    
    def warning() -> None:
        print('важная информация!')
    
    def alert() -> None:
        print('КРИТИЧЕСКИ ВАЖНАЯ ИНФОРМАЦИЯ')


# >>> Monitor.info
# <function Monitor.info at 0x00000223408EF060>
# >>>
# >>> Monitor.warning
# <function Monitor.warning at 0x00000223408EF100>
# >>>
# >>> Monitor.alert
# <function Monitor.alert at 0x00000223408EF1A0>


# >>> Monitor.info()
# информация обычного уровня важности
# >>>
# >>> Monitor.warning()
# важная информация!
# >>>
# >>> Monitor.alert()
# КРИТИЧЕСКИ ВАЖНАЯ ИНФОРМАЦИЯ


# >>> m1 = Monitor()
# >>>
# >>> m1.info
# <bound method Monitor.info of <__main__.Monitor object at 0x0000022340676690>>
# >>>
# >>> m1.info()
# ...
# TypeError: Monitor.info() takes 0 positional arguments but 1 was given


class Monitor:
    """
    Набор уведомлений.
    """
    @staticmethod
    def info() -> None:
        print('информация обычного уровня важности')
    
    @staticmethod
    def warning() -> None:
        print('важная информация!')
    
    @staticmethod
    def alert() -> None:
        print('КРИТИЧЕСКИ ВАЖНАЯ ИНФОРМАЦИЯ')


# >>> Monitor.info
# <function Monitor.info at 0x0000025B01C5F240>
# >>>
# >>> Monitor.warning
# <function Monitor.warning at 0x0000025B01C5F2E0>
# >>>
# >>> Monitor.alert
# <function Monitor.alert at 0x0000025B01C5F380>

# >>> m1 = Monitor()
# >>>
# >>> m1.info
# <function Monitor.info at 0x0000025B01C5F240>
# >>>
# >>> m1.info()
# информация обычного уровня важности
# >>>
# >>> Monitor.info()
# информация обычного уровня важности


# при вызове статического метода от экземпляра происходит подмена вызова
# m1.info() --> Monitor.info()

# в общем виде
# instance.method(*args, **kwargs) --> Class.method(*args, **kwargs)

