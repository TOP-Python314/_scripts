def table_format(
        column1: 'Iterable',
        *columns: 'Iterable',
        v_sep: str = ' ',
        align: str = '>'
) -> str:
    # в развёрнутых строках документации для детального описания сигнатуры функции может использоваться синтаксис разметки reStructuredText
    """Принимает один и более столбцов произвольных данных. Возвращает строковое табличное представление данных.
    
    Количество строк таблицы ограничивается количеством элементов в самом коротком переданном столбце.
    
    :param column1: итерируемый объект с произвольными элементами
    :param columns: произвольное количество итерируемых объектов
    :param v_sep: вертикальный разделитель столбцов таблицы
    :param align: горизонтальное выравнивание данных в столбце; допустимые значения: '<' - влево, '^' - по центру, '>' - вправо
    """
    # добавление обязательного столбца таблицы в кортеж
    columns = column1, *columns
    # подсчёт наибольшего количества символов в каждом столбце таблицы
    c_width = [
        max(len(str(cell)) for cell in col)
        for col in columns
    ]
    cnt_cols = len(columns)
    return '\n'.join([
        # формирование одной строки таблицы
        v_sep.join(
            f'{row[i]:{align}{c_width[i]}}' 
            # i - индекс столбца таблицы
            for i in range(cnt_cols)
        )
        for row in zip(*columns)
    ])


def full_table_format(
        column1: list | tuple | range,
        *columns: list | tuple | range,
        v_sep: str = ' ',
        align: str = '>'
) -> str:
    """Принимает один и более столбцов произвольных данных. Возвращает строковое табличное представление данных.
    
    Количество строк таблицы равно количеству элементов в самом длинном переданном столбце.
    
    :param column1: последовательность с произвольными элементами
    :param columns: произвольное количество последовательностей
    :param v_sep: вертикальный разделитель столбцов таблицы
    :param align: горизонтальное выравнивание данных в столбце; допустимые значения: '<' - влево, '^' - по центру, '>' - вправо
    """
    columns = column1, *columns
    cnt_cols = len(columns)
    
    c_width, c_len = [], []
    for col in columns:
        c_width.append(max(len(str(cell)) for cell in col))
        c_len.append(len(col))
    
    rows = []
    # i - индекс строки таблицы
    for i in range(max(c_len)):
        # получение данных для строки таблицы
        row = []
        for col in columns:
            try:
                row.append(col[i])
            except IndexError:
                row.append('')
        # формирование строки таблицы
        rows.append(v_sep.join(
            f'{row[j]:{align}{c_width[j]}}' 
            # j - индекс столбца таблицы
            for j in range(cnt_cols)
        ))
    
    return '\n'.join(rows)


# тестовые данные
table_of_numbers = [
    list(range(i, i+7)) 
    for i in range(-179, 1500, 180)
]

# >>> print(table_format(*table_of_numbers))
# -179 1 181 361 541 721 901 1081 1261 1441
# -178 2 182 362 542 722 902 1082 1262 1442
# -177 3 183 363 543 723 903 1083 1263 1443
# -176 4 184 364 544 724 904 1084 1264 1444
# -175 5 185 365 545 725 905 1085 1265 1445
# -174 6 186 366 546 726 906 1086 1266 1446
# -173 7 187 367 547 727 907 1087 1267 1447

# тестовые данные
data = [
    range(1, 7),
    ['тут', 'слово', 'разве это длиннно?', 'пфф', 'ещё строка'],
    (3, 5, 18, 3),
]

# >>> print(table_format(*data, v_sep=' | ', align='^'))
# 1 |        тут         | 3
# 2 |       слово        | 5
# 3 | разве это длиннно? | 18
# 4 |        пфф         | 3

# >>> print(full_table_format(*data, v_sep=' | ', align='^'))
# 1 |        тут         | 3
# 2 |       слово        | 5
# 3 | разве это длиннно? | 18
# 4 |        пфф         | 3
# 5 |     ещё строка     |
# 6 |                    |
