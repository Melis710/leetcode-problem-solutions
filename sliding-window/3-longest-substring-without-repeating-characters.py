class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_index = {}  # last seen index of a character 
        left = 0  # left pointer of window
        max_len = 0  # maximum length

        for right, char in enumerate(s):  # right pointer of window and current character
            if (duplicate := last_index.get(char, -1)) >= left:  # char was already within the window?
                left = duplicate + 1  # shrink the window to skip the old duplicate
            last_index[char] = right  # update the last seen index for the current character
            max_len = max(max_len, right-left+1)  # update the longest length

        return max_len
