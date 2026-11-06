from collections import deque
class Solution:
    # Multi-Source BFS
    # time complexity: O(N^2)
    # space complexity: O(N^2)
    def shortestBridge(self, grid: list[list[int]]) -> int:
        # mark first island as -1 through DFS traversal, append all of its nodes as source to the queue 
        # find the shortest path to the second island, by running multi-source BFS

        n = len(grid)  # n x n
        queue = deque()
        def dfs(i, j):
            if not (0 <= i < n and 0 <= j < n):
                return 
            if grid[i][j] != 1:
                return

            grid[i][j] = -1  # mark as visited
            queue.append((i, j))
            dfs(i-1, j)
            dfs(i, j-1)
            dfs(i+1, j)
            dfs(i, j+1)

        first_visited = False
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    first_visited = True
                    break
            if first_visited:
                break
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        length = 0

        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()

                for d0, d1 in directions:
                    dx, dy = x + d0, y + d1
                    if 0 <= dx < n and 0 <= dy < n:
                        if grid[dx][dy] == 1:
                            return length

                        if grid[dx][dy] == 0:
                            grid[dx][dy] = -1  # mark as visited
                            queue.append((dx, dy))
            length += 1

        return -1
