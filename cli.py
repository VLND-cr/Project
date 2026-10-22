

import argparse

from calc import series, integration, arrays, sorting

def build_parser():
    """Создаёт и возвращает разборщик параметров."""
    parser = argparse.ArgumentParser(
        prog="mathtool",
        description="mathtool — расчёты над уравнениями и числовыми последовательностями",
        allow_abbrev=False,
    )
    subs = parser.add_subparsers(dest="command")

    # solve
    p = subs.add_parser("solve", help="решение уравнения A*x^2 + B*x + C = 0",
                        allow_abbrev=False)
    p.add_argument("-a", type=int, help="коэффициент A")
    p.add_argument("-b", type=int, help="коэффициент B")
    p.add_argument("-c", type=int, help="коэффициент C")

    # stats
    p = subs.add_parser("stats", help="показатели числовой последовательности",
                        allow_abbrev=False)
    p.add_argument("--input", help="файл с числами")

    #fill
    p = subs.add_parser(
        "fill",
        help = 'генерация случайного массива',
        allow_abbrev=False,
    )
    p.add_argument('-c', '--count', type=int, required=True, 
                   help="количество лементов")
    p.add_argument('--min', dest = 'min_value', type = int,
                   default=arrays.MIN_VALUE, help = 'нижняя граница значений')
    p.add_argument('--max', dest = 'max_value', type = int,
                   default=arrays.MAX_VALUE, help = "верхняя граница значений")
    p.add_argument('--seed', type = int, default=None,
                   help = 'начальное значение генератора')
    p.add_argument('-o', '--output', help = 'файл для созданного массива')

    #sort
    p = subs.add_parser(
        'sort',
        help = 'сортировка массива',
        allow_abbrev=False,
    )

    p.add_argument('-m', '--method', required= True,
                   choices = sorted(sorting.METHODS),
                   help = 'метод сортировки')
    p.add_argument('--order', choices=['asc', 'desc'], default='asc',
                   help = 'направление сортировки')
    p.add_argument('-i', '--input', help = 'файл с исходным массивом')
    p.add_argument('-o', '--output', help = 'файл для отсортированного массива')

    #search
    p =subs.add_parser(
        "search",
        help = 'двоичный поиск в упорядоченном массиве',
        allow_abbrev=False,
    )
    p.add_argument('-v', '--value', type = int, required=True,
                   help="искомое целое число")
    p.add_argument('-i', '--input', help = 'файл с массивом по возрастанию')

    # series
    p = subs.add_parser("series", help="сумма ряда", allow_abbrev=False)
    p.add_argument("--func", required=True, choices=sorted(series.FORMULAS),
                   help="имя ряда")
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--terms", type=int, help="число слагаемых")
    g.add_argument("--eps", type=float, help="точность")

    # integrate
    p = subs.add_parser("integrate", help="численное интегрирование",
                        allow_abbrev=False)
    p.add_argument("--func", required=True, choices=sorted(integration.FUNCTIONS),
                   help="имя функции")
    p.add_argument("--from", dest="start", type=float, required=True,
                   help="нижний предел")
    p.add_argument("--to", dest="end", type=float, required=True,
                   help="верхний предел")
    p.add_argument("--steps", type=int, required=True, help="число шагов")

    return parser