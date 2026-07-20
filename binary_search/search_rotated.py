def search_rotated(nums: list[int], target: int) -> int:
    """Search for a target in a rotated sorted array.

    At each step, determines which half is sorted and
    checks if the target falls within that sorted range.

    Args:
        nums: A rotated sorted list of unique integers.
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

        # LEFT half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1    # target is in sorted left half
            else:
                left = mid + 1     # target is in right half
        # RIGHT half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1     # target is in sorted right half
            else:
                right = mid - 1    # target is in left half

    return -1