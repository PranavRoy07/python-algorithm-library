from arrays_and_hashing.top_k_frequent import top_k_frequent


def test_basic():
    """Find the 2 most frequent numbers."""
    result = top_k_frequent([1, 1, 1, 2, 2, 3], 2)
    assert sorted(result) == [1, 2]


def test_single_element():
    """Only one element, k=1."""
    assert top_k_frequent([1], 1) == [1]


def test_all_same_frequency():
    """When all numbers appear equally, return any k of them."""
    result = top_k_frequent([1, 2, 3], 2)
    assert len(result) == 2
    assert all(num in [1, 2, 3] for num in result)


def test_k_equals_list_length():
    """When k equals unique elements, return all."""
    result = top_k_frequent([3, 3, 5, 5, 1, 1], 3)
    assert sorted(result) == [1, 3, 5]