from python_libtemplate import arithmetic


def test_add():
    assert arithmetic.add(2, 3) == 5
    assert arithmetic.add(-1, 5) == 4


def test_subtract():
    assert arithmetic.subtract(5, 3) == 2
    assert arithmetic.subtract(3, 5) == -2


def test_multiply():
    assert arithmetic.multiply(2, 3) == 6
    assert arithmetic.multiply(-2, 3) == -6


def test_divide():
    assert arithmetic.divide(7, 3) == (2, 1)
    import pytest
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        arithmetic.divide(7, 0)
