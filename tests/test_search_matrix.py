from binary_search.search_matrix import search_matrix


def test_found():
    """Target exists in the matrix."""
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60],
    ]
    assert search_matrix(matrix, 3) == True


def test_not_found():
    """Target does not exist."""
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60],
    ]
    assert search_matrix(matrix, 13) == False


def test_single_element_found():
    """1x1 matrix, target found."""
    assert search_matrix([[5]], 5) == True


def test_single_element_not_found():
    """1x1 matrix, target not found."""
    assert search_matrix([[5]], 3) == False


def test_first_element():
    """Target is the very first element."""
    matrix = [[1, 2], [3, 4]]
    assert search_matrix(matrix, 1) == True


def test_last_element():
    """Target is the very last element."""
    matrix = [[1, 2], [3, 4]]
    assert search_matrix(matrix, 4) == True