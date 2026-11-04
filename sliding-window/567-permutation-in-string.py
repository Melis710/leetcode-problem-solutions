class Solution:
    # Fixed Size Sliding Window
    # Similar to the Leetcode 438 - Find All Anagrams in a String
    # solution with 1 hashmap for target (s1), 1 variable to determine target hashmap satisfied (instead of iterating through the hashmap to see all values == 0)
    # 
    # time complexity: O(N)
    # space complexity: O(N) due to usage of hashmap but based on constraint (all lowercase english letters) O(1) in reality 
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # input validation
        if len(s2) < len(s1):
            return False
        
        # create a frequency map for s2 the target
        s1_map = dict()
        for char in s1:
            s1_map[char] = s1_map.get(char, 0) + 1
        
        # sliding window approach
        k = len(s1)
        required = k
        
        for i, char in enumerate(s2):
            # expand window 
            if char in s1_map:
                if s1_map[char] > 0:
                    required -= 1
                s1_map[char] -= 1
                
            # shrink window 
            if i >= k:
                removed_char = s2[i-k]
                if removed_char in s1_map:
                    if s1_map[removed_char] >= 0:
                        required += 1
                    s1_map[removed_char] += 1
                
            if i >= k-1:
                if required == 0:
                    return True
        
        return False

            
