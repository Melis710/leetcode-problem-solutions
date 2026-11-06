from collections import deque
class Solution:
    # BFS solution
    # time complexity: O(MxN)
    # space complexity: O(min(M, N))
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m, n = len(grid), len(grid[0]) # dimensions (num of rows, num of cols)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        count = 0  # num of islands
        
        ## IDEA: APPLY BFS FROM EACH SOURCE UNVISITED AND INCREMENT COUNT 
        for i in range(m):
            for j in range(n):
                # node = (i, j)
                if grid[i][j] == "0":  # skip water
                    continue

                # hit a land, start BFS
                queue = deque()
                queue.append((i, j))  # start with source
                grid[i][j] = "0"  # mark as visited (making a land water)
                while queue:
                    x, y = queue.popleft()
                    for d0, d1 in directions:  # explore neighbors
                        dx, dy = x + d0, y + d1
                        if (0 <= dx < m and 0 <= dy < n) and grid[dx][dy] == "1":
                            grid[dx][dy] = "0"  # mark as visited
                            queue.append((dx, dy))  # append it to queue                  
                
                count += 1  # new component explored
        
        return count 

