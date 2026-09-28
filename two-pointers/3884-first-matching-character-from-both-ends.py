class Solution:
    # time complexity: O(N)
    # space complexity: O(1)
    def firstMatchingIndex(self, s: str) -> int:
        n = len(s)
        i = 0  # left, right = 0, len(s) - 1
        while i <= (j := n - i - 1):  # left <= right
            if s[i] == s[j]:
                return i
            i += 1  # left += 1
            # right -= 1
        return -1
    