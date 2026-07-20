from sliding_window.sliding_window_max import max_sliding_window


def test_basic():
    """Standard sliding window maximum."""
    assert max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]


def test_single_element_window():
    """Window size 1, each element is its own max."""
    assert max_sliding_window([1, 3, 2, 5], 1) == [1, 3, 2, 5]


def test_window_equals_list():
    """Window covers entire list."""
    assert max_sliding_window([1, 3, 2], 3) == [3]


def test_decreasing():
    """Decreasing numbers."""
    assert max_sliding_window([5, 4, 3, 2, 1], 3) == [5, 4, 3]


def test_increasing():
    """Increasing numbers."""
    assert max_sliding_window([1, 2, 3, 4, 5], 3) == [3, 4, 5]


def test_all_same():
    """All same values."""
    assert max_sliding_window([2, 2, 2, 2], 2) == [2, 2, 2]