from recursion.merge_sort import merge_sort


def test_basic():
    """Sort a normal list."""
    assert merge_sort([38, 27, 43, 3, 9, 82, 10]) == [3, 9, 10, 27, 38, 43, 82]


def test_already_sorted():
    """Already sorted list stays sorted."""
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_reverse_sorted():
    """Reverse sorted list gets sorted."""
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_empty():
    """Empty list returns empty."""
    assert merge_sort([]) == []


def test_single_element():
    """Single element is already sorted."""
    assert merge_sort([42]) == [42]


def test_duplicates():
    """Handles duplicate values correctly."""
    assert merge_sort([3, 1, 3, 2, 1]) == [1, 1, 2, 3, 3]


def test_negative_numbers():
    """Handles negative numbers."""
    assert merge_sort([-3, 5, -1, 0, 2]) == [-3, -1, 0, 2, 5]