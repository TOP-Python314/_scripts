def adder(num1, num2):
    print(f'{num1 = }   {num2 = }')
    return num1 + num2


# >>> adder(1, 7)
# num1 = 1   num2 = 7
# 8
# >>>
# >>> adder(12, -12)
# num1 = 12   num2 = -12
# 0
# >>>
# >>> adder(12)
# ...
# TypeError: adder() missing 1 required positional argument: 'num2'
# >>>
# >>> adder(25, 25, 25)
# ...
# TypeError: adder() takes 2 positional arguments but 3 were given


def multiplier(num1: float, num2: float) -> float:
    return num1 * num2


# >>> multiplier(2, 7.5)
# 15.0
# >>>
# >>> multiplier('abc', 4)
# 'abcabcabcabc'


def test_arguments(par1, par2, par3) -> None:
    print(
        'test_arguments',
        f'    {par1 = }',
        f'    {par2 = }',
        f'    {par3 = }',
        sep='\n'
    )


# >>> test_arguments('a', 'b', 'c'*3)
# test_arguments
#     par1 = 'a'
#     par2 = 'b'
#     par3 = 'ccc'
# >>>
# >>> test_arguments(par1=(1,), par2=[2], par3={3})
# test_arguments
#     par1 = (1,)
#     par2 = [2]
#     par3 = {3}
# >>>
# >>> test_arguments(par3=(1,), par1=[2], par2={3})
# test_arguments
#     par1 = [2]
#     par2 = {3}
#     par3 = (1,)
# >>>
# >>> test_arguments((1,), par3=[2], par2={3})
# test_arguments
#     par1 = (1,)
#     par2 = {3}
#     par3 = [2]
# >>>
# >>> test_arguments('x', 'y', par2='z')
# ...
# TypeError: test_arguments() got multiple values for argument 'par2'
# >>>
# >>> test_arguments(par2='z', 'x', 'y')
# ...
# SyntaxError: positional argument follows keyword argument
