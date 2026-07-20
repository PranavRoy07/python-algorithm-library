from recursion.fibonacci import fibonacci


def test_zero():
    """Fibonacci of 0 is 0."""
    assert fibonacci(0) == 0


def test_one():
    """Fibonacci of 1 is 1."""
    assert fibonacci(1) == 1


def test_small():
    """Small fibonacci numbers."""
    assert fibonacci(5) == 5


def test_medium():
    """Medium fibonacci number."""
    assert fibonacci(10) == 55


def test_larger():
    """Larger fibonacci number."""
    assert fibonacci(20) == 6765


def test_two():
    """Fibonacci of 2 is 1."""
    assert fibonacci(2) == 1
    