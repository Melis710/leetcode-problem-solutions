class Solution:
    # Two Pointers solution
    # sort starts and ends separately
    # process each start to see if it is before or after the minimum end
    # 
    # time complexity: O(N*logN)
    # space complexity: O(N)
    def minGroups(self, intervals: list[list[int]]) -> int:
        starts = sorted(i[0] for i in intervals)
        ends = sorted(i[1] for i in intervals)

        end_ptr = 0
        groups = 0

        for start in starts:
            if start > ends[end_ptr]:
                end_ptr += 1
            else:
                groups += 1

        return groups
