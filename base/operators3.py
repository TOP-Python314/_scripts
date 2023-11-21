# >>> var1 = 'Python'
# >>> var2 = 'C++'

# >>> id(var1)
# 140729902205008
# >>>
# >>> id(var2)
# 3061168190640

# >>> var3 = 'Python'
# >>>
# сработало кэширование
# >>> id(var3)
# 140729902205008


# >>> var1 = ['python', 3]
# >>> var3 = ['python', 3]
# >>>
# >>> id(var1)
# 3061171220864
# >>> id(var3)
# 3061171239872
# >>>
# >>> var1
# ['python', 3]
# >>> var3
# ['python', 3]
# >>>
# >>> var1 == var3
# True
# >>> var1 is var3
# False


# >>> var2
# 'C++'
# >>> var4 = 'C++'
# >>>
# >>> var2 == var4
# True
# >>> var2 is var4
# False
# >>>
# >>> id(var2)
# 3061168190640
# >>> id(var4)
# 3061171292848


# один оператор: is not
# >>> var1 is not var3
# True

# два оператора: is и not
# >>> not var1 is var3
# True


# >>> n1 = 17
# >>> n2 = 17
# >>>
# >>> n1 is n2
# True

# >>> id(n1)
# 140729903605032

# сработало кэширование
# >>> id(n2)
# 140729903605032

