class Person:
    def __init__(
            self, 
            last_name: str, 
            first_name: str, 
            patr_name: str
    ):
        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.patr_name = patr_name.title()
    
    @property
    def fio(self) -> str:
        return f'{self.last_name} {self.first_name} {self.patr_name}'
    
    @property
    def io(self) -> str:
        return f'{self.first_name} {self.patr_name}'
    
    @property
    def initials_first(self) -> str:
        return f'{self.first_name[0]}. {self.patr_name[0]}. {self.last_name}'
    
    @property
    def initials_last(self) -> str:
        return f'{self.last_name} {self.first_name[0]}. {self.patr_name[0]}.'


timofey = Person('Озеров', 'Тимофей', 'Валерианович')

# >>> timofey.fio
# 'Озеров Тимофей Валерианович'
# >>>
# >>> timofey.io
# 'Тимофей Валерианович'
# >>>
# >>> timofey.initials_last
# 'Озеров Т. В.'
# >>>
# >>> timofey.initials_first
# 'Т. В. Озеров'
