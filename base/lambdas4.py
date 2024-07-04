funcs = []
for n in range(5, 10):
    funcs.append(
        lambda: print(n)
    )

for func in funcs:
    # каждая функция обращается к одному и тому же n в пространстве имён модуля (глобальном)
    func()

print()

funcs2 = []
for n in range(5, 10):
    funcs2.append(
        # каждое n помещается в локальное пространство имён каждой функции
        lambda q=n: print(q)
    )

for func in funcs2:
    func()

