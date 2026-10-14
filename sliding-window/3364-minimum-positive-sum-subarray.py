class Solution:
    # fixed size (k) sliding window solution
    # time complexity: O(n*k) where k = r-l+1
    # space complexity: O(1)
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_sum = float("inf")

        for k in range(l, r+1):  # try each fixed win size k from l to r inclusive
            # initialize the first window sum
            win_sum = sum(nums[:k])
            if 0 < win_sum < min_sum:
                min_sum = win_sum

            # slide the window
            for i in range(k, len(nums)):
                win_sum -= nums[i-k]
                win_sum += nums[i]
                # update the minimum sum
                if 0 < win_sum < min_sum:
                    min_sum = win_sum

        return -1 if min_sum == float("inf") else min_sum