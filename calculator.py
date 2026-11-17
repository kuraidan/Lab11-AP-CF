# https://github.com/kuraidan/Lab11-AP-CF
# Partner 1: Christian Fernandez
# Partner 2 : Aidan Przybylski

import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def logarithm(a, b):
    try:
        return math.log(a,b)
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

def div(a, b):
    if a == 0:
        raise ZeroDivisionError('Cannot divide by 0')
    else:
        return b / a

def exp(a, b):
    return a ** b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("a cannot be 0")
    return b / a

