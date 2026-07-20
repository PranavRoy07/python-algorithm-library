from sliding_window.best_time_stock import max_profit


def test_basic():
    """Buy low, sell high for max profit."""
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5


def test_no_profit():
    """Prices only go down, no profit possible."""
    assert max_profit([7, 6, 4, 3, 1]) == 0


def test_single_day():
    """Can't buy and sell on same day."""
    assert max_profit([5]) == 0


def test_two_days_profit():
    """Simple two-day profit."""
    assert max_profit([1, 5]) == 4


def test_two_days_loss():
    """Price drops, no profit."""
    assert max_profit([5, 1]) == 0


def test_empty():
    """Empty list returns zero."""
    assert max_profit([]) == 0