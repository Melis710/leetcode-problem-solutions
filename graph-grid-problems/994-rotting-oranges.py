from collections import deque
class Solution:
    # Multi-Source BFS (Breadth First Search)
    # time complexity: O(MxN)
    # space complexity: O(MxN)
    def orangesRotting(self, grid: list[list[int]]) -> int:
        queue = deque()
        m, n = len(grid), len(grid[0])
        num_fresh = 0  # number of fresh oranges
        # initialize queue with rotten oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:  # rotten
                    queue.append((i, j))  # append the node
                elif grid[i][j] == 1:  # fresh
                    num_fresh += 1
        # early exit if already none of them fresh 
        if num_fresh == 0:
            return 0  # 0 time needed

        time = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue: 
            time += 1  # new level of BFS
            # process the new level 
            for _ in range(len(queue)):
                x, y = queue.popleft()
                # process the neighbors
                for d in directions:
                    dx, dy = x + d[0], y + d[1]
                    if 0 <= dx < m and 0 <= dy < n and grid[dx][dy] == 1:
                        grid[dx][dy] = 2
                        num_fresh -= 1
                        queue.append((dx, dy))
            # if no fresh left, we found minimum time elapsed
            if num_fresh == 0:
                return time
            
        return -1
