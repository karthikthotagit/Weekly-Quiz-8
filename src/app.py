from math import log, sqrt, sin, cos

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b

def square(a):
    return a * a

def sqrtFunc(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number.")
    return sqrt(a)

def logFunc(x, base=None):
    if x <= 0:
        raise ValueError("Log domain error: x must be > 0.")
    if base is None:
        return log(x)
    if base <= 0 or base == 1:
        raise ValueError("Invalid log base. base must be > 0 and != 1.")
    return log(x) / log(base)

def sinFunc(x):
    return sin(x)

def cosFunc(x):
    return cos(x)

def percentage(part, whole=None):
    if whole is None:
        return part / 100.0
    if whole == 0:
        raise ZeroDivisionError("Cannot compute percentage with whole == 0.")
    return (part / whole) * 100.0

__all__ = [
    "add",
    "sub",
    "mul",
    "div",
    "square",
    "sqrtFunc",
    "logFunc",
    "sinFunc",
    "cosFunc",
    "percentage",
]
