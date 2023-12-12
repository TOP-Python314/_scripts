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

hand = tuple(int(card) for card in input(' > ').split())
combination = 'старшая карта'

unique_cards = set(hand)
uniques = len(unique_cards)
max_count = max(hand.count(card) for card in unique_cards)

if uniques == 4:
    combination = 'пара'

elif uniques == 3:
    if max_count == 2:
        combination = 'две пары'
    elif max_count == 3:
        combination = 'сет'

# elif sorted(hand) == list(range(min(hand), min(hand)+5)):
#     combination = 'стрит'

elif uniques == 5 and max(hand) - min(hand) == 4:
    combination = 'стрит'

elif uniques == 2:
    if max_count == 3:
        combination = 'фулл-хаус'
    elif max_count == 4:
        combination = 'каре'

print(combination)
