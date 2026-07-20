def is_power_of_two(n: int) -> bool:
    """Check if a number is a power of two using recursion.

    A power of two is any number that can be expressed as 2^k
    where k is a non-negative integer (1, 2, 4, 8, 16, ...).

    Recursively divides by 2 until reaching 1 (power of two)
    or an odd number (not a power of two).

    Args:
        n: An integer to check.

    Returns:
        True if n is a power of two, False otherwise.
    """
    # Base cases
    if n <= 0:
        return False
    if n == 1:
        return True

    # If odd (not divisible by 2), it's not a power of 2
    if n % 2 != 0:
        return False

    # Recursive case: divide by 2 and check again
    return is_power_of_two(n // 2)