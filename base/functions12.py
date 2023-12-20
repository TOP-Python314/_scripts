def map(func_obj: 'function', iterable: 'iterable') -> list:
    """Функция высшего порядка, которая для каждого элемента переданного итерируемого объекта вызывает переданную функцию. Результаты возвращаются в виде списка.
    
    Передаваемая функция должна принимать один позиционный аргумент."""
    results = []
    for elem in iterable:
        results.append(func_obj(elem))
    return results


def cube(number: int) -> int:
    return number**3


def syllables(word: str) -> str:
    return '-'.join(
        word[i:i+2]
        for i in range(0, len(word), 2)
    )


# >>> cube
# <function cube at 0x000001D799B1F060>
# >>>
# >>> map(cube, range(2, 10))
# [8, 27, 64, 125, 216, 343, 512, 729]

# >>> syllables
# <function syllables at 0x000001D799B1F100>
# >>> 
# >>> map(syllables, ['мама', 'книга', 'самовар'])
# ['ма-ма', 'кн-иг-а', 'са-мо-ва-р']
