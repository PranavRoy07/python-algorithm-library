from recursion.power_of_two import is_power_of_two


def test_one():
    """1 is 2^0, a power of two."""
    assert is_power_of_two(1) == True


def test_two():
    """2 is 2^1."""
    assert is_power_of_two(2) == True


def test_sixteen():
    """16 is 2^4."""
    assert is_power_of_two(16) == True


def test_not_power():
    """6 is not a power of two."""
    assert is_power_of_two(6) == False


def test_zero():
    """0 is not a power of two."""
    assert is_power_of_two(0) == False


def test_negative():
    """Negative numbers are not powers of two."""
    assert is_power_of_two(-4) == False


def test_large_power():
    """Large power of two."""
    assert is_power_of_two(1024) == True


def test_three():
    """3 is not a power of two."""
    assert is_power_of_two(3) == False