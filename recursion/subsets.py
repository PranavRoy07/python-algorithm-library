def subsets(nums: list[int]) -> list[list[int]]:
    """Generate all possible subsets of the input list.

    Uses backtracking to explore two choices for each element:
    include it or skip it. Builds subsets recursively.

    Args:
        nums: A list of unique integers.

    Returns:
        A list of all possible subsets, including the
        empty set and the full set.
    """
    result: list[list[int]] = []

    def backtrack(start: int, current: list[int]) -> None:
        """Recursively build subsets starting from index start.

        Args:
            start: The index to start considering elements from.
            current: The subset being built so far.
        """
        # Add a copy of current subset to results
        result.append(current[:])

        # Try adding each remaining element
        for i in range(start, len(nums)):
            current.append(nums[i])       # include this element
            backtrack(i + 1, current)      # recurse with next elements
            current.pop()                  # undo (backtrack!)

    backtrack(0, [])
    return result