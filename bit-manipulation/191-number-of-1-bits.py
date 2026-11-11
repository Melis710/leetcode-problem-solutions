class Solution:
    ## String Conversion

    # time complexity: O(B) B: number of bits (32-bit int)  
    #space complexity: O(B) (32-bit int)
    def hammingWeight(self, n: int) -> int:
        b_str = bin(n)[2:]  # binary string representation
        count = 0
        for b in b_str:
            count += (b == "1")
        return count
        
class Solution:
    ## Bit Shift

    # time complexity: O(B)
    # pace complexity: O(1)
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += (n & 1)
            n >>= 1
        return count

class Solution:
    ## Kernighan's Algorithm 
    
    # time complexity: O(set bits)
    # space complexity: O(1)
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= (n-1)
            count += 1
        return count
        