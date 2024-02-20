class Fridge:
    def __init__(self, *products: str):
        self.camera: list[str] = list(products)
    
    def __iter__(self):
        # return iter(self.camera)
        return self.camera.__iter__()
    
    def __getitem__(self, key: int):
        return self.camera[key]
    
    def put(self, *products: str):
        self.camera.extend(products)
    
    def __repr__(self):
        return '\n'.join(self.camera)


kitchen = Fridge('молоко 3,2%', 'филе куриное')

# >>> kitchen
# молоко 3,2%
# филе куриное

# >>> kitchen[0]
# 'молоко 3,2%'
# >>>
# >>> kitchen.camera[0]
# 'молоко 3,2%'

kitchen.put(
    'сметана 20%',
    'картофель  ',
)

for product in kitchen:
    print(product)

# молоко 3,2%
# филе куриное
# сметана 20%
# картофель
