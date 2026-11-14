from collections import deque
class Solution:
    # BFS 
    # Process the tree level by level. At each level the very first node is a leftmost node.
    # After the completion of traversal, we reach the bottom level's leftmost node.
    # time complexity: O(n)
    # space complexity: O(n)
    def findBottomLeftValue(self, root: TreeNode | None) -> int:
        queue = deque([root])
        
        while queue:
            leftmost = queue[0].val  # node value at the front of the queue is the leftmost

            for _ in range(len(queue)):  # dequeue the level, enqueue the next level 
                node = queue.popleft()
                # add level from left to right
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return leftmost

class Solution:
    # more elegant solution: BFS Traversal from RIGHT to LEFT
    # BFS already process nodes level by level
    # if we add right nodes before lefts, at the end of the traversal we get leftmost bottom node
    # time complexity: O(N)
    # space complexity: O(N)
    def findBottomLeftValue(self, root: TreeNode | None) -> int:
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            # add right node before left
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        
        return node.val  # the last traversed element is bottom leftmost 