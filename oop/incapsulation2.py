class Test:
    def __init__(self):
        self.__secret = 'очень важное значение'
    
    def instance_inner_namespace(self):
        return self.__dict__
    
    # метод геттер (getter)
    def get_secret(self):
        return self.__secret
    
    # метод сеттер (setter)
    def set_secret(self, new_value):
        self.__secret = new_value


t1 = Test()

# >>> t1.__dict__
# {'_Test__secret': 'очень важное значение'}
# >>>
# >>> t1.instance_inner_namespace()
# {'_Test__secret': 'очень важное значение'}
# >>>
# >>> t1.get_secret()
# 'очень важное значение'
# >>>
# >>> t1.set_secret('новое секректное значение')
# >>>
# >>> t1.get_secret()
# 'новое секректное значение'
# >>>
# >>> t1.__dict__
# {'_Test__secret': 'новое секректное значение'}
