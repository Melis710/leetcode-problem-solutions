class Solution:
    # dynamic size sliding window
    # time complexity: O(n)
    # space complexity: O(n) 
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        win_elements = set()  # elements seen as long as they are unique
        win_total = 0  # sum of numbers within the window
        max_total = 0  # maximum total to find
        l = 0  # left boundary of window
        for num in nums:  # right boundary of window
            while num in win_elements:  # shrink window from left until all unique elements
                removed_num = nums[l]
                win_elements.remove(removed_num)
                win_total -= removed_num
                l += 1
            
            win_total += num  # expand window to right
            win_elements.add(num)
            max_total = max(max_total, win_total)  # update max total

        return max_total

class Solution:
    # dynamic sliding window
    # bytearray version further optimized for LeetCode
    # when input constraints are relatively small, utilize arrays to avoid hashing overhead with sets and dictionaries
    # here since we store the existence of a value as True or False, we can use bytearray 
    # to store binary value True or False, which is represented by 1 or 0 in the background

    # time complexity: O(n)
    # space complexity: O(1) 
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        is_seen = bytearray(10001)  # constant space 
        curr_total = 0
        max_total = 0
        l = 0
        for num in nums:
            while is_seen[num]:
                removed_el = nums[l]
                curr_total -= removed_el
                is_seen[removed_el] = False
                l += 1
            
            curr_total += num
            is_seen[num] = True
            # instead of max() function call, use if clause for efficiency
            if curr_total > max_total:
                max_total = curr_total
            
        return max_total
            