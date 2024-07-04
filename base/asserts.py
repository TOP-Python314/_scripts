# >>> assert True
# >>> 
# >>> assert False
# AssertionError
# >>> 


def divide(n1, n2):
    return n1 // n2


def test_type(n1, n2):
    if type(n1) is type(n2) is int:
        assert type(divide(n1, n2)) is int
    
    elif type(n1) is float or type(n2) is float:
        assert type(divide(n1, n2)) is float


def test_zero():
    try:
        divide(1, 0)
    except ZeroDivisionError:
        assert True
    except Exception as exc:
        assert False, str(exc)
    else:
        assert False, 'деление на ноль должно вызывать ошибку'



if __name__ == '__main__':
    
    test_data = [
        (10, 3),
        (1, 7),
        (12, 6.0),
        (12.0, 6),
    ]
    for args in test_data:
        try:
            print(f'\ntest_data={args}')
            test_type(*args)
        except AssertionError as exc:
            print('ПРОВАЛЕН', exc)
        else:
            print('ПРОЙДЕН')
    
    try:
        print('\ntest_data=(1, 0)')
        test_zero()
    except AssertionError as exc:
        print('ПРОВАЛЕН', exc)
    else:
        print('ПРОЙДЕН')

