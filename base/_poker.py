# старшая карта
# (2, 4, 10, 14, 5)
# пара
# (5, 7, 10, 4, 5)
# две пары
# (4, 5, 6, 6, 5)
# сет
# (7, 7, 2, 14, 7)
# стрит
# (4, 5, 6, 7, 8)
# фулл-хаус
# (4, 5, 4, 4, 5)
# каре
# (5, 5, 5, 4, 5)


# длинные аннотации сохраняются в отдельные переменные
FiveCards = tuple[int, int, int, int, int]


def combination(hand: FiveCards) -> str:
    """В переданной последовательности номиналов пяти карт находит самую старшую комбинацию покера (техасский холдем)."""
    unique_cards = set(hand)
    uniques = len(unique_cards)
    
    if uniques == 4:
        return 'пара'
    
    max_count = max(hand.count(card) for card in unique_cards)
    if uniques == 3:
        if max_count == 2:
            return 'две пары'
        elif max_count == 3:
            return 'сет'
    
    # if sorted(hand) == list(range(min(hand), min(hand)+5)):
    #     return 'стрит'
    
    if uniques == 5 and max(hand) - min(hand) == 4:
        return 'стрит'
    
    if uniques == 2:
        if max_count == 3:
            return 'фулл-хаус'
        elif max_count == 4:
            return 'каре'
    
    return 'старшая карта'


def get_hand() -> FiveCards:
    """Возвращает кортеж из пяти целых чисел, полученных из одной строки стандартного потока ввода (stdin)."""
    return tuple(int(card) for card in input(' > ').strip().split())


# >>> get_hand()
#  > 9 3 8 9 12
# (9, 3, 8, 9, 12)
# >>>
#>>> combination(get_hand())
# > 9 3 8 9 12
#'пара'
# >>>
# >>> combination([10, 5, 10, 10, 6])
# 'сет'
# >>>
# >>> combination
# <function combination at 0x00000141A174EFC0>
# >>>
# >>> combination.__name__
# 'combination'
# >>>
# >>> combination.__doc__
# 'В переданной последовательности номиналов пяти карт находит самую старшую комбинацию покера (техасский холдем).'
# >>>
# >>> get_hand.__doc__
# 'Возвращает кортеж из пяти целых чисел, полученных из одной строки стандартного потока ввода (stdin).'