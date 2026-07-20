def binary_search(nums: list[int], target: int) -> int:
    """Search for a target in a sorted list using binary search.

    Repeatedly halves the search space by comparing the
    target to the middle element.

    Args:
        nums: A sorted list of integers.
        target: The value to search for.

    Returns:
        The index of target if found, otherwise -1.
    """
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1     # target is in RIGHT half
        else:
            right = mid - 1    # target is in LEFT half

    return -1