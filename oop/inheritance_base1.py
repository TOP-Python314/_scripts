class Product:
    ...


class Fridge(list):
    def __init__(self, *products: str):
        super().__init__(products)
    
    # в классе list есть методы append() и extend(), но их сигнатуры отличаются — если важна именно такая сигнатура, то предпочтительнее добавить ещё один метод
    # def put(self, *products: str):
    #     self.camera.extend(products)
    
    def __repr__(self):
        return '\n'.join(self)
    
    def clear_expired(self):
        ...


kitchen = Fridge('молоко 3,2%', 'филе куриное')

# >>> kitchen
# молоко 3,2%
# филе куриное

# >>> kitchen[1]
# 'филе куриное'

# >>> kitchen.append('картофель')
# >>>
# >>> for prod in kitchen:
# ...     print(prod)
# ...
# молоко 3,2%
# филе куриное
# картофель
