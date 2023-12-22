def catcher(func_obj: 'function') -> 'function':
    def wrapper(*args, **kwargs):
        try:
            return func_obj(*args, **kwargs)
        except Exception as exc:
            return exc
    return wrapper


def divider(n1: float, n2: float) -> float:
    return n1 / n2


def name_format(full_name: str) -> str:
    last, first, patr = full_name.split(' ')
    return f'{last} {first[0]}. {patr[0]}.'


# >>> divider(1, 5)
# 0.2
# >>> divider(6, 0)
# ...
# ZeroDivisionError: division by zero
# >>>
# >>> divider = catcher(divider)
# >>>
# >>> divider(1, 6)
# 0.16666666666666666
# >>> divider(1, 0)
# ZeroDivisionError('division by zero')


# >>> name_format('Шаповаленко Геннадий Дмитриевич')
# 'Шаповаленко Г. Д.'
# >>>
# >>> name_format('Шаповаленко Геннадий')
# ...
# ValueError: not enough values to unpack (expected 3, got 2)
# >>>
# >>> name_format = catcher(name_format)
# >>>
# >>> name_format('Клишта Данил Сергеевич')
# 'Клишта Д. С.'
# >>>
# >>> name_format('Клишта Данил')
# ValueError('not enough values to unpack (expected 3, got 2)')
# >>>
# >>> name_format('Клишта Данил ')
# IndexError('string index out of range')
