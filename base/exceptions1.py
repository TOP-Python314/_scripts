# try:
#     <потенциально_опасный_блок>
# 
# except <тип1_исключения>:
#     <блок_выполняемый_при_перехвате_1>
# 
# except <тип2_исключения>:
#     <блок_выполняемый_при_перехвате_2>
# 
# ...
# 
# else:
#     <блок_выполняемый_при_отсутствии_исключений>
# 
# finally:
#     <блок_выполняемый_при_любом_исходе>


n1, n2 = int(input(' > ')), int(input(' > '))

try:
    res = n1 / n2
except NameError:
    print('переменные не объявлены')
except ZeroDivisionError:
    print('деление на ноль невозможно')
else:
    print(f'{res = }')
finally:
    print('конец')

