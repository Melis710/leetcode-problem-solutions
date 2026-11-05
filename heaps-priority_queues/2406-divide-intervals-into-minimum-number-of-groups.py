import heapq
class Solution:
    # Sorting & Min Heap solution
    # sort based on start time
    # process intervals according to their start time
    # keep min heap based on end time
    # when new interval arrives, compare its start time to the min end time
    # if min end time is less than new interval's start time, no need for a new room (no need for heap push)
    # otherwise, add new room
    # after all intervals processed gives the number of rooms (groups) used

    # time complexity: O(N*logN)
    # space complexity: O(N) because if all intervals intersect we keep N rooms in heap
    def minGroups(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        min_heap = []
        for start, end in intervals:
            if min_heap and start > min_heap[0]:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, end)
        return len(min_heap)
