# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base Case
        if not root:
            return 0
        # Recursive Case
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))  # +1 for this level, plus maximum depth of two branches
