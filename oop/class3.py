class Table:
    length = 0
    width = 0
    height = 0


t1 = Table()
t2 = Table()

# >>> t1
# <__main__.Table object at 0x0000022598DCCB60>
# >>> t2
# <__main__.Table object at 0x0000022598BDB950>
# >>>
# >>> id(t1)
# 2360501652320
# >>> id(t2)
# 2360499616080

# >>> Table
# <class '__main__.Table'>
# >>>
# >>> type(t1)
# <class '__main__.Table'>
# >>>
# >>> t1.__class__
# <class '__main__.Table'>
# >>>
# >>> type(t1) is t1.__class__ is Table
# True

# >>> t1.__dict__
# {}
# >>> t2.__dict__
# {}

# >>> t1.length, t1.width, t1.height
# (0, 0, 0)
# >>> 
# >>> t2.length, t2.width, t2.height
# (0, 0, 0)


t1.length, t1.width, t1.height = 120, 80, 80
t2.length, t2.width, t2.height = 100, 100, 60

# >>> Table.__dict__
# mappingproxy({..., 'length': 0, 'width': 0, 'height': 0})

# >>> t1.__dict__
# {'length': 120, 'width': 80, 'height': 80}

# >>> t2.__dict__
# {'length': 100, 'width': 100, 'height': 60}

# >>> Table.length
# 0
# >>> t1.length
# 120
# >>> t2.length
# 100
