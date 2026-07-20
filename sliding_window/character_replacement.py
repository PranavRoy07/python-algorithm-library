from collections import Counter


def character_replacement(s: str, k: int) -> int:
    """Find longest substring after replacing at most k characters.

    Uses a sliding window tracking character frequencies.
    The key insight: if (window_size - most_frequent_count) <= k,
    the window is valid.

    Args:
        s: A string of uppercase English letters.
        k: Maximum number of character replacements allowed.

    Returns:
        Length of the longest substring with all same characters
        after at most k replacements.
    """
    count: Counter[str] = Counter()
    left = 0
    max_freq = 0
    best = 0

    for right in range(len(s)):
        count[s[right]] += 1
        max_freq = max(max_freq, count[s[right]])

        # If replacements needed > k, shrink window
        window_size = right - left + 1
        if window_size - max_freq > k:
            count[s[left]] -= 1
            left += 1

        best = max(best, right - left + 1)

    return best