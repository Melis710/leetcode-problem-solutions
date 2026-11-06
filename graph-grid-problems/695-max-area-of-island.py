from collections import deque
class Solution:
    # BFS solution
    # time complexity: O(MxN)
    # space complexity: O(MxN)
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        max_area = 0

        # run BFS for each source 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:  # already visited or water, skip it
                    continue
                
                # hit a land, explore the island (add num of neighbors level by level)
                area = 0
                queue = deque()
                queue.append((i, j))  # append the source node to the queue
                grid[i][j] = 0  # mark as visited

                while queue:
                    area += 1  # increment for each node in the queue
                    x, y = queue.popleft()  # node coordinates
                    for d0, d1 in directions:  # explore the neighbors
                        dx, dy = x + d0, y + d1  # (dx, dy) = neighbor coordinates
                        if (0 <= dx < m and 0 <= dy < n) and grid[dx][dy] == 1:
                            queue.append((dx, dy))  # if 1, append it to queue
                            grid[dx][dy] = 0  # mark as visited

                # update area
                max_area = max(max_area, area)

        return max_area

class Solution:
    # Recursive DFS solution
    # time complexity: O(MxN)
    # space complexity: O(MxN)
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            # check if coordinates valid
            if not (0 <= i < m and 0 <= j < n):
                return 0
            # check if already seen or water 
            if grid[i][j] == 0:
                return 0
            # we hit a land
            grid[i][j] = 0  # mark as visited
            return 1 + dfs(i-1, j) + dfs(i+1, j) + dfs(i, j-1) + dfs(i, j+1)  # itself + size of 4 neigboring subgraphs
        
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))

        return max_area

