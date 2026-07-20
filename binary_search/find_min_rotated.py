def find_min(nums: list[int]) -> int:
    """Find the minimum element in a rotated sorted array.

    A sorted array has been rotated between 1 and n times.
    Uses binary search by comparing the middle element to
    the rightmost element to determine which half contains
    the minimum.

    Args:
        nums: A rotated sorted list of unique integers.

    Returns:
        The minimum element in the array.
    """
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            # Minimum is in the RIGHT half
            left = mid + 1
        else:
            # Minimum is in the LEFT half (including mid)
            right = mid

    return nums[left]