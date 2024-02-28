from datetime import date, datetime as dt, timedelta as td
from itertools import filterfalse


class Product:
    _default_date_format: str = '%d.%m.%Y'
    
    def __init__(
            self,
            name: str,
            produced: date | str = date.today(),
            days_before_expire: int = 7
    ):
        self.name = name
        if isinstance(produced, str):
            produced = dt.strptime(produced, self._default_date_format).date()
        self.produced: date = produced
        self.expired: date = produced + td(days=days_before_expire)
    
    def is_expired(self) -> bool:
        return date.today() >= self.expired
    
    def __repr__(self):
        state = 'не годен' if self.is_expired() else 'годен'
        return f'{self.name} ({state})'


class Fridge:
    def __init__(self, *products: Product):
        self.camera: list[Product] = list(products)
    
    def __iter__(self):
        return iter(self.camera)
    
    def __getitem__(self, key: int):
        return self.camera[key]
    
    def __repr__(self):
        return '\n'.join(repr(pr) for pr in self.camera)
    
    def put(self, *products: Product) -> None:
        self.camera.extend(products)
    
    def clear_expired(self) -> None:
        # for pr in self.camera.copy():
        #     if pr.is_expired():
        #         self.camera.remove(pr)
        
        # to_remove = []
        # for i, pr in enumerate(self.camera):
        #     if pr.is_expired():
        #         to_remove.append(i)
        # for i in to_remove:
        #     self.camera.pop(i)
        
        self.camera = list(filterfalse(
            lambda pr: pr.is_expired(),
            self.camera
        ))


kitchen = Fridge(
    Product('молоко 3,2%', '21.02.2024'),
    Product('говяжья лопатка', days_before_expire=2),
    Product('картофель', '05.02.2024', days_before_expire=15),
)

# >>> kitchen
# молоко 3,2% (годен)
# говяжья лопатка (годен)
# картофель (не годен)

# >>> for product in sorted(kitchen, key=lambda pr: pr.expired):
# ...     print(product.expired, product.name)
# ...
# 2024-02-20 картофель
# 2024-02-24 говяжья лопатка
# 2024-02-28 молоко 3,2%

# >>> kitchen.clear_expired()
# >>>
# >>> kitchen
# молоко 3,2% (годен)
# говяжья лопатка (годен)
