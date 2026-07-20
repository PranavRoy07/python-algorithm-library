from recursion.subsets import subsets


def test_three_elements():
    """All subsets of [1,2,3]."""
    result = subsets([1, 2, 3])
    expected = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    assert sorted(result) == sorted(expected)


def test_empty():
    """Subsets of empty list is just empty set."""
    assert subsets([]) == [[]]


def test_single_element():
    """Subsets of [1] is [] and [1]."""
    result = subsets([1])
    expected = [[], [1]]
    assert sorted(result) == sorted(expected)


def test_two_elements():
    """Subsets of [0, 1]."""
    result = subsets([0, 1])
    expected = [[], [0], [1], [0, 1]]
    assert sorted(result) == sorted(expected)


def test_correct_count():
    """Number of subsets should be 2^n."""
    result = subsets([1, 2, 3, 4])
    assert len(result) == 16  # 2^4 = 16