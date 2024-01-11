def gcd(number1: int, number2: int) -> int:
    """Рекурсивное вычисление наибольшего общего делителя (НОД)."""
    if number2:
        res = gcd(number2, number1 % number2)
        return res
    else:
        return number1


# >>> gcd(10, 5)
# 5
# >>> gcd(24, 18)
# 6
# >>> gcd(17, 13)
# 1
