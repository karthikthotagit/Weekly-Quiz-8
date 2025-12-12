import sys
from pathlib import Path
import math
import pytest

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import (
    add,
    sub,
    mul,
    div,
    square,
    sqrt,
    log,
    sin,
    cos,
    percentage,
)


def test_add_basic():
    assert add(5, 6) == 11
    assert add(-1, 1) == 0
    assert add(0.1, 0.2) == pytest.approx(0.30000000000000004)


def test_sub_basic():
    assert sub(5, 3) == 2
    assert sub(-1, -1) == 0


def test_mul_basic():
    assert mul(3, 4) == 12
    assert mul(0, 100) == 0
    assert mul(-2, 3) == -6


def test_div_basic():
    assert div(10, 2) == 5
    assert div(5, 2) == 2.5
    assert div(-6, 3) == -2


def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(1, 0)


def test_square_and_sqrt():
    assert square(5) == 25
    assert square(-3) == 9

    assert sqrt(9) == 3
    assert sqrt(0) == 0
    with pytest.raises(ValueError):
        sqrt(-1)


def test_log_natural_and_base():
    assert log(math.e) == pytest.approx(1.0)
    assert log(100, 10) == pytest.approx(2.0)
    assert log(0.5, 2) == pytest.approx(-1.0)

    with pytest.raises(ValueError):
        log(0)

    with pytest.raises(ValueError):
        log(-5)

    with pytest.raises(ValueError):
        log(10, 1)

    with pytest.raises(ValueError):
        log(10, -2)


def test_trig():
    assert sin(0) == pytest.approx(0.0)
    assert cos(0) == pytest.approx(1.0)

    assert sin(math.pi / 2) == pytest.approx(1.0)
    assert cos(math.pi) == pytest.approx(-1.0)


def test_percentage_no_whole():
    assert percentage(50) == pytest.approx(0.5)
    assert percentage(100) == pytest.approx(1.0)
    assert percentage(0) == pytest.approx(0.0)


def test_percentage_with_whole():
    assert percentage(1, 4) == pytest.approx(25.0)
    assert percentage(2, 5) == pytest.approx(40.0)
    assert percentage(2, -4) == pytest.approx(-50.0)


def test_percentage_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        percentage(1, 0)


def test_large_numbers():
    assert add(1e18, 1e18) == 2e18
    assert mul(1e9, 1e9) == 1e18


def test_float_imprecision_cases():
    assert add(0.1, 0.2) == pytest.approx(0.30000000000000004)
