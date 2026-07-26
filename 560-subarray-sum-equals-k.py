def subarraySum(nums: list[int], k: int) -> int:
    total = 0  # total number of subarrays
    curr_sum = 0  # current cumulative sum 
    sum_freq = {0: 1}  # initialize prefix sums
    
    for i in range(len(nums)):
        curr_sum += nums[i]  # update cumulative sum
        comp = curr_sum - k  # complement
        if comp in sum_freq:
            total += sum_freq[comp]  # add number of subarrays
        sum_freq[curr_sum] = sum_freq.get(curr_sum, 0) + 1  # add new prefix sum

    return total
