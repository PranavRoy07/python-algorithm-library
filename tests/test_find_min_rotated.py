from binary_search.find_min_rotated import find_min


def test_rotated():
    """Array rotated in the middle."""
    assert find_min([3, 4, 5, 1, 2]) == 1


def test_rotated_more():
    """Array rotated further."""
    assert find_min([4, 5, 6, 7, 0, 1, 2]) == 0


def test_not_rotated():
    """Array not rotated at all."""
    assert find_min([1, 2, 3, 4, 5]) == 1


def test_single_element():
    """Single element is the minimum."""
    assert find_min([1]) == 1


def test_two_elements():
    """Two elements rotated."""
    assert find_min([2, 1]) == 1


def test_rotated_by_one():
    """Rotated by just one position."""
    assert find_min([5, 1, 2, 3, 4]) == 1