class Proteus:
    @staticmethod
    def move():
        print('движение')
    
    @staticmethod
    def eat():
        print('питание')
    
    @staticmethod
    def reproduce():
        print('размножение')


class Fish(Proteus):
    @staticmethod
    def breath():
        print('дыхание')


class Reptile(Fish):
    @staticmethod
    def hide():
        print('скрытность')


class Bird(Reptile):
    @staticmethod
    def fly():
        print('полёт')


class Mammal(Reptile):
    @staticmethod
    def care():
        print('забота')


class Human(Mammals):
    @staticmethod
    def speak():
        print('речь')


ivan = Human()
kesha = Bird()

# >>> dir(ivan)
# [..., 'breath', 'care', 'eat', 'hide', 'move', 'reproduce', 'speak']

# >>> dir(kesha)
# [..., 'breath', 'eat', 'fly', 'hide', 'move', 'reproduce']

# >>> ivan.__class__
# <class '__main__.Human'>
# >>> ivan.__class__.__mro__
# (<class '__main__.Human'>, 
#  <class '__main__.Mammal'>, 
#  <class '__main__.Reptile'>, 
#  <class '__main__.Fish'>, 
#  <class '__main__.Proteus'>, 
#  <class 'object'>)

# >>> kesha.__class__
# <class '__main__.Bird'>
# >>> kesha.__class__.__mro__
# (<class '__main__.Bird'>,
#  <class '__main__.Reptile'>, 
#  <class '__main__.Fish'>, 
#  <class '__main__.Proteus'>, 
#  <class 'object'>)
