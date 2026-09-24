import math

MAX_COUNT = 20   
MAX_ABS = 10000   

def total(values):
   
    r = 0
    for v in values:
        r += v
    return r

def mean(values):
    
    return total(values) / len(values)

def sum_squares(values):
    
    r = 0
    for v in values:
        r += v * v
    return r

def rms(values):
    
    return math.sqrt(sum_squares(values) / len(values))

def variance(values):
    
    m = mean(values)
    r = 0
    for v in values:
        r += (v - m) ** 2
    return r / len(values)

def sko(values):
    
    return math.sqrt(variance(values))

def stdev(values):
    
    if len(values) < 2:
        return None
    m = mean(values)
    r = 0
    for v in values:
        r += (v - m) ** 2
    return math.sqrt(r / (len(values) - 1))

def minimum(values):
    
    r = values[0]
    for v in values:
        if v < r:
            r = v
    return r

def maximum(values):
    
    r = values[0]
    for v in values:
        if v > r:
            r = v
    return r

def positive_count(values):
    
    r = 0
    for v in values:
        if v > 0:
            r += 1
    return r

def negative_count(values):
   
    r = 0
    for v in values:
        if v < 0:
            r += 1
    return r
