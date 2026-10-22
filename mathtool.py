import sys, math, time

from calc import equation, series, stats, integration, arrays, sorting
from cli import build_parser


def handle_solve(args):
    
    if args.a is None and args.b is None and args.c is None:
        a = int(input("Введите A: "))
        b = int(input("Введите B: "))
        c = int(input("Введите C: "))
    elif args.a is not None and args.b is not None and args.c is not None:
        a, b, c = args.a, args.b, args.c
    else:
        raise ValueError("нужно задать либо все три коэффициента, либо ни одного")

    equation.check_coefficients({"A": a, "B": b, "C": c})
    kind, d, roots = equation.solve(a, b, c)

    if kind == "линейное":
        print("Уравнение линейное")
        print(f"x = {int(roots[0])}")
        return 0

    print("Уравнение квадратное")
    print(f"Дискриминант: {d}")
    if len(roots) == 2:
        print(f"x1 = {roots[0]:.3f}")
        print(f"x2 = {roots[1]:.3f}")
    elif len(roots) == 1:
        print(f"x = {roots[0]:.3f}")
    else:
        print("Действительных корней нет")
    return 0


def read_numbers(path):
    
    if path:
        with open(path, encoding="utf-8-sig") as handle:
            lines = handle.readlines()
    else:
        lines = sys.stdin.readlines()

    values = []
    for line in lines:
        for word in line.split():
            try:
                values.append(float(word))
            except ValueError:
                raise ValueError(f"{word} не является числом")
    return values

def check_values(values):
    
    if not values:
        raise ValueError("последовательность пуста")
    if len(values) > stats.MAX_COUNT:
        raise ValueError("чисел больше допустимого")
    for v in values:
        if not math.isfinite(v):
            raise ValueError("значение не является конечным")
        if abs(v) > stats.MAX_ABS:
            raise ValueError("значение по модулю больше допустимого")


REPORT = [
    ("Количество",     len,                   "d"),
    ("Сумма",          stats.total,           ".3f"),
    ("Ср. арифм.",     stats.mean,            ".3f"),
    ("Сумма кв.",      stats.sum_squares,     ".3f"),
    ("Ср. кв.",        stats.rms,             ".3f"),
    ("Дисперсия",      stats.variance,        ".3f"),
    ("СКО",            stats.sko,             ".3f"),
    ("Станд. откл.",   stats.stdev,           ".3f"),
    ("Наименьшее",     stats.minimum,         ".3f"),
    ("Наибольшее",     stats.maximum,         ".3f"),
    ("Положительных",  stats.positive_count,  "d"),
    ("Отрицательных",  stats.negative_count,  "d"),
]

def handle_stats(args):
    
    values = read_numbers(args.input)
    check_values(values)
    for label, func, fmt in REPORT:
        value = func(values)
        if value is None:
            print(f"{label}: НЕ СУЩЕСТВУЕТ")
        else:
            print(f"{label}: {value:{fmt}}")
    return 0

def handle_series(args):
    
    term, formula = series.FORMULAS[args.func]

    
    if args.terms is not None:
        if not 1 <= args.terms <= series.MAX_TERMS:
            raise ValueError("количество слагаемых вне диапазона")
    else:
        if not (math.isfinite(args.eps) and 0 < args.eps <= series.MAX_EPS):
            raise ValueError("точность вне диапазона")

    print(formula)
    if args.terms is not None:
        result = series.sum_by_count(term, args.terms)
        count = args.terms
    else:
        result, count = series.sum_by_eps(term, args.eps)
    print(f"Слагаемых: {count}")
    print(f"Сумма ряда: {result:.{series.DIGITS}f}")
    return 0

#обработчик integrate

def handle_integrate(args):
    
    func, formula, low, high, closed = integration.FUNCTIONS[args.func]
    a, b = args.start, args.end

   
    if not (math.isfinite(a) and math.isfinite(b)):
        raise ValueError("предел не является конечным числом")
    if a >= b:
        raise ValueError("начальный предел не меньше конечного")
    if closed:
        outside = a < low or b > high
    else:
        outside = a <= low or b >= high
    if outside:
        raise ValueError("предел вне промежутка")
    if not 1 <= args.steps <= integration.MAX_STEPS:
        raise ValueError("количество шагов вне диапазона")

    print(formula)
    value = integration.integrate(func, a, b, args.steps)
    print(f"Значение интеграла: {value:.{integration.DIGITS}f}")
    return 0

def read_array(path):
    if path:
        with open(path, encoding="utf-8-sig") as handle:
            text = handle.read()
    else:
        lines = []
        print("Введите массив (пустая строка - конец):",
              file = sys.stderr, end = "")

        while True:
            try:
                line = input()
            except EOFError:
                break
            if not line.strip():
                break
            lines.append(line)

        text = text.replace(',','')
        words = text.split()

        values = []
        for word in words:
            try:
                values.append(int(word))
            except ValueError:
                raise ValueError(f'{word} не является целым числом')

        arrays.check_values(values)
        return values

def write_array(path, values):
    with open(path,'w', encoding="utf-8") as handle:
        handle.write(''.join(str(x) for x in values) + '\n')

def print_array(path, values):
    print(' '.join(str(x) for x in values))

def measure(name, operation, parameters):
    start = time.perf_counter()
    result = operation(*parameters)
    elapsed = time.perf_counter()-start

    print(
        f'Время операции {name}: {elapsed:.6f} c',
        file = sys.stderr
    )
    

#обработчик fill
def handle_fill(args):
    if not 1<= args.count <= arrays.MAX_COUNT:
        raise ValueError(f'количество элементов вне диапозона 1..{arrays.MAX_COUNT}')
    if args.min_value < arrays.MIN_VALUE or args.max_value >arrays.MAX_VALUE:
        raise ValueError(
            f'границы значений вне диапозона'
            f'{arrays.MIN_VALUE}..{arrays.MAX_VALUE}'
        )
    if args.min_value > args.max_value:
        raise ValueError("минимум больше максимума")

    values = arrays.fill(
        args.count,
        args.min_value,
        args.max_value,
        args.seed,
    )

    if args.output:
        write_array(args.output, values)
        print(f"Записано элементов: {len(values)} в файл {args.output}")
    else:
        print_array(values)
    return 0 

#обраюотчик sort
def handle_sort(args):
    values = read_array(args.input)
    method = sorting.METHODS[args.method]
    descending = args.order == 'desc'

    measure(f'sort({args.method})', method, [values, descending])

    if args.output:
        write_array(args.output, values)
        print(f'Записано элементов: {len(values)} в файл {args.output}')
    else:
        print_array(values)

    print("Массив отсортирован")
    return 0

#обработчик двоичного поиска
def handle_search(args):
    if abs(args.value) > arrays.MAX_SEARCH:
        raise ValueError(
            f'Модуль искомого значения больше {arrays.MAX_SEARCH}'
        )
    values = read_array(args.input)
    arrays.check_sorted_ascending(values)
    index = arrays.binary_search(values, args.value)
    if index is None:
        print(f'Значение {args.value} не найдено')
        return 1
    print(f'Значение {args.value} имккет элемент с индексом {index + 1}.')
    return 0

HANDLERS = {
    # Словарь «имя команды → функция-обработчик».
    # Имена функций без скобок — это сами функции.
    "solve":     handle_solve,
    "stats":     handle_stats,
    "series":    handle_series,
    "integrate": handle_integrate,
    "fill": handle_fill,
    'sort': handle_sort,
    'search': handle_search,
}

def main(argv):
    """Разбирает параметры, вызывает обработчик, возвращает код."""
    parser = build_parser()                       # создаём разборщик
    args = parser.parse_args(argv)                # разбор списка параметров без имени программы
                                                  # при ошибке argparse сам завершит работу с кодом 2
    if args.command is None:                      # команда не указана
        parser.print_help()                       # печатаем справку в stdout
        return 0                                  
    try:                                          # пробуем выполнить команду
        return HANDLERS[args.command](args)       # вызов обработчика по имени команды
    except (ValueError, OSError) as error:        # ValueError — ошибки в данных,
                                                  # OSError — несуществующий файл в stats
        print(f"ОШИБКА: {error}", file=sys.stderr)   
        return 1                                  

if __name__ == "__main__":                        # только при прямом запуске файла
                                                  # при импорте __name__ не равен "__main__"
    sys.exit(main(sys.argv[1:]))                  # единственный sys.exit во всём приложении
                                                  