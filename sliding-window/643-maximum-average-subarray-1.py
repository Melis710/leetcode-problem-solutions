class Solution:
    # fixed size sliding window
    # time complexity: O(n)
    # space complexity: O(1)
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        win_sum = 0
        max_sum = float("-inf")

        for i, num in enumerate(nums):
            # expand window
            win_sum += num

            # shrink window
            if i >= k:
                win_sum -= nums[i-k]

            # update maximum sum
            if i >= k-1:
                if win_sum > max_sum:
                    max_sum = win_sum
                
        return max_sum/k
            