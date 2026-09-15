class Solution:
    # Dynamic Size Sliding Window 
    # time complexity: O(n)
    # space complexity: O(1)
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:  # at least 3 numbers needed
            return 0

        left = 0
        count = 0
        for right in range(2, len(nums)): 
            if nums[right] - nums[right-1] == nums[right-1] - nums[right-2]:
                count += (right - left - 1)  # length - 3 + 1, where length = right - left + 1
            else:
                left = right - 1

        return count