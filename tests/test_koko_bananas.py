from binary_search.koko_bananas import min_eating_speed


def test_basic():
    """Find minimum eating speed."""
    assert min_eating_speed([3, 6, 7, 11], 8) == 4


def test_more_time():
    """More hours available, slower speed ok."""
    assert min_eating_speed([30, 11, 23, 4, 20], 5) == 30


def test_extra_time():
    """Much more time, can eat slowly."""
    assert min_eating_speed([30, 11, 23, 4, 20], 6) == 23


def test_single_pile():
    """One pile, one hour."""
    assert min_eating_speed([10], 1) == 10


def test_one_banana_piles():
    """All piles have 1 banana."""
    assert min_eating_speed([1, 1, 1], 3) == 1