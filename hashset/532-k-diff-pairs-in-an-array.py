class Solution:
    # Hashset solution
    # 2 hashsets for both unique numbers being complements and unique pairs as tuples
    # time complexity: O(N)
    # space complexity: O(N)
    def findPairs(self, nums: List[int], k: int) -> int:
        nums_set = set()  # complements, O(1) lookup
        pairs_set = set()  # unique pairs

        for num in nums:
            comp = num - k  # calculate smaller complement 
            # if complement was seen before, form the pair
            if comp in nums_set:
                pair = (comp, num)  # tuple normalization (sorted)
                if pair not in pairs_set:  # ensure only unique pairs added
                    pairs_set.add(pair)
                
            comp = num + k  # calculate greater complement
            # if complement was seen before, form the pair
            if comp in nums_set:
                pair = (num, comp)  # tuple normalization (sorted)
                if pair not in pairs_set:  # ensure only unique pairs added
                    pairs_set.add(pair)
            
            nums_set.add(num)  # add current num as a complement candidate for another number
                
        return len(pairs_set)  # return total number of unique pairs 