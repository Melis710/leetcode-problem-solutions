class Solution:
    # Fixed-Size Sliding Window
    # to simulate type-1 operation, wrap around the first length-1 numbers to the end
    # create 2 same length alternating strings to compare
    # slide the window of size of original length in parallel 
    # 
    # time complexity: O(N)
    # space complexity: O(N) 
    def minFlips(self, s: str) -> int:
        k = len(s)
        s += s[:k-1]
        n = len(s)
        min_ops = float("inf")  # minimum number of 2nd type operations
        ## create strings to compare
        s1, s2 = "", ""
        s1_ops, s2_ops = 0, 0
        for i in range(n):
            if i % 2 == 0:
                s1 += "0"
                s2 += "1"
            else:
                s1 += "1"
                s2 += "0"
        ## sliding window (window initialization and sliding merged)
        for i in range(n):
            # expand window
            if s[i] != s1[i]:
                s1_ops += 1
            if s[i] != s2[i]:
                s2_ops += 1
            
            # shrink window after window initialized
            if i >= k:
                if s[i-k] != s1[i-k]:
                    s1_ops -= 1
                if s[i-k] != s2[i-k]:
                    s2_ops -= 1

            # update minimum once window initialized
            if i >= k-1:
                min_ops = min(min_ops, s1_ops, s2_ops)

        return min_ops

class Solution:
    ## CLEANER VERSION
    def minFlips(self, s: str) -> int:
        k = len(s)
        s += s  
        
        diff = 0
        min_ops = float("inf")
        
        for i in range(len(s)):
            # "010101..." expected character:
            target = "0" if i % 2 == 0 else "1"

            # expand window
            if s[i] != target:
                diff += 1
            # shrink window
            if i >= k:
                out_target = "0" if (i - k) % 2 == 0 else "1"
                if s[i - k] != out_target:
                    diff -= 1
                    
            # update min
            if i >= k - 1:
                # diff -> required operations for "0101..."
                # k - diff -> required operations for "1010..."
                min_ops = min(min_ops, diff, k - diff)
                
        return min_ops