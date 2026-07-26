def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()  # sort to handle duplicates
    n = len(nums)
    res = []  # triplets

    for i in range(n):
        if nums[i] > 0:  # early exit since array is sorted, impossible to have nums[j] + nums[k] < 0
            break

        if i > 0 and nums[i] == nums[i-1]:  # skip same targets
            continue

        ## TwoSum Problem
        target_sum = -nums[i]
        j, k = i + 1, n - 1
        while j < k:
            curr_sum = nums[j] + nums[k]
            if curr_sum == target_sum:
                res.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                while j < k and nums[j] == nums[j-1]:  # skip duplicate second numbers
                    j += 1
                # while skipping j's only is enough, skipping k's too is for optimization here
                while j < k and nums[k] == nums[k+1]:
                    k -= 1
            elif curr_sum > target_sum:
                k -= 1
            else:  # curr_sum < target_sum
                j += 1
        
    return res
