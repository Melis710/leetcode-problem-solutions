class Solution:
    # dynamic size sliding window + hashmap solution
    # time complexity: O(n)
    # space complexity: O(1) since only 3 chars stored in hashmap
    def numberOfSubstrings(self, s: str) -> int:
        freq_map = {"a": 0, "b": 0, "c": 0}  # frequency map of a, b, c for current window
        required = 3  # required unique characters for window to contain
        total = 0  # total number of substrings
        left = 0  # left pointer of window
        for char in s:  # right boundary of window
            freq_map[char] += 1
            if freq_map[char] == 1:  # first occurrence
                required -= 1  # consume
            
            while required == 0:  # all 3 required characters consumed
                left_char = s[left]
                freq_map[left_char] -= 1  # shrink window from left
                if freq_map[left_char] == 0:  # last occurrence
                    required += 1  # produce
                left += 1  # advance left pointer 

            total += left  # the constraint fails starting from index left (inclusive)

        return total

class Solution:
    # Leetcode fastest solution
    # time complexity: O(n)
    # space complexity: O(1)
    def numberOfSubstrings(self, s: str) -> int:
        a, b, c = -1, -1, -1
        total = 0  # total number of substrings

        for i, char in enumerate(s):
            if char == "a":
                a = i
            elif char == "b":
                b = i
            else:  # char == "c"
                c = i
            
            total += min(a, b, c) + 1  # minimum index after which constraint is not satisfied + 1
            
        return total

class Solution:
    # Standard, scalable solution with array for fixed size characters given
    # switching from 3 to 26 fixed chars set is just so simple as changing 3 to 26 
    # time complexity: O(n)
    # space complexity: O(1)
    def numberOfSubstrings(self, s: str) -> int:
        last_indices = [-1] * 3  # list of length 3 for last seen indices of a, b, c
        total = 0  # total number of substrings

        for i, char in enumerate(s):
            last_indices[ord(char) - ord("a")] = i  # save index i at relative position of char 
            total += min(last_indices) + 1  # min index after which constraint violated + 1 

        return total