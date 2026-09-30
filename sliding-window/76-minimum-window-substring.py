class Solution:
    # Dynamic Size Sliding Window Solution
    # time complexity: O(n+m)
    # space complexity: O(m)
    def minWindow(self, s: str, t: str) -> str:
        # if length of t is greater than length of s, all characters of t cannot be in s
        if len(t) > len(s):
            return ""
        # create frequency map for characters in t
        freq_map_t = {}
        for char in t:
            freq_map_t[char] = freq_map_t.get(char, 0) + 1
        
        left = 0  # left pointer of current window
        min_left = 0  # save the left pointer of minimum window to string indexing
        min_len = float("inf")  # initialize to infinity, it changes at least once
        count = len(t)  # initialize the number of total required characters
        for right, char in enumerate(s):  # expand window by right pointer 
            if char in freq_map_t:
                freq_map_t[char] -= 1
                if freq_map_t[char] >= 0:  # if surplus of same character, don't decrement count
                    count -= 1
            
            while count == 0:  # all characters in t is covered, minimize length  
                if (curr_len := right - left + 1) < min_len:
                    min_len = curr_len
                    min_left = left  # save left pointer for minimum length
                # shrink window from left
                left_char = s[left]
                if left_char in freq_map_t:
                    if freq_map_t[left_char] == 0:  # if no surplus (not negative), increment count again (number of required chars to cover)
                        count += 1
                    freq_map_t[left_char] += 1
                left += 1
            
        return "" if min_len == float("inf") else s[min_left:min_left + min_len]