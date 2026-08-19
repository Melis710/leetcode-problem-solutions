class Solution:
    # time complexity: O(n)
    # space complexity: O(n)
    def simplifyPath(self, path: str) -> str:
        stack = []  # stack for undo operations (..)

        for d in path.split("/"):  # for each directory name 
            if d == "" or d == ".":
                continue
            elif d == "..":  # go parent directory (backward - stack undo operation)
                if stack:
                    stack.pop()
            else:  # add directory name (forward - push onto the directory stack)
                stack.append(d)
        
        return "/" + "/".join(stack)

            
    