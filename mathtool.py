import sys, math

from calc import quation


if len(sys.argv) == 1 or sys.argv[1] == '--help':
    print("mathtool — решение уравнений вида A*x^2 + B*x + C = 0\n")
    print("Использование:")
    print("  python mathtool.py                         вывод справки")
    print("  python mathtool.py --help                  вывод справки")
    print("  python mathtool.py solve                   ввод коэффициентов с клавиатуры")
    print("  python mathtool.py solve -a 1 -b -3 -c 2   решение с заданными коэффициентами\n")
    print("Коэффициенты A, B, C — целые числа, по модулю не превышающие 10000.")
    sys.exit(0)

if sys.argv[1] != 'solve':
    print("ОШИБКА: неизвестная команда", file=sys.stderr)
    sys.exit(1)


