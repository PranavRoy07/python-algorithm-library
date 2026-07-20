def merge_sort(nums: list[int]) -> list[int]:
    """Sort a list using the merge sort algorithm.

    Recursively splits the list in half, sorts each half,
    then merges them back together in sorted order.

    Args:
        nums: A list of integers to sort.

    Returns:
        A new sorted list.
    """
    # Base case: lists of 0 or 1 elements are already sorted
    if len(nums) <= 1:
        return nums

    # Split the list in half
    mid = len(nums) // 2
    left_half = merge_sort(nums[:mid])
    right_half = merge_sort(nums[mid:])

    # Merge the two sorted halves
    return merge(left_half, right_half)


def merge(left: list[int], right: list[int]) -> list[int]:
    """Merge two sorted lists into one sorted list.

    Compares elements from both lists one by one,
    always picking the smaller element.

    Args:
        left: A sorted list of integers.
        right: A sorted list of integers.

    Returns:
        A single sorted list containing all elements.
    """
    result: list[int] = []
    i = 0
    j = 0

    # Compare elements from both lists
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements (one list might have leftovers)
    result.extend(left[i:])
    result.extend(right[j:])

    return result