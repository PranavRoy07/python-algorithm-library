from two_pointers.three_sum import three_sum


def test_basic():
    """Find all triplets that sum to zero."""
    result = three_sum([-1, 0, 1, 2, -1, -4])
    expected = [[-1, -1, 2], [-1, 0, 1]]
    assert sorted(result) == sorted(expected)


def test_no_triplets():
    """No valid triplets exist."""
    assert three_sum([0, 1, 1]) == []


def test_all_zeros():
    """Three zeros is the only triplet."""
    assert three_sum([0, 0, 0]) == [[0, 0, 0]]


def test_empty_list():
    """Empty list returns nothing."""
    assert three_sum([]) == []


def test_too_short():
    """Less than 3 elements returns nothing."""
    assert three_sum([1, 2]) == []