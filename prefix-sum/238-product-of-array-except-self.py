class Solution:
    # time complexity: O(n)
    # space complexity: O(1)
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n
        # create prefix product array in place
        for i in range(n-1):
            res[i+1] = res[i] * nums[i]
        
        suffix = 1  # hold suffix product dynamically
        for i in range(n-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        
        return res
    