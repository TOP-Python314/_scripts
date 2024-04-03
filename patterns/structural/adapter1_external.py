"""Демонстратор адаптера для одного класса — внешний модуль"""


class VectorImage:
    def __init__(self, image_path: str):
        self.path = image_path
    
    def render(self):
        return 'svg'

