class Solution:
    ## Two Pointers Solution
    def isPalindrome(self, s: str) -> bool:
        # left and right pointers 
        i, j = 0, len(s) - 1
        # compare alphanumeric characters from both ends 
        while i < j:
            while i < j and not s[i].isalnum():  # increment i until s[i] is alphanumeric character as long as i is less than j
                i += 1
            while i < j and not s[j].isalnum():  # decrement j until s[j] is alphanumeric character as long as j is greater than i 
                j -= 1
            # once s[i] and s[j] are alphanumeric or i and j become same 
            if s[i].lower() != s[j].lower():
                return False
            # s[i].lower() == s[j].lower()
            i += 1
            j -= 1

        return True  # if not return yet, then valid palindrome
