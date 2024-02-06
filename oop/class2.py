class A:
    attr1 = 'атрибут класса'


instance = A()

# внутреннее пространство имён класса
# >>> A.__dict__
# mappingproxy({..., 'attr1': 'атрибут класса'})
# >>>
# >>> A.attr1
# 'атрибут класса'

# внутреннее пространство имён экземпляра
# >>> instance.__dict__
# {}

# доступ к атрибуту класса от экземпляра возможен за счёт расширения области видимости
# >>> instance.attr1
# 'атрибут класса'


# создание атрибута во внутреннем пространстве имён экземпляра
# >>> instance.attr2 = 'атрибут экземпляра'
# >>> instance.__dict__
# {'attr2': 'атрибут экземпляра'}
# >>> 
# >>> new_instance = A()
# >>> new_instance.__dict__
# {}
# >>> 
# >>> A.__dict__
# mappingproxy({..., 'attr1': 'атрибут класса'})


# создание атрибута во внутреннем пространстве имён класса
# >>> A.attr3 = 'ещё один атрибут класса'
# >>> A.__dict__
# mappingproxy({..., 'attr1': 'атрибут класса', 'attr3': 'ещё один атрибут класса'})
# >>>
# >>> instance.attr3
# 'ещё один атрибут класса'
# >>>
# >>> instance.__dict__
# {'attr2': 'атрибут экземпляра'}

