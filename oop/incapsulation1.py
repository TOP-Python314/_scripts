class Test:
    def __init__(self, num1, num2, num3):
        # публичный (public) атрибут
        self.attr1 = num1
        # частный (private) атрибут
        self._attr2 = num2
        # защищённый (protected) атрибут
        self.__attr3 = num3


t1 = Test(24, 12, -9)

# >>> t1.attr1
# 24
# >>> t1.attr1 = 'двадцать четыре'
# >>> t1.attr1
# 'двадцать четыре'


# >>> t1.attr2
# ...
# AttributeError: 'Test' object has no attribute 'attr2'. Did you mean: '_attr2'?
# >>>
# >>> t1._attr2
# 12
# >>> t1._attr2 = 'двенадцать'
# >>> t1._attr2
# 'двенадцать'


# >>> t1.attr3
# ...
# AttributeError: 'Test' object has no attribute 'attr3'. Did you mean: 'attr1'?
# >>>
# >>> t1.__attr3
# ...
# AttributeError: 'Test' object has no attribute '__attr3'. Did you mean: '_attr2'?

# для идентификаторов с префиксом '__' интерпретатор включает механизм подмены имён (name mangling)
# >>> t1.__dict__
# {'attr1': 'двадцать четыре', '_attr2': 'двенадцать', '_Test__attr3': -9}

# >>> t1._Test__attr3
# -9
# >>> t1._Test__attr3 = 'минус девять'
# >>> t1._Test__attr3
# 'минус девять'
