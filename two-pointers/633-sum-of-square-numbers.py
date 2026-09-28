import math

class Solution:
    # Two Pointer solution
    # a and b can take values from 0 to square root of c
    # the values they can take on have a sorted nature like in two sum II problem
    # we can utilize this feature setting two pointers to leftmost and rightmost edges
    # then each iteration directing the current sum towards c
    
    # time complexity: O(sqrt(c))
    # space complexity: O(1)
    def judgeSquareSum(self, c: int) -> bool:
        a, b = 0, math.isqrt(c)  # set initial values

        while a <= b:  # scan value pairs in range from 0 to sqrt(c)
            res = a*a + b*b  # calculate current sum
            if res == c:  # found the pair! immediate return
                return True
            elif res > c:  # if current sum greater, make it smaller by moving right pointer towards left
                b -= 1
            else:  # res < c, make it greater by moving left pointer towards right
                a += 1
        
        return False