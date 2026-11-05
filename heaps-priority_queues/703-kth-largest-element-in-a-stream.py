import heapq

class KthLargest:
    # Min Heap of size K to keep K largest ones
    # time complexity: O(N*logK)
    # space complexity: O(K)
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.min_heap = []  # of size k, holds largest k elements out of nums
        for num in nums:
            heapq.heappush(self.min_heap, num)
            if len(self.min_heap) > self.k:
                heapq.heappop(self.min_heap)
    # add operation 
    # time complexity: O(logk)
    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)