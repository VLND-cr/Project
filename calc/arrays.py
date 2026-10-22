import random

MIN_VALUE = -100
MAX_VALUE = 100
MAX_COUNT = 1000000
MAX_SEARCH = 1000

#создание списка случайных чисел
def fill(count, low=MIN_VALUE, high= MAX_VALUE, seed=None):
    random.seed(seed)
    values = []
    for _ in range(count):
        values.append(random.randint(low, high))
    return values

def check_values(values):
    if not values:
        raise ValueError('последовательность пуста')
    if len(values) > MAX_COUNT:
        raise ValueError(f'количесвто элементов вне диапозона 1..{MAX_COUNT}')
    for value in values:
        if value < MIN_VALUE or value > MAX_VALUE:
            raise ValueError(
                f'Значение {value} вне диапозона {MIN_VALUE}..{MAX_VALUE}'
            )


