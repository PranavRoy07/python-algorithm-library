from binary_search.search_rotated import search_rotated


def test_found():
    """Target found in rotated array."""
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4


def test_found_left_side():
    """Target in the left sorted portion."""
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 5) == 1


def test_not_found():
    """Target not in array."""
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 3) == -1


def test_single_element_found():
    """Single element, target found."""
    assert search_rotated([1], 1) == 0


def test_single_element_not_found():
    """Single element, target not found."""
    assert search_rotated([1], 0) == -1


def test_not_rotated():
    """Array is not rotated."""
    assert search_rotated([1, 2, 3, 4, 5], 3) == 2


def test_two_elements():
    """Two elements, find second."""
    assert search_rotated([3, 1], 1) == 1