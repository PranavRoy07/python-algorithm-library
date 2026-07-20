def permutations(nums: list[int]) -> list[list[int]]:
    """Generate all possible permutations of the input list.

    Uses backtracking to build permutations by trying each
    unused element at every position.

    Args:
        nums: A list of unique integers.

    Returns:
        A list of all possible orderings of the input list.
    """
    result: list[list[int]] = []

    def backtrack(current: list[int], remaining: list[int]) -> None:
        """Recursively build permutations.

        Args:
            current: The permutation being built so far.
            remaining: Elements not yet used.
        """
        # Base case: all elements used
        if not remaining:
            result.append(current[:])
            return

        # Try each remaining element in the next position
        for i in range(len(remaining)):
            current.append(remaining[i])

            # Create new remaining list WITHOUT element i
            new_remaining = remaining[:i] + remaining[i + 1:]

            backtrack(current, new_remaining)
            current.pop()    # undo (backtrack!)

    backtrack([], nums)
    return result