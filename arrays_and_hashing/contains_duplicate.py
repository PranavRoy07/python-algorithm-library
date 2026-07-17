def contains_duplicate(nums: list[int]) -> bool:
    """Check if any value appears more than once in the list.

    Args:
        nums: A list of integers to check.

    Returns:
        True if any value appears at least twice, False otherwise.
    """
    return len(nums) != len(set(nums))