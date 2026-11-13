# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Iterative DFS (with stack data structure) solution
    # time complexity: O(N)
    # space complexity: O(H)

    def minDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        min_depth = float("inf")
        stack = [(root, 1)]
        while stack:
            node, curr_depth = stack.pop()
            if not node.left and not node.right:
                min_depth = min(min_depth, curr_depth)
            
            if node.left:
                stack.append((node.left, curr_depth + 1))
            if node.right:
                stack.append((node.right, curr_depth + 1))
        
        return min_depth

from collections import deque
class Solution:
    # Iterative BFS solution
    # enqueue node - depth pairs to the queue
    # time complexity: O(N)
    # space complexity: O(N)
    def minDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        queue = deque([(root, 1)])  # node, current depth
        min_depth = float("inf")

        while queue:
            node, depth = queue.popleft()  # dequeue a node
            if not node.left and not node.right:  # if leaf node
                min_depth = min(min_depth, depth)  # update minimum depth
            # enqueue children to the queue
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        
        return min_depth

class Solution:
    # Recursive DFS (utilizes underlying call stack)
    # time complexity: O(N)
    # space complexity: O(H)
    def minDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        
        if not root.left and not root.right:  # leaf node
            return 1
        
        left_depth, right_depth = float("inf"), float("inf")
        if root.left: 
            left_depth = self.minDepth(root.left)  # depth of tree rooted at left child
        if root.right:
            right_depth = self.minDepth(root.right)  # depth of tree rooted at right child
        return 1 + min(left_depth, right_depth)