from collections import deque
class Solution:
    # shortest path --> implies BFS !!
    # this solution process the queue level by level because each level means length += 1
    # time complexity: O(N^2)
    # space complexity: O(N^2)
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)  # dimensions (n x n)
        src, dst = (0, 0), (n-1, n-1)
        if grid[src[0]][src[1]] != 0 or grid[dst[0]][dst[1]] != 0:
            return -1

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]  # 8 directions
        queue = deque()
        queue.append(src)  # append to queue
        grid[src[0]][src[1]] = 1  # mark as visited
        length = 0

        while queue:
            for _ in range(len(queue)):  # level by level
                x, y = queue.popleft()
                if (x, y) == dst:
                    return length + 1
                for d0, d1 in directions:  # explore neighbors
                    dx, dy = x + d0, y + d1
                    if (0 <= dx < n and 0 <= dy < n) and grid[dx][dy] == 0:
                        queue.append((dx, dy))  # append to queue
                        grid[dx][dy] = 1  # mark as visited
            length += 1

        return -1

class Solution:
    # this solution directly stores the length dynamically with nodes appended to queue
    # no need for "for loop" to separate levels
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)  # dimensions (n x n)
        src, dst = (0, 0), (n-1, n-1)
        if grid[src[0]][src[1]] != 0 or grid[dst[0]][dst[1]] != 0:
            return -1

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]  # 8 directions
        queue = deque()
        queue.append((src, 1))  # append to queue
        grid[src[0]][src[1]] = 1  # mark as visited
        
        while queue:
            (x, y), length = queue.popleft()
            if (x, y) == dst:
                return length
            for d0, d1 in directions:  # explore neighbors
                dx, dy = x + d0, y + d1
                if (0 <= dx < n and 0 <= dy < n) and grid[dx][dy] == 0:
                    queue.append(((dx, dy), length+1))  # append to queue
                    grid[dx][dy] = 1  # mark as visited
        
        return -1


        
        