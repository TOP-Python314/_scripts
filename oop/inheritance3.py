from re import compile, Pattern


class Person:
    _pattern_name: Pattern = compile(r'(?P<name>[А-ЯЁа-яё]+)(-(?P=name))?')
    
    def __init__(
            self, 
            last_name: str, 
            first_name: str, 
            patr_name: str,
    ):
        for name in (last_name, first_name, patr_name):
            if not self._pattern_name.fullmatch(name):
                raise ValueError
        self.last_name = last_name
        self.first_name = first_name
        self.patr_name = patr_name
    
    def __repr__(self):
        return f'{self.last_name} {self.first_name} {self.patr_name}'


class Student(Person):
    def __init__(
            self, 
            last_name: str, 
            first_name: str, 
            patr_name: str,
            group_number: str,
    ):
        # вызов метода родительского класса со ссылкой на текущий экземпляр
        super().__init__(last_name, first_name, patr_name)
        # то же самое — но явное использование идентификатора класса нежелательно
        # Person.__init__(self)
        
        self.group = group_number


class Teacher(Person):
    def __init__(
            self, 
            last_name: str, 
            first_name: str, 
            patr_name: str,
            group: str,
            *groups: str,
    ):
        super().__init__(last_name, first_name, patr_name)
        self.groups: tuple[str, ...] = (group, *groups)


group = 'ФТИ-32301'
students = [
    Student('Первов', 'Студент', 'Тестович', group),
    Student('Второв', 'Студент', 'Тестович', group),
    Student('Третьев', 'Студент', 'Тестович', group),
]
teach = Teacher('Скрытнов', 'Имярек', 'Имярекович', group)
