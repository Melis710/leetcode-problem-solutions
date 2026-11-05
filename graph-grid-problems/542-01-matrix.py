from collections import deque
class Solution:
    # BFS
    # no need to process level by level because each cell individually processed
    # time complexity: O(MxN)
    # space complexity: O(MxN)
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        queue = deque()  # keeps 0 nodes because their distances already 0!
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # to traverse neighbors
        res = [[-1]*n for _ in range(m)]  # -1 for unseen 
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    res[i][j] = 0  # mark zeros
                
        while queue:
            x, y = queue.popleft()
            # search neighbors
            for d0, d1 in directions:
                dx, dy = x + d0, y + d1
                # check if valid node & unseen yet
                if (0 <= dx < m and 0 <= dy < n) and res[dx][dy] == -1:
                    res[dx][dy] = res[x][y] + 1
                    queue.append((dx, dy))
            
        return res
    