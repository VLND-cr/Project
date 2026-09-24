import math

MAX_TERMS = 10000             # предел параметра --terms
MAX_EPS = 0.0001              # наибольшая допустимая точность
MAX_ITERATIONS = 100000       # предел повторений цикла по точности
DIGITS = math.ceil(-math.log10(MAX_EPS))  # число знаков вывода

def sign(n):
    
    return -1 if n % 2 == 0 else 1

def term_sqplus(n):
    
    return sign(n) / (n * n + 1)

def term_third(n):
    
    return sign(n) / (3 * n)

FORMULAS = {
    "sqplus": (term_sqplus, "S = 1/(1^2+1) - 1/(2^2+1) + 1/(3^2+1) - ..."),
    "third":  (term_third,  "S = 1/3 - 1/6 + 1/9 - ..."),
}

def sum_by_count(term, count):
    
    r = 0
    for n in range(1, count + 1):
        r += term(n)
    return r

def sum_by_eps(term, eps):
    
    r = 0
    n = 0
    while True:
        n += 1
        value = term(n)
        r += value
        if abs(value) < eps:
            return r, n
        if n >= MAX_ITERATIONS:
            raise ValueError("точность не достигнута")