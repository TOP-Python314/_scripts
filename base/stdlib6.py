from math import factorial
from time import perf_counter as pc


def my_factorial(number: int) -> int:
    prod = 1
    for n in range(2, number+1):
        prod *= n
    return prod


coeff = 10**6

start = pc()
my_factorial(1234)
end = pc()
print(f'время выполнения my_factorial(1234): {(end-start)*coeff:.0f} мкс')

start = pc()
factorial(1234)
end = pc()
print(f'время выполнения factorial(1234): {(end-start)*coeff:.0f} мкс')

