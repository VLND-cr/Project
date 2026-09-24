import sys, math

MAX_VALUE = 10000

try:
    if len(sys.argv) == 2:
        a = int(input("Введите A: "))
        b = int(input("Введите B: "))
        c = int(input("Введите C: "))
    elif len(sys.argv) == 8 and sys.argv[2] == '-a' and sys.argv[4] == '-b' and sys.argv[6] == '-c':
        a, b, c = int(sys.argv[3]), int(sys.argv[5]), int(sys.argv[7])
    else:
        raise ValueError("ОШИБКА: неверный набор параметров")
except ValueError:
    raise ValueError('ОШИБКА: коэффициент не является целым числом')
    



if abs(a) > MAX_VALUE or abs(b) > MAX_VALUE or abs(c) > MAX_VALUE:
    raise ValueError("ОШИБКА: значение вне допустимого диапазона")
     

    
if a == 0:
    if b == 0:
        raise ValueError ('ОШИБКА: это не уравнение, неизвестное отсутствует')
    print("Уравнение линейное")
    print(f"x = {int(-c/b)}")
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