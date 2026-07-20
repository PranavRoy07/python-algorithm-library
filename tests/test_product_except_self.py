from arrays_and_hashing.product_except_self import product_except_self


def test_basic():
    """Normal case with positive numbers."""
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]


def test_with_zero():
    """One zero makes all other positions zero except that one."""
    assert product_except_self([0, 1, 2, 3]) == [6, 0, 0, 0]


def test_with_two_zeros():
    """Two zeros makes everything zero."""
    assert product_except_self([0, 0, 2, 3]) == [0, 0, 0, 0]


def test_two_elements():
    """Smallest valid input: two elements."""
    assert product_except_self([3, 5]) == [5, 3]


def test_negative_numbers():
    """Works with negative numbers."""
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]