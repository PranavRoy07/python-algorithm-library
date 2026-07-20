def search_matrix(matrix: list[list[int]], target: int) -> bool:
    """Search for a target value in a sorted 2D matrix.

    The matrix has these properties:
    - Each row is sorted left to right.
    - First integer of each row is greater than the last
      integer of the previous row.

    Treats the 2D matrix as a flat sorted list and
    performs binary search using index conversion.

    Args:
        matrix: A 2D list of sorted integers.
        target: The value to search for.

    Returns:
        True if target is found, False otherwise.
    """
    if not matrix or not matrix[0]:
        return False

    rows = len(matrix)
    cols = len(matrix[0])
    left = 0
    right = rows * cols - 1

    while left <= right:
        mid = (left + right) // 2

        # Convert flat index to row and column
        row = mid // cols
        col = mid % cols
        value = matrix[row][col]

        if value == target:
            return True
        elif value < target:
            left = mid + 1
        else:
            right = mid - 1

    return False