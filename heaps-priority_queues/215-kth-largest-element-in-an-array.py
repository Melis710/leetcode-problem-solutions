import heapq
class Solution:
    # time complexity: O(N*logK)
    # space complexity: O(K)
    def findKthLargest(self, nums: list[int], k: int) -> int:
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)  # remove minimum
        # after all n elements processed, the remaining elements are the k largest elements 
        # and the root is the kth largest one because it's the minimum (kth one) of the remaining 
        return min_heap[0]
