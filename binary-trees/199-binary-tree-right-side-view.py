from collections import deque
class Solution:
    # BFS level by level explicitly, enqueuing nodes from right to left
    # append the first node of each level (which is the rightmost node of each level since added from right to left)
    # time complexity: O(N)
    # space complexity: O(N)
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []

        queue = deque([root])
        res = []  # rightmost values at each level

        while queue:
            res.append(queue[0].val)  # append rightmost value of current level

            for _ in range(len(queue)): 
                node = queue.popleft()  # dequeue this level
                # enqueue new level from right to left nodes
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        
        return res