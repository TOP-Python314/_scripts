title = '\n\n{} цикл'
prompt = '\nвведите команду > '
stop_word = 'выход'
cycle_end = '\nцикл завершён'


print(title.format('первый'))
command = input(prompt)
# условие продолжения цикла
while command != stop_word:
    print(command.upper())
    command = input(prompt)
else:
    print(cycle_end)


print(title.format('второй'))
while True:
    # условие выхода из цикла
    command = input(prompt)
    if command == stop_word:
        break
    print(command.upper())
else:
    print(cycle_end)


print(title.format('третий'))
# Python 3.8+
while (command := input(prompt)) != stop_word:
    print(command.upper())
else:
    print(cycle_end)

