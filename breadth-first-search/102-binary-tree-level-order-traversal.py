# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:  # early exit if no root
            return []

        res = []  # result to be returned
        queue = deque([root])  # initialize the queue with root node

        while queue:  # while queue is not empty
            n = len(queue)  # current number of nodes in the queue gives number of nodes for the current level
            level = []  # level traversal
            for _ in range(n): # first n nodes forms the traversal for this level
                node = queue.popleft()
                level.append(node.val)  # append the value 
                # enqueue children to the queue for next level traversal
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
            
        return res