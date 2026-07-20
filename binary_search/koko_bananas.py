import math


def min_eating_speed(piles: list[int], h: int) -> int:
    """Find the minimum bananas-per-hour speed to finish in h hours.

    Binary searches on the speed value. For each candidate speed,
    calculates total hours needed. Finds the lowest speed that
    finishes within h hours.

    Args:
        piles: A list of banana pile sizes.
        h: Maximum hours available to eat all bananas.

    Returns:
        The minimum integer eating speed.
    """
    left = 1
    right = max(piles)

    while left < right:
        mid = (left + right) // 2

        # Calculate hours needed at this speed
        hours = sum(math.ceil(pile / mid) for pile in piles)

        if hours <= h:
            right = mid       # speed works, try slower
        else:
            left = mid + 1    # too slow, need faster

    return left