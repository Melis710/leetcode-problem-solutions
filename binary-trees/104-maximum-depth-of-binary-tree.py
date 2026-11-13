class Solution:
    # Recursive DFS 
    # time complexity: O(N)
    # space complexity: O(H)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

class Solution:
    # Iterative DFS
    # time complexity: O(N)
    # space complexity: O(H)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stack = [(root, 1)]
        max_depth = 1
        while stack:
            node, depth = stack.pop()

            if not node.left and not node.right:
                max_depth = max(max_depth, depth)
            
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        
        return max_depth

from collections import deque
class Solution:
    # Iterative BFS
    # time complexity: O(N)
    # space complexity: O(N)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([(root, 1)])
        max_depth = 1
        while queue:
            node, depth = queue.popleft()
            # checking if leaf node is not necessary as in min depth
            # since it will get larger anyways
            max_depth = max(max_depth, depth)
            
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        
        return max_depth
            

        