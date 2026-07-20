from sliding_window.character_replacement import character_replacement


def test_basic():
    """Replace 1 character to get longest repeating."""
    assert character_replacement("AABABBA", 1) == 4


def test_all_same():
    """Already all same, no replacement needed."""
    assert character_replacement("AAAA", 2) == 4


def test_replace_all():
    """k large enough to replace entire string."""
    assert character_replacement("ABCD", 3) == 4


def test_no_replacements():
    """k=0 means find longest natural repeat."""
    assert character_replacement("AABBC", 0) == 2


def test_single_char():
    """Single character string."""
    assert character_replacement("A", 0) == 1


def test_two_groups():
    """Two groups with replacement."""
    assert character_replacement("ABAB", 2) == 4