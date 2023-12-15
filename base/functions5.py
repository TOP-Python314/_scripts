flag = False
for num1 in range(2, 10):
    for num2 in range(2, 10):
        if num1 * num2 > 15:
            flag = True
            break
    if flag:
        break
print(f'минимальные числа, произведение которых больше 15: {num1} и {num2}')
# минимальные числа, произведение которых больше 15: 2 и 8


def min_numbers_for_product(product: int) -> tuple[int, int]:
    half = product // 2
    for num1 in range(2, half):
        for num2 in range(2, half):
            if num1 * num2 > product:
                return num1, num2

product = 15
num1, num2 = min_numbers_for_product(product)
print(f'минимальные числа, произведение которых больше {product}: {num1} и {num2}')
# минимальные числа, произведение которых больше 15: 3 и 6
