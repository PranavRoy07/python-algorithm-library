from recursion.permutations import permutations


def test_three_elements():
    """All permutations of [1,2,3]."""
    result = permutations([1, 2, 3])
    expected = [
        [1, 2, 3], [1, 3, 2],
        [2, 1, 3], [2, 3, 1],
        [3, 1, 2], [3, 2, 1],
    ]
    assert sorted(result) == sorted(expected)


def test_single_element():
    """One element has one permutation."""
    assert permutations([1]) == [[1]]


def test_two_elements():
    """Two elements have two permutations."""
    result = permutations([0, 1])
    expected = [[0, 1], [1, 0]]
    assert sorted(result) == sorted(expected)


def test_correct_count():
    """Number of permutations should be n!."""
    result = permutations([1, 2, 3, 4])
    assert len(result) == 24  # 4! = 24


def test_empty():
    """Empty list has one permutation (the empty list)."""
    assert permutations([]) == [[]]