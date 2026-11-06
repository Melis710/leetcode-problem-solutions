from collections import deque
class Solution:
    # shortest path --> implies BFS !
    # no need to maintain a min_length variable, BFS finds and returns once found by its nature
    # IMPORTANT: in this question, be careful about states to mark as visited. it's 3 dimensional !!
    # states marked as visited are not i, j. they also include remaining k !!
    # time complexity: O(MxN)
    # space complexity: O(MxNxK)
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if k >= m + n - 2:  # we can go straightforwardly, BIG OPTIMIZATION HERE !
            return m + n - 2

        queue = deque()
        queue.append((0, 0, k, 0))  # x, y, k, length
        visited = set()
        visited.add((0, 0, k))  # mark the state x, y, k as visited
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            x, y, k_remaining, length = queue.popleft()
            if x == m-1 and y == n-1:
                return length

            for d0, d1 in directions:
                dx, dy = x + d0, y + d1
                if 0 <= dx < m and 0 <= dy < n:
                    new_k = k_remaining - grid[dx][dy]  # if grid[dx][dy] == 1, decrements
                    if new_k >= 0 and (dx, dy, new_k) not in visited:
                        visited.add((dx, dy, new_k))
                        queue.append((dx, dy, new_k, length + 1))
        
        return -1 
