# str() — человекочитаемое строковое представление
# repr() — машиночитаемое строковое представление

from decimal import Decimal as dec


def func():
    pass


print(
    f'{str(None) = }\t{repr(None) = }',
    f'{str(12) = }\t{repr(12) = }',
    f'{str(3.3) = }\t{repr(3.3) = }',
    f'{str(True) = }\t{repr(True) = }',
    f'{str(False) = }\t{repr(False) = }',
    f'{str("PYTHON") = }\t{repr("PYTHON") = }',
    f'{str(dec("4.4")) = }\t{repr(dec("4.4")) = }',
    f'{str([5, 6]) = }\t{repr([5, 6]) = }',
    f'{str(func) = }\t{repr(func) = }',
    sep='\n'
)

