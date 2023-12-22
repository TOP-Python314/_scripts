def converging_to_zero(number: int):
    for n in range(number, 0, -1):
        yield n
        yield -n
    yield 0


for n in converging_to_zero(3):
    print(n)

# 3
# -3
# 2
# -2
# 1
# -1
# 0

# >>> list(converging_to_zero(5))
# [5, -5, 4, -4, 3, -3, 2, -2, 1, -1, 0]

