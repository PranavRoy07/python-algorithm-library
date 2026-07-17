from arrays_and_hashing.group_anagrams import group_anagrams


def test_basic_anagrams():
    """Groups words with same letters together."""
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    # Sort inner lists and outer list for comparison
    result = sorted([sorted(group) for group in result])
    expected = sorted([sorted(g) for g in [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]])
    assert result == expected


def test_empty_strings():
    """Handles empty strings correctly."""
    result = group_anagrams([""])
    assert result == [[""]]


def test_no_anagrams():
    """Each word is its own group when no anagrams exist."""
    result = group_anagrams(["abc", "def", "ghi"])
    result = sorted([sorted(group) for group in result])
    expected = sorted([["abc"], ["def"], ["ghi"]])
    assert result == expected


def test_empty_list():
    """Empty input returns empty output."""
    assert group_anagrams([]) == []