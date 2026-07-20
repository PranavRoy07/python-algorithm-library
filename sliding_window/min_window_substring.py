from collections import Counter


def min_window(s: str, t: str) -> str:
    """Find the minimum window in s that contains all characters of t.

    Uses a sliding window that expands right to include characters
    and shrinks left to find the smallest valid window.

    Args:
        s: The source string to search in.
        t: The target string whose characters must all be present.

    Returns:
        The smallest substring of s containing all characters
        of t, or empty string if no such window exists.
    """
    if not s or not t:
        return ""

    need = Counter(t)
    missing = len(t)
    left = 0
    best_start = 0
    best_length = float("inf")

    for right in range(len(s)):
        # If this character is needed, reduce missing count
        if need[s[right]] > 0:
            missing -= 1
        need[s[right]] -= 1

        # When all characters are found, try to shrink
        while missing == 0:
            window_size = right - left + 1
            if window_size < best_length:
                best_length = window_size
                best_start = left

            # Remove left character and shrink
            need[s[left]] += 1
            if need[s[left]] > 0:
                missing += 1
            left += 1

    if best_length == float("inf"):
        return ""
    return s[best_start:best_start + int(best_length)]