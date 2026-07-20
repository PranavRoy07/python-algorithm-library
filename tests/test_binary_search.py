from binary_search.binary_search import binary_search


def test_found_middle():
    """Target is in the middle."""
    assert binary_search([1, 3, 5, 7, 9], 5) == 2


def test_found_start():
    """Target is at the beginning."""
    assert binary_search([1, 3, 5, 7, 9], 1) == 0


def test_found_end():
    """Target is at the end."""
    assert binary_search([1, 3, 5, 7, 9], 9) == 4


def test_not_found():
    """Target does not exist."""
    assert binary_search([1, 3, 5, 7, 9], 6) == -1


def test_single_element_found():
    """List with one element, target found."""
    assert binary_search([5], 5) == 0


def test_single_element_not_found():
    """List with one element, target not found."""
    assert binary_search([5], 3) == -1


def test_empty_list():
    """Empty list returns -1."""
    assert binary_search([], 5) == -1