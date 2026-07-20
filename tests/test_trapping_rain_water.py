from two_pointers.trapping_rain_water import trap


def test_basic():
    """Classic example with valleys that trap water."""
    assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6


def test_no_water():
    """Ascending heights trap nothing."""
    assert trap([1, 2, 3, 4, 5]) == 0


def test_simple_valley():
    """Simple valley traps water."""
    assert trap([3, 0, 3]) == 3


def test_empty():
    """Empty list traps nothing."""
    assert trap([]) == 0


def test_flat():
    """Flat surface traps nothing."""
    assert trap([2, 2, 2, 2]) == 0


def test_v_shape():
    """V shape traps water at the bottom."""
    assert trap([4, 2, 0, 3, 2, 5]) == 9