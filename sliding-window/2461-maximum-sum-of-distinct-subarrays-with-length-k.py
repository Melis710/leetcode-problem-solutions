class Solution:
    # Fixed Size Sliding Window
    # dictionary to check uniqueness (number of keys) and to hold how many times the same value appears within the window 
    #
    # time complexity: O(N)
    # space complexity: O(K) K being the maximum size of subarray with all distinct elements 
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        max_sum = 0
        win_sum = 0
        win_set = dict()

        for i, num in enumerate(nums):
            # expand window
            win_set[num] = win_set.get(num, 0) + 1
            win_sum += num

            # shrink window
            if i >= k:
                old_num = nums[i-k]
                win_set[old_num] -= 1
                if win_set[old_num] == 0:
                    del win_set[old_num]
                win_sum -= old_num

            # update maximum sum
            if i >= k-1:
                if len(win_set) == k:
                    max_sum = max(max_sum, win_sum)

        return max_sum