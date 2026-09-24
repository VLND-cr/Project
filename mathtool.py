import sys, math

from calc import equation, series, stats 
from cli import build_parser


def handle_solve(args):
    """Решает уравнение, печатает результат, возвращает код."""
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
    """Читает числа из файла или со стандартного ввода."""
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



