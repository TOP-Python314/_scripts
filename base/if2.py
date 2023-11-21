word = input('введите слово > ').lower()

if 'Я' < word < 'б':
    print('слово на букву "а"')

elif word < 'в':
    print('слово на букву "б"')

elif word < 'г':
    print('слово на букву "в"')

# ...

else:
    print('это не слово')

