def twoSum(nums: list[int], target_sum: int) -> list[int]:
    i, j = 0, len(nums) - 1  # initialize pointers
    curr_sum = nums[i] + nums[j]  # current sum, given length >= 2

    while i < j and curr_sum != target_sum:
        if curr_sum > target_sum:  # too big, move left
            j -= 1
        if curr_sum < target_sum:  # too small, move right
            i += 1 
        curr_sum = nums[i] + nums[j]  # update current sum

    return [i+1, j+1]  # exactly one solution guaranteed, 1-indexed
