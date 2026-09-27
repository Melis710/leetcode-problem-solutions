class Solution:
    # hashmap solution
    # find max of frequency of x + frequency of x+1. order doesn't matter
    # time complexity: O(N)
    # space complexity: O(N)
    def findLHS(self, nums: list[int]) -> int:
        freq_map = dict()  # frequency map of unique characters
        for num in nums:  # create the frequency map
            freq_map[num] = freq_map.get(num, 0) + 1
        # find the maximum of sum freq(x) + freq(x+1)
        max_len = 0
        for key in freq_map.keys():
            # without branch, mathematical trick used instead
            max_len = max(max_len, freq_map[key] + freq_map.get(key + 1, -freq_map[key]))
        
        return max_len