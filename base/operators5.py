def true():
    print('истина')
    return True


def false():
    print('ложь')
    return False


true() or true() or false()
# истина

print()

false() or false() or true() or false()
# ложь
# ложь
# истина

print()

true() and true() and false()
# истина
# истина
# ложь

print()

false() and true()
# ложь
