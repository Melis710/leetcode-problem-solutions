class Solution:
    # Dynamic Size Sliding Window
    # time complexity: O(N)
    # space complexity: O(1)
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        freq_map = {"T": 0, "F": 0}
        left = 0  # left pointer of window (to shrink)
        max_len = 0  # maximum length to be found and return

        for right in range(len(answerKey)):  # right pointer of window (to expand)
            freq_map[answerKey[right]] += 1  # expand window to the right
            # adjust window based on constraint (shrink from left)
            while freq_map["T"] > k and freq_map["F"] > k:
                freq_map[answerKey[left]] -= 1
                left += 1
            # update maximum window length
            max_len = max(max_len, right-left+1)
        
        return max_len
            
        