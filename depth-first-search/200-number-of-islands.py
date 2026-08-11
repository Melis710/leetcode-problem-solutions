class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        # helper depth-first search function
        def dfs(i, j):
            ## Base Case
            if not (0 <= i < m and 0 <= j < n):  # array boundary check
                return
            if grid[i][j] == '0':  # value check
                return

            ## Recursive Case
            grid[i][j] = '0'  # turn "1" into "0"
            dfs(i - 1, j)  # explore above neighbor
            dfs(i + 1, j)  # explore below neighbor
            dfs(i, j - 1)  # explore left neighbor
            dfs(i, j + 1)  # explore right neighbor

        for i in range(m):  # iterate through rows
            for j in range(n):  # iterate through columns
                if grid[i][j] == "1":  # if a land encountered, explore the island
                    count += 1
                    dfs(i, j)

        return count
                    