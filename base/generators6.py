def counter(number: int):
    while True:
        yield number
        number += 1


text = input(' > ')
for items in zip(text, counter(0)):
    print(items)


def cycle_alphabet(upper_case: bool = False):
    left, right = (65, 90) if upper_case else (97, 122)
    code = left
    while True:
        yield chr(code)
        code = (code - left + 1) % 26 + left


n1, n2 = map(int, input('\n\nдва числа: ').split())
for items in zip(cycle_alphabet(), range(n1, n2)):
    print(items)

