from collections import deque
class Solution:
    # Dynamic Sliding Window & Monotonically Increasing - Decreasing Queue (Deque) Solution
    # min_deque to hold next minimums in monotonically increasing order
    # max_deque to hold next maximums in monotonically decreasing order
    # 3 Steps for Dynamic Sliding Window solution:
    #   1. expand window (outer loop tracks right pointer) by updating min_deque and max_deque
    #   2. shrink window until it satisfies the constraint being <= limit
    #   3. update the maximum length (expanding window via outer loop while <= limit)

    # time complexity: O(N)
    # space complexity: O(N)
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        max_len = 0
        min_deque = deque()  # monotonically increasing
        max_deque = deque()  # monotonically decreasing
        left = 0

        for right, num in enumerate(nums):
            ## EXPAND WINDOW 
            # update min deque
            while min_deque and num < min_deque[-1]:
                min_deque.pop()
            min_deque.append(num)
            # update max deque
            while max_deque and max_deque[-1] < num:
                max_deque.pop()
            max_deque.append(num)
            
            ## SHRINK WINDOW
            while min_deque and max_deque and max_deque[0] - min_deque[0] > limit:
                if nums[left] == min_deque[0]:
                    min_deque.popleft()
                if nums[left] == max_deque[0]:
                    max_deque.popleft()
                left += 1
            
            ## UPDATE MAXIMUM LENGTH
            if (right - left + 1) > max_len:
                max_len = right - left + 1
            
        return max_len
