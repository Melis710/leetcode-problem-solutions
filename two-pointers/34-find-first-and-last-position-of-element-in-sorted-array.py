class Solution:
    ## Binary Search solution for start and end indices
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        i, j = 0, n - 1
        start = -1 
        # there are 2 transitions: from a lower value to target and from target to a higher value
        while i <= j:
            mid = (i + j)//2
            if nums[mid] == target:  # if equal to target, update start index
                start = mid
                j = mid - 1  # shrink search space from right to look for an earlier start index
            elif nums[mid] < target:  # if middle value is less than target, need to search right part
                i = mid + 1
            else:  # search left part since nums[mid] > target
                j = mid - 1  
        # Early Exit: if target is NOT FOUND, no need to search for end index
        if start == -1:
            return [-1, -1]
        # set i to start to leave only one transition point (fewer conditional checks)
        i, j = start, n - 1
        end = -1

        while i <= j:
            mid = (i + j)//2
            if nums[mid] == target:  # if equal to target, update end index
                end = mid
                i = mid + 1  # narrow search space down to right half to look for a higher end index
            else:  # not equal, search left part
                j = mid - 1

        return [start, end]
                   