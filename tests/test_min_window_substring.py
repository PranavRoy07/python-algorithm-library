from sliding_window.min_window_substring import min_window


def test_basic():
    """Find smallest window containing all characters."""
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"


def test_exact_match():
    """Target is the entire string."""
    assert min_window("a", "a") == "a"


def test_no_match():
    """Target characters not in string."""
    assert min_window("a", "aa") == ""


def test_empty_string():
    """Empty source string."""
    assert min_window("", "ABC") == ""


def test_duplicate_target():
    """Target has duplicate characters."""
    assert min_window("aaabbc", "abc") == "abbc"


def test_whole_string_needed():
    """Need the entire string."""
    assert min_window("abc", "abc") == "abc"