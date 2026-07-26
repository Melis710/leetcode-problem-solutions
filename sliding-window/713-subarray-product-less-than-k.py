def numSubarrayProductLessThanK(nums: list[int], k: int) -> int:
    if k <= 1:  
        return 0  # since 1 <= nums[i]

    i = 0  # left pointer
    product = 1  # start with identity element
    total = 0  # total number of subarrays

    for j in range(len(nums)):  # right pointer
        product *= nums[j]  # expand window
        while product >= k:  # shrink window to satisfy the constraint
            product //= nums[i]
            i += 1
        total += (j - i + 1)  # every new element brings in subarrays of window size

    return total
