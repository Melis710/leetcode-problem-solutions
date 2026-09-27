class Solution:
    # Hashmap solution, used as frequency map of numbers
    # time complexity: O(N)
    # space complexity: O(N)
    def findPairs(self, nums: List[int], k: int) -> int:
        freq_map = dict()  # frequency map of distinct numbers
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        count = 0  # number of pairs
        for num in freq_map:
            # if k is positive, check presence of complement of num, num + k
            if k > 0 and freq_map.get(num + k, 0):
                count += 1
            # if k is 0, num and its complement are equal so we need at least 2 of them to form a pair like (1, 1)
            elif k == 0 and freq_map[num] >= 2:
                count += 1

        return count