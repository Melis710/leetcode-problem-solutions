import heapq
class Solution:
    # hashmap for frequency map & minimum heap of size k for largest k
    # time complexity: O(N + M*logK) where M is number of unique elements
    # space complexity: O(N)
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq_map = dict()
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        min_heap = []  # of size at most K
        for num, freq in freq_map.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
            
        return [item[1] for item in min_heap]
