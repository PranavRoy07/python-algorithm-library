def product_except_self(nums: list[int]) -> list[int]:
    """Calculate product of all elements except the current one.

    For each position i, returns the product of all numbers
    in the list except nums[i], without using division.

    Args:
        nums: A list of integers.

    Returns:
        A list where each element is the product of all
        other elements in the input list.
    """
    n = len(nums)
    result = [1] * n

    # Left pass: multiply everything to the LEFT of each position
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]

    # Right pass: multiply everything to the RIGHT of each position
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]

    return result