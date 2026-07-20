def fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number.

    Uses an iterative approach for efficiency. The sequence
    starts with 0, 1, 1, 2, 3, 5, 8, 13, ...

    The recursive formula is: fib(n) = fib(n-1) + fib(n-2)
    with base cases fib(0) = 0 and fib(1) = 1.

    Args:
        n: A non-negative integer position in the sequence.

    Returns:
        The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1

    prev = 0
    curr = 1

    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr

    return curr