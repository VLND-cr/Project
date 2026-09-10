import sys, math

M = 10000

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

try:
    if len(sys.argv) == 2:
        a = int(input("Введите A: "))
        b = int(input("Введите B: "))
        c = int(input("Введите C: "))
    elif len(sys.argv) == 8 and sys.argv[2] == '-a' and sys.argv[4] == '-b' and sys.argv[6] == '-c':
        a, b, c = int(sys.argv[3]), int(sys.argv[5]), int(sys.argv[7])
    else:
        print("ОШИБКА: неверный набор параметров", file=sys.stderr)
        sys.exit(1)
except ValueError:
    print("ОШИБКА: коэффициент не является целым числом", file=sys.stderr)
    sys.exit(1)

if abs(a) > M or abs(b) > M or abs(c) > M:
    print("ОШИБКА: значение вне допустимого диапазона", file=sys.stderr)
    sys.exit(1)

if a == 0:
    if b == 0:
        print("ОШИБКА: это не уравнение, неизвестное отсутствует", file=sys.stderr)
        sys.exit(1)
    print("Уравнение линейное")
    print(f"x = {-c/b:.3f}")
else:
    print("Уравнение квадратное")
    D = b*b - 4*a*c
    print(f"D = {D}")
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        print(f"x1 = {x1:.3f}\nx2 = {x2:.3f}")
    elif D == 0:
        print(f"x = {-b/(2*a):.3f}")
    else:
        print("Действительных корней нет")