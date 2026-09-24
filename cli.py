

import argparse

from calc import series, integration

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