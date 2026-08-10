class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_val = nums[0]  # initialize minimum value as the first element to compare 
        i, j = 0, len(nums) - 1  # both ends of array

        while i <= j:
            mid = (i + j)//2  # middle element index
            if nums[mid] < min_val:
                min_val = nums[mid]  # potential minimum
                j = mid - 1  # lower value might be found in left half
            else: 
                i = mid + 1

        return min_val