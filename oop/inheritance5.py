class A:
    def __init__(self):
        self.attr = 'a'


class B(A):
    def __init__(self):
        self.attr = 'b'


class C(B):
    def __init__(self):
        self.attr = 'c'


class D(C):
    def __init__(self):
        self.attr = 'd'


class Test1(D):
    def __init__(self):
        super().__init__()


class Test2(D):
    def __init__(self):
        super(D, self).__init__()


class Test3(D):
    def __init__(self):
        super(B, self).__init__()


# >>> print(*Test1.__mro__, sep='\n')
# <class '__main__.Test1'>
# <class '__main__.D'>
# <class '__main__.C'>
# <class '__main__.B'>
# <class '__main__.A'>
# <class 'object'>


t1, t2, t3 = Test1(), Test2(), Test3()

# >>> t1.attr
# 'd'
# >>> t2.attr
# 'c'
# >>> t3.attr
# 'a'
