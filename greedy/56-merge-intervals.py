import heapq
class Solution:
    # Min Heap solution (Not Optimal -> heap overhead)
    # time complexity: O(NlogN)
    # space complexity: O(1)
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        heapq.heapify(intervals)
        res = []
        while len(intervals) >= 2:
            start1, end1 = heapq.heappop(intervals)
            start2, end2 = heapq.heappop(intervals)
            if end1 < start2:
                res.append([start1, end1])
                heapq.heappush(intervals, [start2, end2])
            elif start2 < end1 and end2 < end1:
                heapq.heappush(intervals, [start1, end1])
            else:
                heapq.heappush(intervals, [start1, end2])

        if intervals:
            res.append(heapq.heappop(intervals))
        return res


class Solution:
    # Optimal Sorting & Greedy Solution
    
    # time compelxity: O(NlogN)
    # space complexity: O(1)
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            curr_x, curr_y = intervals[i]
            last_x, last_y = res[-1]

            if last_y >= curr_x:
                res[-1] = [last_x, max(last_y, curr_y)]
            else:  # last_y < curr_x
                res.append(intervals[i])

        return res