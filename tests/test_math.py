import pytest

#A Failing Test Case
def test_one_plus_one():
    assert 1 + 1 == 2


# A Failing Test Case
def test_one_plus_two():
    a = 1
    b = 2
    c = 0
    # c = 3
    assert a + b == c


# A Test Case with an Exception
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0

    assert "division by zero" in str(e.value)


# Parameterized Test Cases
# DRY: Don't Repeat Yourself!
"""
def test_multiply_two_positive_ints():
    assert 2 * 3 == 6


def test_multiply_identity():
    assert 1 * 99 == 99

def test_multiply_zero():
    assert 0 * 100 == 0
"""

products = [
    (2, 3, 6),            # positive integers
    (1, 99, 99),          # identity
    (0, 99, 0),           # zero
    (3, -4, -12),         # positive by negative
    (-5, -5, 25),         # negative by negative
    (2.5, 6.7, 16.75),    # floats
]


@pytest.mark.parametrize("a, b, product", products)
def test_multiplication(a, b, product):
    assert a * b == product

