def length_of_longest_substring(s: str) -> int:
    """Find the length of the longest substring without repeating characters.

    Uses a sliding window with a set to track characters
    currently in the window.

    Args:
        s: The input string.

    Returns:
        The length of the longest substring with all
        unique characters.
    """
    char_set: set[str] = set()
    left = 0
    best = 0

    for right in range(len(s)):
        # If character already in window, shrink from left
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        # Add current character to window
        char_set.add(s[right])

        # Update best length
        best = max(best, right - left + 1)

    return best
