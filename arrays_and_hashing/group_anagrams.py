from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    """Group strings that are anagrams of each other.

    Anagrams are words that contain the same letters in any order.
    For example: "eat", "tea", "ate" are all anagrams.

    Args:
        strs: A list of strings to group.

    Returns:
        A list of lists, where each inner list contains
        strings that are anagrams of each other.
    """
    groups: defaultdict[str, list[str]] = defaultdict(list)

    for word in strs:
        key = "".join(sorted(word))
        groups[key].append(word)

    return list(groups.values())