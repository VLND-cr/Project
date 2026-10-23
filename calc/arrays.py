import random

MIN_VALUE = -100
MAX_VALUE = 100
MAX_COUNT = 1_000_000
MAX_SEARCH = 1000

def fill(count, low=MIN_VALUE, high=MAX_VALUE, seed=None):
    """Создаёт список случайных целых чисел."""
    random.seed(seed)
    values = []
    for _ in range(count):
        values.append(random.randint(low, high))
    return values

def check_values(values):
    """Проверяет количество и диапазон значений массива."""
    if not values:
        raise ValueError("последовательность пуста")
    if len(values) > MAX_COUNT:
        raise ValueError(f"количество элементов вне диапазона 1..{MAX_COUNT}")
    for value in values:
        if value < MIN_VALUE or value > MAX_VALUE:
            raise ValueError(
                f"значение {value} вне диапазона {MIN_VALUE}..{MAX_VALUE}"
            )

def check_sorted_ascending(values):
    """Проверяет, что массив упорядочен по возрастанию."""
    for i in range(len(values) - 1):
        if values[i] > values[i + 1]:
            raise ValueError("массив не упорядочен по возрастанию")

def binary_search(values, target):
    """Возвращает индекс target в упорядоченном массиве или None."""
    left = 0
    right = len(values) - 1

    while left <= right:
        middle = (left + right) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return None