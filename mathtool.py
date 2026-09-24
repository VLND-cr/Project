import sys, math

from calc import equation, series, stats, integration
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
    """Проверяет список чисел на допустимость."""
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

# ---------- обработчик integrate ----------

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



HANDLERS = {
    "solve":     handle_solve,
    "stats":     handle_stats,
    "series":    handle_series,
    "integrate": handle_integrate,
}

def main(argv):
    
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command is None:
        parser.print_help()
        return 0
    try:
        return HANDLERS[args.command](args)
    except (ValueError, OSError) as error:
        print(f"ОШИБКА: {error}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))