from math import log as _log, sqrt as _sqrt, sin as _sin, cos as _cos
from typing import Optional

def add(a: float, b: float) -> float:
    return a + b

def sub(a: float, b: float) -> float:
    return a - b

def mul(a: float, b: float) -> float:
    return a * b

def div(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b

def square(a: float) -> float:
    return a * a

def sqrt(a: float) -> float:
    if a < 0:
        raise ValueError("Cannot take square root of negative number.")
    return _sqrt(a)

def log(x: float, base: Optional[float] = None) -> float:
    if x <= 0:
        raise ValueError("Log domain error: x must be > 0.")
    if base is None:
        return _log(x)
    if base <= 0 or base == 1:
        raise ValueError("Invalid log base. base must be > 0 and != 1.")
    return _log(x) / _log(base)

def sin(x: float) -> float:
    return _sin(x)

def cos(x: float) -> float:
    return _cos(x)

def percentage(part: float, whole: Optional[float] = None) -> float:
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
    "sqrt",
    "log",
    "sin",
    "cos",
    "percentage",
]
