import sys, math

MAX_VALUE = 10000

def check_coefficients(coefficients):
    
    for name, value in coefficients.items():
        if abs(value) > MAX_VALUE:
            raise ValueError(f"коэффициент {name} вне допустимого диапазона")

def solve(a, b, c):
    
    if a == 0:
        if b == 0:
            raise ValueError("это не уравнение, неизвестное отсутствует")
        return "линейное", None, [-c / b]

    d = b * b - 4 * a * c
    if d < 0:
        return "квадратное", d, []
    if d == 0:
        return "квадратное", d, [-b / (2 * a)]
    return "квадратное", d, [(-b + math.sqrt(d)) / (2 * a),
                             (-b - math.sqrt(d)) / (2 * a)]

