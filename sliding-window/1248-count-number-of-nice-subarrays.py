class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_sum = {0: 1}  # number of indices (value) having that prefix sum (key), initialized with empty subarray sum
        num_odds = 0  # current number of odds
        total = 0  # total number of valid subarrays

        for num in nums:
            if num % 2 == 1:  # if num is an odd number, increment current count of odd numbers
                num_odds += 1

            total += prefix_sum.get(num_odds-k, 0)  # add valid subarrays using number of possible junks 
            prefix_sum[num_odds] = prefix_sum.get(num_odds, 0) + 1  # record number of indices for num_odds
            
        return total
