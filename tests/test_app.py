import sys
from pathlib import Path
import pytest
import math

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import (
    add,
    sub,
    mul,
    div,
    square,
    sqrtFunc,
    logFunc,
    sinFunc,
    cosFunc,
    percentage,
)

def testAdd():
    assert add(5, 6) == 11
    assert add(-1, 1) == 0
    assert add(0.1, 0.2) == pytest.approx(0.30000000000000004)

def testSub():
    assert sub(5, 3) == 2
    assert sub(-1, -1) == 0

def testMul():
    assert mul(3, 4) == 12
    assert mul(0, 100) == 0
    assert mul(-2, 3) == -6

def testDiv():
    assert div(10, 2) == 5
    assert div(5, 2) == 2.5
    assert div(-6, 3) == -2

def testDivByZero():
    with pytest.raises(ZeroDivisionError):
        div(1, 0)

def testSquareAndSqrt():
    assert square(5) == 25
    assert square(-3) == 9
    assert sqrtFunc(9) == 3
    assert sqrtFunc(0) == 0
    with pytest.raises(ValueError):
        sqrtFunc(-1)

def testLog():
    assert logFunc(math.e) == pytest.approx(1.0)
    assert logFunc(100, 10) == pytest.approx(2.0)
    assert logFunc(0.5, 2) == pytest.approx(-1.0)
    with pytest.raises(ValueError):
        logFunc(0)
    with pytest.raises(ValueError):
        logFunc(-5)
    with pytest.raises(ValueError):
        logFunc(10, 1)
    with pytest.raises(ValueError):
        logFunc(10, -2)

def testTrig():
    assert sinFunc(0) == pytest.approx(0.0)
    assert cosFunc(0) == pytest.approx(1.0)
    assert sinFunc(math.pi / 2) == pytest.approx(1.0)
    assert cosFunc(math.pi) == pytest.approx(-1.0)

def testPercentage():
    assert percentage(50) == pytest.approx(0.5)
    assert percentage(100) == pytest.approx(1.0)
    assert percentage(0) == pytest.approx(0.0)
    assert percentage(1, 4) == pytest.approx(25.0)
    assert percentage(2, 5) == pytest.approx(40.0)
    assert percentage(2, -4) == pytest.approx(-50.0)
    with pytest.raises(ZeroDivisionError):
        percentage(1, 0)

def testLargeNumbers():
    assert add(1e18, 1e18) == 2e18
    assert mul(1e9, 1e9) == 1e18

def testFloatImprecision():
    assert add(0.1, 0.2) == pytest.approx(0.30000000000000004)
