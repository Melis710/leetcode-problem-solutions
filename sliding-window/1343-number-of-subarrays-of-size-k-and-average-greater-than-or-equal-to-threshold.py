class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        # instead of calculating division by k every step
        target_sum = k*threshold  # calculate sum over a window and compare that to this
        # initialize first window
        curr_sum = sum(arr[:k])
        count = 1 if curr_sum >= target_sum else 0
        # slide the window
        for i in range(k, len(arr)):
            # remove old number
            curr_sum -= arr[i-k]
            # add new number
            curr_sum += arr[i]
            # update count 
            if curr_sum >= target_sum:
                count += 1
        
        return count
