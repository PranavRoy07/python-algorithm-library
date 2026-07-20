def is_palindrome(s: str) -> bool:
    """Check if a string is a valid palindrome.

    Considers only alphanumeric characters and ignores case.
    For example, "A man, a plan, a canal: Panama" is a palindrome.

    Args:
        s: The input string to check.

    Returns:
        True if the string is a palindrome, False otherwise.
    """
    left = 0
    right = len(s) - 1

    while left < right:
        # Skip non-alphanumeric characters from left
        while left < right and not s[left].isalnum():
            left += 1

        # Skip non-alphanumeric characters from right
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare characters (ignore case)
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True