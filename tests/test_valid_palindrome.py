from two_pointers.valid_palindrome import is_palindrome


def test_basic_palindrome():
    """Simple palindrome returns True."""
    assert is_palindrome("racecar") == True


def test_sentence_palindrome():
    """Ignores spaces, punctuation, and capitalization."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True


def test_not_palindrome():
    """Non-palindrome returns False."""
    assert is_palindrome("hello") == False


def test_empty_string():
    """Empty string is a palindrome."""
    assert is_palindrome("") == True


def test_single_character():
    """Single character is always a palindrome."""
    assert is_palindrome("a") == True


def test_numbers_and_letters():
    """Handles mix of numbers and letters."""
    assert is_palindrome("0P") == False