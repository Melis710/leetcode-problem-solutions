## Solution: Fixed Sized Sliding Window

class Solution:
    ## Two pass solution
    # time complexity: O(2N) 
    # space complexity: O(1)
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        ## Initialize first window solution
        # calculate window sum
        win_sum = 0
        for i in range(minutes):
            win_sum += customers[i]
        # add number of naturally satisfied 
        for i in range(minutes, len(customers)):
            if grumpy[i]:
                continue
            win_sum += customers[i]
        # initialize maximum sum as current window sum
        max_sum = win_sum
        # slide the window dropping left element if left is grumpy and adding right element if right is grumpy
        for right in range(minutes, len(customers)):
            # drop left if grumpy 
            if grumpy[right-minutes]:
                win_sum -= customers[right-minutes]
            # add right if grumpy
            if grumpy[right]:
                win_sum += customers[right]

            # update maximum
            max_sum = max(max_sum, win_sum)

        return max_sum

class Solution:
    ## One Pass solution
    # time complexity: O(N)
    # space compexity: O(1)
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # base sum of naturally satisfied customers is always same
        # find maximum extra covered by window
        base = 0
        curr_extra = 0
        max_extra = 0
        # manipulate both base sum and current extra sum in one loop
        for i in range(len(customers)):
            if i >= minutes and grumpy[i-minutes]:
                curr_extra -= customers[i-minutes]

            if grumpy[i]:
                curr_extra += customers[i]
            else:
                base += customers[i]

            max_extra = max(max_extra, curr_extra)
            
        return base + max_extra
        

        
