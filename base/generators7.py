def iterable_number(number):
    yield number


for n in iterable_number(47):
    print(n)
# 47


def iter_digits(number: int, low_order: bool = True):
    for d in str(number)[::-1]:
        yield int(d)


print(*iter_digits(30928))
# 8 2 9 0 3
