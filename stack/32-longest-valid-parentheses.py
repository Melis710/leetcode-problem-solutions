class Solution:
    # Solution Utilizing Stack
    # Two Phases: 
    # * Phase 1: Mark each parenthesis either valid or invalid
    # * Phase 2: Find the max consecutive valid parentheses

    # time complexity: O(n)
    # space complexity: O(n)
    def longestValidParentheses(self, s: str) -> int:
        ## Phase 1: Determine validity of parentheses
        stack = []  # hold opening parentheses
        validity_bits = [0]*len(s)  # initialize array of validity bits, all invalid (0)initially

        for i, c in enumerate(s):
            if c == "(":  # add opening parenthesis to the stack
                stack.append(i)
            elif c == ")":  # if closing parenthesis has a match, mark both as valid (1)
                if stack:
                    validity_bits[stack.pop()] = 1  # for matching opening parenthesis
                    validity_bits[i] = 1  # for closing parenthesis

        ## Phase 2: Find max consecutive ones from an array consisting of 1s and 0s
        longest = 0  # longest length to find and return
        length = 0  # current window length (count of 1s)
        for bit in validity_bits:
            if bit:  # if bit = 1
                length += 1  # update window length
                longest = max(longest, length)  # update longest length
            else:  # bit = 0
                length = 0  # reset the window 

        return longest


class Solution2:
    # Two Pass Solution: from left to right (forward), from right to left (backward)
    # * From Left to Right Traversal: Handles invalid closing parentheses
    # * From Right to Left Traversal: Handles invalid opening parentheses

    # time complexity: O(n)
    # space complexity: O(1)
    def longestValidParentheses(self, s: str) -> int:
        left = right = longest = 0  # number of left parentheses, number of right, longest valid length

        ## Forward Pass
        for p in s:
            if p == ")":
                right += 1
            else:  # p = "("
                left += 1

            if right > left:  # excess of ")" makes it invalid, reset left and right counters
                left = right = 0
            elif left == right:  # valid substring
                longest = max(longest, 2*left)  # update valid longest length

        left = right = 0  # reset number of left and right parentheses
        ## Backward Pass
        for p in reversed(s):
            if p == "(":
                left += 1
            else:  # p = ")"
                right += 1

            if left > right:  # excess of "(" makes it invalid, reset left and right counters
                left = right = 0
            elif left == right:  # valid substring
                longest = max(longest, 2*left)  # update valid longest length

        return longest

class Solution3:
    # Single Pass & Stack Solution (Anchor Method)
    # Stack holds the last invalid index as boundary and indices of opening parentheses
    
    # time complexity: O(n)
    # space complexity: O(n)
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # for "()" 1 - (-1) = 2, initialize the boundary as -1
        longest = 0  # longest length to find

        for i, p in enumerate(s):
            if p == "(":
                stack.append(i)
            else:  # p = ")"
                stack.pop()  # pop out the last matching parenthesis or last invalid boundary
                if stack:  # if still non-empty, update longest
                    longest = max(longest, i - stack[-1])
                else:  # we have ")" and stack empty, push the invalid index onto the stack instead of the popped out invalid index
                    stack.append(i)
        
        return longest