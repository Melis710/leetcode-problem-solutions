# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Iterative DFS (using stack data structure) solution
    # Idea: push nodes as well as current sum at that node as tuples onto the stack
    # time complexity: O(N), N: number of nodes
    # space complexity: O(N)
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if not root:
            return False

        stack = [(root, root.val)]  # (node, sum at that node)
        while stack:
            # pop a node
            node, curr_sum = stack.pop()

            # process the node
            if curr_sum == targetSum and not node.left and not node.right:  # if current sum is equal to the target sum at a leaf node
                    return True  # a path from the root to a leaf whose total is equal to target exist!
            
            # push node's children
            if node.left:
                stack.append((node.left, curr_sum + node.left.val))
            if node.right:
                stack.append((node.right, curr_sum + node.right.val))

        return False

class Solution:
    # Recursive DFS 
    # maintaining a separate current sum state as argument between calls
    # time complexity: O(N)
    # space complexity: O(H)

    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        def helper(root, curr_sum) -> bool:
            if not root:
                return False
            
            if not root.left and not root.right:
                return (curr_sum + root.val) == targetSum
            
            return helper(root.left, curr_sum + root.val) or helper(root.right, curr_sum + root.val)
            
        return helper(root, 0)
        
class Solution:
    # Recursive DFS
    # time complexity: O(N)
    # space complexity: O(H), H is the height of tree
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return root.val == targetSum
        
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)