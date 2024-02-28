class Vehicle:
    name: str = 'транспортное средство'
    wheels: int = 4
    
    def __init__(self, speed: int):
        self.speed = speed
    
    def __repr__(self):
        return f'{self.name} двигается по земле со скоростью {self.speed} км/ч'


class Bike(Vehicle):
    name = 'велосипед'
    wheels = 2


class Car(Vehicle):
    name = 'автомобиль'


class Train(Vehicle):
    name = 'поезд'
    wheels = 12
    
    def __repr__(self):
        return f'{self.name} двигается по железной дороге со скоростью {self.speed} км/ч'


class Aircraft(Vehicle):
    name = 'самолёт'
    wheels = 6
    
    def __init__(self, ground_speed: int, air_speed: int):
        self.ground_speed = ground_speed
        self.air_speed = air_speed
    
    def __repr__(self):
        return f'{self.name} двигается по земле со скоростью {self.ground_speed} км/ч и в воздухе со скоростью {self.air_speed} км/ч'


vehicles = (
    Bike(18),
    Train(75),
    Car(60),
    Aircraft(50, 700)
)

for v in vehicles:
    print(v)

# велосипед двигается по земле со скоростью 18 км/ч
# поезд двигается по железной дороге со скоростью 75 км/ч
# автомобиль двигается по земле со скоростью 60 км/ч
# самолёт двигается по земле со скоростью 50 км/ч и в воздухе со скоростью 700 км/ч

for v in sorted(vehicles, key=lambda v: v.speed, reverse=True):
    print(v)

# AttributeError: 'Aircraft' object has no attribute 'speed'
