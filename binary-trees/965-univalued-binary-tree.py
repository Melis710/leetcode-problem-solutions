class Solution:
    # Recursive DFS
    # time complexity: O(n)
    # space complexity: O(h)
    def isUnivalTree(self, root: TreeNode | None) -> bool:
        if not root:
            return True

        if root.left and root.left.val != root.val:
            return False
        
        if root.right and root.right.val != root.val:
            return False
        
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)

class Solution:
    # Iterative DFS
    # time complexity: O(n)
    # space complexity: O(h)
    def isUnivalTree(self, root: TreeNode | None) -> bool:
        stack = [root]

        while stack:
            node = stack.pop()
            
            if node.left and node.left.val != node.val:
                return False
            if node.right and node.right.val != node.val:
                return False
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return True


from collections import deque
class Solution:
    # Iterative BFS 
    # time complexity: O(n)
    # space complexity: O(n)
    def isUnivalTree(self, root: TreeNode | None) -> bool:
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node.left and node.left.val != node.val:
                return False
            if node.right and node.right.val != node.val:
                return False
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return True