mammals = {
    'тигр',
    'верблюд',
    'баран',
    'кит',
    'морж',
}
aquatic = {
    'осьминог',
    'кальмар',
    'краб',
    'кит',
    'морж',
}

# >>> mammals | aquatic
# {'баран', 'кальмар', 'краб', 'тигр', 'осьминог', 'верблюд', 'кит', 'морж'}

# >>> mammals & aquatic
# {'кит', 'морж'}

# >>> mammals - aquatic
# {'баран', 'верблюд', 'тигр'}
# >>>
# >>> aquatic - mammals
# {'кальмар', 'краб', 'осьминог'}

# >>> mammals ^ aquatic
# {'баран', 'кальмар', 'краб', 'осьминог', 'тигр', 'верблюд'}
# >>>
# >>> (mammals | aquatic) - (mammals & aquatic)
# {'баран', 'кальмар', 'краб', 'тигр', 'осьминог', 'верблюд'}

aquatic_mammals = {'кит', 'морж'}

# >>> aquatic_mammals < mammals
# True
# >>>
# >>> mammals > aquatic_mammals
# True

# >>> mammals < aquatic
# False
# >>> 
# >>> mammals > aquatic
# False

# >>> mammals & aquatic == aquatic_mammals
# True
# >>>
# >>> mammals != aquatic
# True


# >>> {1, 2, 3} == {3, 2, 1}
# True
# >>> 
# >>> {1, 2, 3} < {3, 2, 1}
# False
# >>>
# >>> {1, 2, 3} <= {3, 2, 1}
# True


immutable_aquatic = frozenset(aquatic)

# >>> immutable_aquatic
# frozenset({'кальмар', 'осьминог', 'кит', 'морж', 'краб'})
# >>>
# >>> id(immutable_aquatic)
# 1344675574976
# >>>
# >>> immutable_aquatic |= {'креветка', 'дельфин'}
# >>> immutable_aquatic
# frozenset({'креветка', 'дельфин', 'кальмар', 'осьминог', 'кит', 'морж', 'краб'})
# >>>
# >>> id(immutable_aquatic)
# 1344675575200
# >>> 
# >>> immutable_aquatic.update({'креветка', 'дельфин'})
# ...
# AttributeError: 'frozenset' object has no attribute 'update'

