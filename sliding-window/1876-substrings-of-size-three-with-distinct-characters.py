class Solution:
    # Scalable Fixed Size Sliding Window Approach with Hashmap
    # time complexity: O(n)
    # space complexity: O(1)
    def countGoodSubstrings(self, s: str) -> int:
        k = 3  # window size
        if len(s) < k:  # early exit 
            return 0 

        letters = dict()  # frequency map for the window
        count = 0  # count of good substrings 
        # Initialize the first window
        for i in range(k):  
            letters[s[i]] = letters.get(s[i], 0) + 1

        if len(letters) == k:  # if there are k distinct keys, increment counter
            count += 1

        # Slide the window
        for i in range(k, len(s)):
            letters[s[i-k]] -= 1  # shrink from left
            if not letters[s[i-k]]:  # if zeroed, delete that key
                del letters[s[i-k]]
            letters[s[i]] = letters.get(s[i], 0) + 1  # expand to right

            if len(letters) == k:  # if there are k distinct keys within the window, increment counter
                count += 1
            
        return count
            