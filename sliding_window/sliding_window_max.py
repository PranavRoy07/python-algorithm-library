from collections import deque


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    """Find the maximum value in each sliding window of size k.

    Uses a deque (double-ended queue) to efficiently track
    the maximum. The deque stores indices of useful elements
    in decreasing order of their values.

    Args:
        nums: A list of integers.
        k: The size of the sliding window.

    Returns:
        A list of maximum values for each window position.
    """
    dq: deque[int] = deque()  # stores INDICES, not values
    result: list[int] = []

    for i in range(len(nums)):
        # Remove indices that are outside the window
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove indices of elements SMALLER than current
        # (they can never be the max while current exists)
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        # Start recording results once first window is complete
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result