import heapq
class MedianFinder:
    ## TWO HEAPS: MAX HEAP FOR THE FIRST HALF AND MIN HEAP FOR THE SECOND HALF OF THE LIST
    # space complexity: O(N)
    def __init__(self):
        self.heap1 = []  # max heap - end of 1st half 
        self.heap2 = []  # min heap - start of 2nd half

    # addNum uses Blind Push technique (first adds to heap1 by default then adjusts)
    # time complexity: O(logN)
    def addNum(self, num: int) -> None:
        # add to heap1 (max heap) first by default
        heapq.heappush(self.heap1, -num)  # -num since max heap

        # rule: 1st half's last element cannot be greater than first element of 2nd half
        if self.heap2 and -self.heap1[0] > self.heap2[0]:
            heapq.heappush(self.heap2, -heapq.heappop(self.heap1))
        
        # balance two heaps: only 1st half may be 1 greater than or equal to 2nd half in size
        if len(self.heap1) - len(self.heap2) > 1:
            heapq.heappush(self.heap2, -heapq.heappop(self.heap1))
        elif len(self.heap2) > len(self.heap1):
            heapq.heappush(self.heap1, -heapq.heappop(self.heap2))        

    # time complexity: O(1)
    def findMedian(self) -> float:
        # two possibilities: heap1 size is 1 more than heap2 or they are equal in size
        if len(self.heap1) > len(self.heap2):
            return -self.heap1[0]
        else:
            return (-self.heap1[0] + self.heap2[0])/2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()