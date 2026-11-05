import heapq
class Solution:
    # Min Heap Solution
    # time complexity: O(N + K*logN) = O(N) for heapify + O(K*logN)
    # space complexity: O(N)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(pow(p[0], 2) + pow(p[1], 2), p) for p in points]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]

class Solution:
    # time complexity: O(N*logK)
    # space complexity: O(K)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return heapq.nsmallest(k, points, key=lambda p: p[0]**2 + p[1]**2)


class Solution:
    # Manual Version of Right Above
    # time complexity: O(N*logK)
    # space complexity: O(K)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []  # create a max heap
        for x, y in points:
            heapq.heappush(max_heap, (-(x**2 + y**2), [x, y]))  # add negative of distance
            if len(max_heap) > k:  # hold no more than k points
                heapq.heappop(max_heap)  # largest one gets popped off
        return [p[1] for p in max_heap]  # k closest points left
    