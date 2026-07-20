def trap(height: list[int]) -> int:
    """Calculate how much rain water is trapped between bars.

    Uses two pointers tracking the maximum height seen
    from both sides to determine water at each position.

    Args:
        height: A list of non-negative integers representing
                the height of bars.

    Returns:
        The total units of rain water trapped.
    """
    if not height:
        return 0

    left = 0
    right = len(height) - 1
    left_max = height[left]
    right_max = height[right]
    water = 0

    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            water += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water += right_max - height[right]

    return water