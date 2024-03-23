"""
Dependencies Inversion Principle — Принцип Инверсии Зависимостей

Средний уровень — хранилище
"""

import solid_dip_low as model


__ivan = model.Person('Иван')
__anna = model.Person('Анна')
__elena = model.Person('Елена')
__michael = model.Person('Михаил')
__petr = model.Person('Пётр')
__inna = model.Person('Инна')
__liza = model.Person('Елизавета')

db = model.Relationship()

db.add_relation(__ivan, __elena)
db.add_relation(__ivan, __michael)
db.add_relation(__anna, __elena)
db.add_relation(__anna, __michael)
db.add_relation(__petr, __liza)
