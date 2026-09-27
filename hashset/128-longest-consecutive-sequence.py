class Solution:
    # Hashset solution
    # time complexity: O(N)
    # space complexity: O(N)
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set(nums)  # duplicates don't add to length
        max_len = 0
        for num in nums_set:
            # check if the num is a start point
            if num - 1 in nums_set:
                continue
            # here num is the start point, measure the length of consecutive sequence
            curr_len = 0
            next_num = num
            while next_num in nums_set:
                curr_len += 1
                next_num += 1
            # update the maximum length found
            max_len = max(max_len, curr_len)

        return max_len
