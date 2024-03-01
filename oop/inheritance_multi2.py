class A:
    def __init__(self, value):
        self.attr = value


class B:
    def __init__(self, value):
        self.attr = value + 100


class C(A):
    pass


class D(B, C):
    def __init__(self, value):
        super().__init__(value)
        self.attr += 200


class E:
    def __init__(self, value):
        self.attr2 = value


class F(C, E):
    pass


class G(F, D):
    def __init__(self, value):
        super().__init__(value)
        self.attr += 500


# >>> A.__mro__
# (<class '__main__.A'>, 
#  <class 'object'>)
# >>>
# >>> B.__mro__
# (<class '__main__.B'>, 
#  <class 'object'>)
# >>>
# >>> C.__mro__
# (<class '__main__.C'>, 
#  <class '__main__.A'>, 
#  <class 'object'>)
# >>>
# >>> D.__mro__
# (<class '__main__.D'>, 
#  <class '__main__.B'>, 
#  <class '__main__.C'>, 
#  <class '__main__.A'>, 
#  <class 'object'>)
# >>>
# >>> E.__mro__
# (<class '__main__.E'>, 
#  <class 'object'>)
# >>>
# >>> F.__mro__
# (<class '__main__.F'>, 
#  <class '__main__.C'>, 
#  <class '__main__.A'>, 
#  <class '__main__.E'>, 
#  <class 'object'>)
# >>>
# >>> G.__mro__
# (<class '__main__.G'>, 
#  <class '__main__.F'>, 
#  <class '__main__.D'>, 
#  <class '__main__.B'>, 
#  <class '__main__.C'>, 
#  <class '__main__.A'>, 
#  <class '__main__.E'>, 
#  <class 'object'>)

a = A(1)
b = B(2)
c = C(3)
d = D(4)
e = E(5)
f = F(6)
# breakpoint()
g = G(7)

for inst in (a, b, c, d, e, f, g):
    print(f'{inst.__class__.__name__} instance namespace', inst.__dict__)

# A instance namespace {'attr': 1}
# B instance namespace {'attr': 102}
# C instance namespace {'attr': 3}
# D instance namespace {'attr': 304}
# E instance namespace {'attr2': 5}
# F instance namespace {'attr': 6}
# G instance namespace {'attr': 807}
