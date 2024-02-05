from sys import argv

print(*argv)

# > python stdlib7.py
# stdlib7.py

# > python -i stdlib7.py
# stdlib7.py

# > python stdlib7.py arg1
# stdlib7.py arg1

# > python -i stdlib7.py arg1 44
# stdlib7.py arg1 44
# >>> argv
# ['stdlib7.py', 'arg1', '44']
