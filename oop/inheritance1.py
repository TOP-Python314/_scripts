from pprint import pprint


# родительский, базовый, надкласс, суперкласс, старший
class A:
    attr1 = 'атрибут класса A'
    
    def __init__(self):
        self.inst_attr1 = 'атрибут экземпляра класса A'


# дочерний, производный, подкласс, младший
class B(A):
    attr2 = 'атрибут класса B'


a = A()
b = B()

# >>> a.attr1
# 'атрибут класса A'
# >>> a.inst_attr1
# 'атрибут экземпляра класса A'
# >>> b.attr1
# 'атрибут класса A'
# >>> b.attr2
# 'атрибут класса B'
# >>> b.inst_attr1
# 'атрибут экземпляра класса A'

# >>> B.attr2
# 'атрибут класса B'
# >>> B.attr1
# 'атрибут класса A'

# >>> pprint(a.__dict__, sort_dicts=False)
# {'inst_attr1': 'атрибут экземпляра класса A'}
# >>>
# >>> pprint(A.__dict__, sort_dicts=False)
# mappingproxy({'__module__': '__main__',
#               'attr1': 'атрибут класса A',
#               '__init__': <function A.__init__ at 0x000002CF31F2EFC0>,
#               '__dict__': <attribute '__dict__' of 'A' objects>,
#               '__weakref__': <attribute '__weakref__' of 'A' objects>,
#               '__doc__': None})
# >>>
# >>> pprint(b.__dict__, sort_dicts=False)
# {'inst_attr1': 'атрибут экземпляра класса A'}
# >>>
# >>> pprint(B.__dict__, sort_dicts=False)
# mappingproxy({'__module__': '__main__',
#               'attr2': 'атрибут класса B',
#               '__doc__': None})

# >>> dir(a)
# [..., 'attr1', 'inst_attr1']
# >>>
# >>> dir(b)
# [..., 'attr1', 'attr2', 'inst_attr1']
