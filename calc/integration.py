import math

MAX_STEPS = 100000
DIGITS = 4

def f_ratio(x):
    
    return x / (x + 1)

def f_root(x):
    
    return math.sqrt(x * x + 1)


FUNCTIONS = {
    "ratio": (f_ratio, "F(x) = x / (x + 1)",    0, 20, True),
    "root":  (f_root,  "F(x) = sqrt(x^2 + 1)", -5,  5, False),
}

def integrate(func, a, b, steps):
    
    dx = (b - a) / steps
    r = 0
    for i in range(steps):
        r += func(a + i * dx) * dx
    return r