class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = 0  # maximum length to find
        count = 0  # count of 1s within current window 

        for num in nums:
            if num:  # num = 1
                count += 1  # update window count
                max_len = max(max_len, count)  # update maximum length
            else:  # once hit 0 reset the window
                count = 0

        return max_len
            

