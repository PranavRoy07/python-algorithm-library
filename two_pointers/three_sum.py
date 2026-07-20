def three_sum(nums: list[int]) -> list[list[int]]:
    """Find all unique triplets that sum to zero.

    Uses sorting and two pointers to avoid duplicates
    and achieve efficient performance.

    Args:
        nums: A list of integers.

    Returns:
        A list of lists, where each inner list contains
        three numbers that add up to zero. No duplicate
        triplets are included.
    """
    nums.sort()
    result: list[list[int]] = []

    for i in range(len(nums) - 2):
        # Skip duplicate values for first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for second number
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicates for third number
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif total < 0:
                left += 1      # need bigger sum → move left →
            else:
                right -= 1     # need smaller sum → move right ←

    return result