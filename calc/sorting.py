from .arrays import MIN_VALUE, MAX_VALUE

METHODS = {}

def _out_of_order(a, b, descending):
    """Возвращает True, если a и b стоят не в нужном порядке."""
    if descending:
        return a < b
    return a > b

def bubble_sort(array, descending=False):
    """Сортировка пузырьком. Изменяет array, возвращает None."""
    n = len(array)

    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if _out_of_order(array[j], array[j + 1], descending):
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break

    return None

METHODS["bubble"] = bubble_sort

def selection_sort(array, descending=False):
    """Сортировка выбором. Изменяет array, возвращает None."""
    n = len(array)

    for i in range(n - 1):
        best = i
        for j in range(i + 1, n):
            if _out_of_order(array[best], array[j], descending):
                best = j
        array[i], array[best] = array[best], array[i]

    return None

METHODS["selection"] = selection_sort

def insertion_sort(array, descending=False):
    """Сортировка вставками. Изменяет array, возвращает None."""
    n = len(array)

    for i in range(1, n):
        current = array[i]
        j = i

        while j > 0 and _out_of_order(array[j - 1], current, descending):
            array[j] = array[j - 1]
            j -= 1

        array[j] = current

    return None

METHODS["insertion"] = insertion_sort

def counting_sort(array, descending=False):
    """Сортировка подсчётом. Изменяет array, возвращает None."""
    counters = [0] * (MAX_VALUE - MIN_VALUE + 1)

    for value in array:
        counters[value - MIN_VALUE] += 1
    k = 0
    if descending:
        indices = range(len(counters) - 1, -1, -1)
    else:
        indices = range(len(counters))

    for index in indices:
        for _ in range(counters[index]):
            array[k] = index + MIN_VALUE
            k += 1

    return None

METHODS["counting"] = counting_sort