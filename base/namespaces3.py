codes = ('04fa', '04d1', '051b')
print(f'\n{globals() = }')


def function1():
    print(f'\nвнутри function1\n\t{locals() = }')
    print(codes)


def function2():
    codes = 'локальная переменная'
    print(f'\nвнутри function2\n\t{locals() = }')
    print(codes)


function1()
function2()

print(f'\n{globals() = }')


def function3():
    try:
        print(f'\n{codes = }')
    except UnboundLocalError: 
        print('\nнельзя обращаться к глобальной переменной и создавать одноимёную локальную переменную в локальном пространстве имён')
    codes = 'локальная переменная'
    print(f'\nвнутри function3\n\t{locals() = }')


function3()


def function4():
    global codes
    print(f'\n{codes = }')
    codes = 'локальная переменная'
    print(f'\nвнутри function4\n\t{locals() = }')


function4()

print(f'\n{globals() = }')

