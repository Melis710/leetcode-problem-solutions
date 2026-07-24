def minSubArrayLen(target: int, nums: list[int]) -> int:
    i = 0  # left pointer
    curr_sum = 0  # current window sum
    min_len = float('inf')  # initialize as +inf for minimum logic

    for j in range(len(nums)):  # right pointer
        curr_sum += nums[j]  # expand the window
        while curr_sum >= target:  # shrink the window for minimum size constraint
            min_len = min(min_len, j - i + 1)
            curr_sum -= nums[i]
            i += 1

    return min_len if min_len != float('inf') else 0
