class Battery:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.charge: int = 0
    
    def full_charge(self):
        self.charge = self.capacity
    
    # self += other
    def __iadd__(self, other: int):
        if isinstance(other, int):
            new_value = self.charge + other
            if new_value >= self.capacity:
                new_value = self.capacity
            self.charge = new_value
        else:
            raise TypeError
        return self
    
    # self -= other
    def __isub__(self, other: int):
        ...
    
    def __repr__(self):
        return f'<{self.charge}/{self.capacity}>'
    

b1 = Battery(10)

# >>> b1
# <0/10>
# >>>
# >>> b1 += 5
# >>> b1
# <5/10>
# >>>
# >>> b1 += 10
# >>> b1
# <10/10>


# b1 + 3    # b1.__add__(3)
# 3 + b1    # 3.__add__(b1)
            # b1.__radd__(3)
