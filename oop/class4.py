class Book:
    def __init__(self, title: str, author1: str, *authors: str):
        self.title = title
        self.authors = [author1, *authors]
    
    def constructor(self, description: str):
        self.description = description


# при вызове объекта класса вызывается метод __call__() метакласса type 
# Book(*args, **kwargs)
#   |
#   V
# def type.__call__(Book, *args, **kwrags):
#     instance = Book.__new__(*args, **kwargs)
#     instance.__init__(*args, **kwargs)
#     return instance


besy = Book('Бесы', 'Достоевский Ф.М.')

# >>> besy.__dict__
# {'title': 'Бесы', 'authors': ['Достоевский Ф.М.']}

# >>> besy.constructor('О влиянии либеральных идей на различные слои общества Российской империи второй половины XIX в.')
# >>> besy.__dict__
# {'title': 'Бесы', 'authors': ['Достоевский Ф.М.'], 'description': 'О влиянии либеральных идей на различные слои общества Российской империи второй половины XIX в.'}
