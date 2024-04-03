"""Демонстратор адаптера для одного класса."""

from abc import ABC, abstractmethod

import adapter1_external


class RasterInterface(ABC):
    """
    Описывает поля и методы, обязательные для реализации в классах, использующих растровые изображения.
    """
    @abstractmethod
    def draw(self):
        pass


class RasterImage(RasterInterface):
    def __init__(self, image_path: str):
        self.path = image_path
    
    def _get_image(self) -> str:
        return self.path.rsplit('.', 1)[-1]
    
    def draw(self) -> str:
        return f'Drawing {self._get_image()}'


class VectorToRasterAdapter(RasterInterface):
    """
    Специализированный адаптер векторного изображения к интерфейсу отображения растровых изображений.
    """
    def __init__(self, vector_image: adapter1_external.VectorImage):
        self.vector = vector_image
    
    def rasterize(self) -> str:
        return f'rasterized {self.vector.render()}'
    
    def draw(self):
        return f'Drawing {self.rasterize()}'



if __name__ == '__main__':
    img1 = RasterImage('figure1.png')
    img2 = RasterImage('background.jpg')
    
    # адаптируемый объект
    img3 = adapter1_external.VectorImage('diagram1.svg')
    # адаптированный объект
    img3_adapted = VectorToRasterAdapter(img3)
    
    gallery = [img1, img2, img3_adapted]
    for img in gallery:
        print(img.draw())

