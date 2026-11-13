import heapq
class Solution:
    # Min Heap solution
    # Idea: heapify rating-index pairs based on minimum rating
    # each iteration, assign number of candies given to that index based on its neighbors
    # smaller ratings will be processed first

    # time complexity: O(N*logN)
    # space complexity: O(N)
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings) 
        if n == 1:  # no neighbors, give smallest possible
            return 1

        hashmap = dict()  # keys: indices, values: ratings
        heap = [(rating, i) for i, rating in enumerate(ratings)]  # heap to keep ratings ordered
        heapq.heapify(heap)
        candies = 0  # total number of candies distributed
        while heap:
            rating, idx = heapq.heappop(heap)  # minimum rating of ones not processed yet
            # at index 0 and n-1, there is one neighbor 
            if idx == 0:
                if ratings[1] >= rating:  # if less than or equal to its neighbor
                    hashmap[idx] = 1  # give smallest possible candies
                else:  # greater than its neighbor, neighbor smaller, was processed before
                    hashmap[idx] = hashmap[1] + 1  # give 1 more candies
            elif idx == n - 1:
                if ratings[n-2] >= rating:
                    hashmap[idx] = 1
                else:
                    hashmap[idx] = hashmap[n-2] + 1
            else:  # middle indices, non-boundaries 
                if rating <= ratings[idx-1] and rating <= ratings[idx+1]:  # if less than both neighbors, give smallest possible candies
                    hashmap[idx] = 1
                elif rating > ratings[idx-1]:  # greater than left neighbor
                    hashmap[idx] = hashmap[idx-1] + 1  # give one more candies
                if rating > ratings[idx+1]:  # greater than right neighbor?
                    # give maximum of left neighbor, if assigned, and right neighbor
                    hashmap[idx] = max(hashmap.get(idx, 1), hashmap[idx+1]+1)
            
            candies += hashmap[idx]  # increment by current number of candies given
        
        return candies
 
import heapq
class Solution:
    # ***** OPTIMAL SOLUTION *****
    # Two-Pass Greedy

    # time complexity: O(N)
    # space complexity: O(N)
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        candies = [1]*n
        # from left to right, check relation with left neighbors
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        # from right to left, check relation with right neighbors
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                if candies[i] <= candies[i+1]:  # if not already > 
                    candies[i] = candies[i+1] + 1
            
        return sum(candies)
