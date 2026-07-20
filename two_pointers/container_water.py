def max_area(height: list[int]) -> int:
    """Find two lines that together hold the most water.

    Uses two pointers starting at both ends and moving
    the shorter line inward to find the maximum area.

    Args:
        height: A list of non-negative integers representing
                the height of vertical lines.

    Returns:
        The maximum amount of water that can be contained.
    """
    left = 0
    right = len(height) - 1
    best = 0

    while left < right:
        width = right - left
        water = min(height[left], height[right]) * width
        best = max(best, water)

        # Move the SHORTER line inward (it limits the water)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return best