import math

def add(a, b):
    return a + b

def sub(a, b):
    return a -b

def mul(a, b):
    a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError('Cannot divide by 0')
    else:
        return b / a

def log(a, b):
    if a <= 0:
        raise ValueError('Logarithm base must be greater than 0')
    if a == 1:
        raise ValueError('Log base cannot be 1')
    if b <= 0:
        raise ValueError('Log argument must be greater than 0')
    return math.log(b, a)

def exp(a, b):
    return a ** b
