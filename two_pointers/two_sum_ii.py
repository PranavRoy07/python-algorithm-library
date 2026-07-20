def two_sum_ii(numbers: list[int], target: int) -> list[int]:
    """Find two numbers in a sorted array that add up to target.

    Uses two pointers since the array is already sorted.
    Returns 1-indexed positions of the two numbers.

    Args:
        numbers: A sorted list of integers.
        target: The target sum to find.

    Returns:
        A list of two 1-indexed positions whose values
        add up to target.
    """
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1       # sum too small → need bigger number
        else:
            right -= 1      # sum too big → need smaller number

    return []