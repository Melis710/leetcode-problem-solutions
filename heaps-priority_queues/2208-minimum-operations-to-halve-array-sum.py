import heapq
class Solution:
    # Max Heap solution
    # time complexity: O(N*logN)
    # space complexity: O(N)
    def halveArray(self, nums: list[int]) -> int:
        sum_nums = sum(nums)
        half_sum = sum_nums/2

        ops = 0
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        
        while sum_nums > half_sum:
            half_num = heapq.heappop(max_heap)/2
            sum_nums += half_num
            ops += 1
            heapq.heappush(max_heap, half_num)
            
        return ops

class Solution:
    # Same Logic, Cleaner Readibility
    # general rule for floating point operations in Python is to accumulate them instead of continuously subtracting them from a greater number 
    def halveArray(self, nums: list[int]) -> int:
        half_sum = sum(nums)/2.0
        reduced_amount = 0.0

        ops = 0
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        
        while reduced_amount < half_sum:
            largest_half = -heapq.heappop(max_heap)/2.0
            reduced_amount += largest_half
            ops += 1
            heapq.heappush(max_heap, -largest_half)
            
        return ops

