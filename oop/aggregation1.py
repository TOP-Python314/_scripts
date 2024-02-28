class A:
    attr = 'атрибут класса A'


class B:
    def __init__(self, instance: A):
        self.associated = instance


a = A()
b = B(a)

# >>> a
# <__main__.A object at 0x0000024F34974710>
# >>>
# >>> a.attr
# 'атрибут класса A'

# >>> b
# <__main__.B object at 0x0000024F34975A60>
# >>>
# >>> b.associated
# <__main__.A object at 0x0000024F34974710>
# >>>
# >>> b.associated.attr
# 'атрибут класса A'

# >>> a.__dict__
# {}
# >>> a.value = 359
# >>>
# >>> b.associated.__dict__
# {'value': 359}
# >>>
# >>> b.associated.value
# 359
