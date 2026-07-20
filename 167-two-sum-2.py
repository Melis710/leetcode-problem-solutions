def twoSum(nums: list[int], target: int) -> list[int]:
    i, j = 0, len(nums) - 1  # initialize pointers
    curr_sum = nums[i] + nums[j]  # current sum, given length >= 2

    while i < j and curr_sum != target:
        if curr_sum > target:  # too big, move left
            j -= 1
        if curr_sum < target:  # too small, move right
            i += 1 
        curr_sum = nums[i] + nums[j]  # update current sum

    return [i+1, j+1]  # exactly one solution guaranteed, 1-indexed
