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


