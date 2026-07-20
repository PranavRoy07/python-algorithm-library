from sliding_window.longest_substring import length_of_longest_substring


def test_basic():
    """Normal string with repeating characters."""
    assert length_of_longest_substring("abcabcbb") == 3


def test_all_same():
    """All same characters, longest is 1."""
    assert length_of_longest_substring("bbbbb") == 1


def test_mixed():
    """Mixed repeating characters."""
    assert length_of_longest_substring("pwwkew") == 3


def test_empty():
    """Empty string returns 0."""
    assert length_of_longest_substring("") == 0


def test_all_unique():
    """Every character is unique."""
    assert length_of_longest_substring("abcdef") == 6


def test_single_char():
    """Single character string."""
    assert length_of_longest_substring("a") == 1