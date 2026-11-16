import math

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b

def logarithm(a, b):
    try:
        return math.log(b,a)
    except(ValueError,ZeroDivisionError):
        raise ValueError

def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        raise ValueError

def hypotenuse(a, b):
    math.hypot(a, b)

def sub(a, b):
    return a -b

def mul(a, b):
    a * b

def exp(a, b):
    return a ** b

