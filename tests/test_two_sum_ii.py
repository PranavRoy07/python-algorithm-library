from two_pointers.two_sum_ii import two_sum_ii


def test_basic():
    """Normal case: find two numbers that add to target."""
    assert two_sum_ii([2, 7, 11, 15], 9) == [1, 2]


def test_negative_numbers():
    """Works with negative numbers."""
    assert two_sum_ii([-1, 0], -1) == [1, 2]


def test_target_at_ends():
    """Answer is the first and last elements."""
    assert two_sum_ii([1, 2, 3, 4, 5], 6) == [1, 5]


def test_two_elements():
    """Smallest valid input."""
    assert two_sum_ii([1, 3], 4) == [1, 2]