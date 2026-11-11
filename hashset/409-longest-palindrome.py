class Solution:
    # time complexity: O(n)
    # space complexity: O(1) since string consists of English letters only
    def longestPalindrome(self, s: str) -> int:
        unpaired = set()
        length = 0
        for c in s:
            # if we encounter a pair 
            if c in unpaired:
                length += 2
                unpaired.remove(c)
            else:
                unpaired.add(c)
        return (length + 1) if unpaired else length  # if at least one unpaired element
