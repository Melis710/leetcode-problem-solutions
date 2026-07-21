def threeSum2(nums: list[int]) -> list[list[int]]:
    nums.sort()  # sort to handle duplicates and two sum problem
    res = []  # list of triples to be returned
    n = len(nums)
    i = 0
    while i < n:
        # fix the first number to reduce the problem to Two Sum
        num1 = nums[i]  
        target = -num1  # target sum
        j, k = i + 1, n - 1
        ## Two Sum Problem: find all pairs with target sum
        while j < k:
            curr_sum = nums[j] + nums[k]
            if curr_sum == target:
                num2, num3 = nums[j], nums[k]
                res.append([num1, num2, num3])
                # move one step
                j += 1
                k -= 1
                # skip same num2s to avoid duplicates
                while j < k and nums[j] == nums[j-1]: 
                    j += 1
                # skip same num3s to avoid duplicates
                while j < k and nums[k] == nums[k+1]:
                    k -= 1
            elif curr_sum < target:  # move right
                j += 1
            else:
                k -= 1  # move left
        i += 1
        # skip same target sums (num1s)
        while i < n and nums[i] == nums[i-1]:  
            i += 1

    return res
