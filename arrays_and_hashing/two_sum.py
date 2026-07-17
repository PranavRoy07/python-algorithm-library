def two_sum(nums: list[int], target: int) -> list[int]:
    """Find two numbers in the list that add up to the target.

    Args:
        nums: A list of integers to search through.
        target: The target sum to find.

    Returns:
        A list containing the indices of the two numbers
        that add up to target, or an empty list if not found.
    """
    seen: dict[int, int] = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []