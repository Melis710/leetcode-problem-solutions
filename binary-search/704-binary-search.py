class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1  # start and end indices for search

        while i <= j:  # eventually search space will be one element i = j, then search is done
            mid = (i + j)//2  # calculate midpoint index
            if nums[mid] == target:  # if midpoint equal to target, immediately return the index
                return mid
            elif nums[mid] > target:  # search left half
                j = mid - 1
            else:  # nums[mid] < target, search right half
                i = mid + 1
        
        return -1  # if here, target NOT FOUND