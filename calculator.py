import math

def add(a, b):
    return a + b

<<<<<<< HEAD
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
=======
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
>>>>>>> 29fa48e8d945d439c417e3792abb682db92cc3e6
