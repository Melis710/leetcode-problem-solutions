class Solution:
    # Filter out the invalid parentheses
    # How to decide if a parenthesis is valid or not?
    # * Any opening parentheses remaining at the stack are invalid.
    # * Any closing parentheses encountered when the stack holding opening parentheses is empty is invalid.

    # time complexity: O(n)
    # space complexity: O(n)
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        invalid_indices = set()
        valid_str = []

        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if not stack:
                    invalid_indices.add(i)
                else:
                    stack.pop()
            
        for i in stack:
            invalid_indices.add(i)
        
        for i, c in enumerate(s):
            if i not in invalid_indices:
                valid_str.append(c)
          
        return "".join(valid_str)