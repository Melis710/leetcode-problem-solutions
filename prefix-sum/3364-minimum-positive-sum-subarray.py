class Solution:
    # time complexity: O(n*k) where k = r-l+1
    # space complexity: O(n)
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_sum = float("inf")  # to find min, initialize as +inf
        n = len(nums)
        prefix_sum = [0] * (n+1)  # accumulate prefix sum 
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]
    
        for i in range(l, r+1):  # window length from l to r
            for j in range(i, n+1):  # start from at least l elements ahead 
                # if subarray sum is positive and a new minimum
                if 0 < (sub_sum := prefix_sum[j] - prefix_sum[j-i]) < min_sum:
                    min_sum = sub_sum  # update minimum sum
                    
        return -1 if min_sum == float("inf") else min_sum