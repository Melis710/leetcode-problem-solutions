class Solution:
    # Recursive DFS
    # time complexity: O(n)
    # space complexity: O(h)  h:height
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if root is None:
            return None
        
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

class Solution:
    # Iterative DFS
    # time complexity: O(n)
    # space complexity: O(h)
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if root is None:
            return None

        stack = [root]
        while stack:
            # pop node from stack
            node = stack.pop()
            # process the node
            node.left, node.right = node.right, node.left
            # push children of the node onto the stack
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return root

from collections import deque
class Solution:
    # Iterative BFS
    # time complexity: O(n)
    # space complexity: O(n)
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if root is None:
            return None

        queue = deque([root])
        while queue:
            # dequeue a node
            node = queue.popleft()
            # process
            node.left, node.right = node.right, node.left
            # enqueue the children of the node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return root
