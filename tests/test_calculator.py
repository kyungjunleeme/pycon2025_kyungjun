import pytest
from pycon2025_kyungjun.calculator import add
from pycon2025_kyungjun.calculator import subtract
from pycon2025_kyungjun.calculator import multiply
from pycon2025_kyungjun.calculator import divide


def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2


def test_subtract():
    assert subtract(3, 2) == 1
    assert subtract(2, 3) == -1
    assert subtract(0, 0) == 0


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(-2, -3) == 6


def test_divide():
    assert divide(6, 3) == 2
    assert divide(6, -3) == -2
    assert divide(-6, -3) == 2


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)
