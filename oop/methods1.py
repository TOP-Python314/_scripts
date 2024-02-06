class Dog:
    def bark(self):
        try:
            name_to_print = self.name
        except AttributeError:
            name_to_print = self
        print(name_to_print, 'говорит гав')


barsik = Dog()


# >>> Dog.bark
# <function Dog.bark at 0x000001CAD511EFC0>

# >>> barsik.bark
# <bound method Dog.bark of <__main__.Dog object at 0x000001CAD4CEB950>>


# при вызове метода от экземпляра происходит подмена вызова
# barsik.bark() --> Dog.bark(barsik)

# в общем виде
# instance.method(*args, **kwargs) --> Class.method(instance, *args, **kwargs)


# >>> barsik.bark()
# <__main__.Dog object at 0x000001CAD4CEB950> говорит гав

# >>> barsik.name = 'Барсик'
# >>> barsik.__dict__
# {'name': 'Барсик'}
# >>> 
# >>> barsik.bark()
# Барсик говорит гав


bobik = Dog()

# >>> bobik.bark()
# <__main__.Dog object at 0x0000025A2B62A360> говорит гав

# >>> bobik.name = 'Бобик'
# >>> bobik.__dict__
# {'name': 'Бобик'}
# >>> 
# >>> bobik.bark()
# Бобик говорит гав