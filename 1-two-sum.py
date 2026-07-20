def twoSum(nums: list[int], target: int) -> list[int]:
    seen_nums = dict()  # nums[i] : i
    for j, num in enumerate(nums):  # j = 2nd number's index
        comp = target - num  # complement of current number
        if comp in seen_nums:  # complement was seen before?
            i = seen_nums[comp]  # i = 1st number's index
            return [i, j]  # assumed only one solution exists
        seen_nums[num] = j  # add to seen numbers, continue searching  