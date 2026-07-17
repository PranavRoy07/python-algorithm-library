from arrays_and_hashing.contains_duplicate import contains_duplicate


def test_has_duplicates():
    """List with duplicates returns True."""
    assert contains_duplicate([1, 2, 3, 1]) == True


def test_no_duplicates():
    """List without duplicates returns False."""
    assert contains_duplicate([1, 2, 3, 4]) == False


def test_empty_list():
    """Empty list returns False."""
    assert contains_duplicate([]) == False