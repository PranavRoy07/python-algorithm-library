from collections import Counter


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """Find the k most frequently occurring elements.

    Args:
        nums: A list of integers.
        k: Number of top frequent elements to return.

    Returns:
        A list of the k most frequent elements.
    """
    count = Counter(nums)
    return [num for num, freq in count.most_common(k)]