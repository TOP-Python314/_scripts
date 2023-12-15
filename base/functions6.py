def calculator(num1: float, num2: float, *, operation: str) -> float:
    if operation == '+':
        return float(num1 + num2)
    elif operation == '-':
        return float(num1 - num2)
    elif operation == '*':
        return float(num1 * num2)
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return float(f"{'' if num1 >= 0 else '-'}inf")


# >>> calculator(1, 2, '-')
# ...
# TypeError: calculator() takes 2 positional arguments but 3 were given
# >>> 
# >>> calculator(14, 9, operation='+')
# 23.0
# >>> 
# >>> calculator(num1=5, num2=0, operation='/')
# inf
# >>> 
# >>> calculator(num2=19, operation='*', num1=3)
# 57.0



def calculator(
        num1: float, 
        num2: float, 
        # все параметры слева от разделителя / становятся строго позиционными
        /, 
        # все параметры между разделителями / и * становятся позиционно-ключевыми
        *, 
        # все параметры справа от разделителя * становятся строго ключевым
        operation: str
) -> float:
    ...

