from arrays_and_hashing.two_sum import two_sum


def test_two_sum_basic():
    """Normal case: two numbers add up to target."""
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]


def test_two_sum_negative_numbers():
    """Edge case: works with negative numbers."""
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]


def test_two_sum_empty_list():
    """Edge case: empty list returns empty."""
    assert two_sum([], 5) == []