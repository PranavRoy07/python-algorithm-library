from two_pointers.container_water import max_area


def test_basic():
    """Classic example with multiple heights."""
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


def test_two_lines():
    """Only two lines available."""
    assert max_area([1, 1]) == 1


def test_decreasing():
    """Heights decrease left to right."""
    assert max_area([4, 3, 2, 1]) == 4


def test_increasing():
    """Heights increase left to right."""
    assert max_area([1, 2, 3, 4]) == 4


def test_same_height():
    """All lines are the same height."""
    assert max_area([5, 5, 5, 5]) == 15