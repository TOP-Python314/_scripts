class Test:
    attr = 'атрибут класса'
    
    def method():
        print('вызов метода')


# >>> Test
# <class '__main__.Test'>
# >>>
# >>> Test.__name__
# 'Test'
# >>>
# >>> Test.attr
# 'атрибут класса'
# >>>
# >>> Test.method
# <function Test.method at 0x0000028F7F41EFC0>
# >>>
# >>> Test.method()
# вызов метода


# >>> aaa = Test
# >>> aaa
# <class '__main__.Test'>

