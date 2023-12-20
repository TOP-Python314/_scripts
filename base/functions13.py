def filter(func_obj: 'function', iterable: 'iterable') -> list:
    results = []
    for elem in iterable:
        if func_obj(elem):
            results.append(elem)
    return results


def is_short(word: str) -> bool:
    """Предикат, возвращающий True для всех строк, длина которых строго меньше четырёх."""
    return len(word) < 4


def is_prime(number: int) -> bool:
    for div in range(2, int(number**0.5) + 1):
        if number % div == 0:
            return False
    return True


text = '''Каждый составленный запрос должен быть выполнен студентом на своём локальном сервере

Если запрос возвращает ошибку или некорректные данные, и все опечатки устранены, то необходимо обратиться к преподавателю за консультацией в личный чат Teams'''

# >>> filter(is_short, text.split())
# ['на', 'или', 'и', 'все', 'то', 'к', 'за', 'в', 'чат']

# >>> filter(is_prime, range(10, 100))
# [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
