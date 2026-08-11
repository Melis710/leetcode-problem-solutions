from collections import deque

class Solution:
    ## BFS solution
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:  # early exit
            return image
        
        m, n = len(image), len(image[0])  # dimensions
        starting_color = image[sr][sc]  # starting pixel's color
        image[sr][sc] = color  # mark visited changing the color to avoid duplicates
        queue = deque([(sr, sc)])  # initialize queue with the root

        while queue:  # while queue is non-empty
            sr, sc = queue.popleft()
            # enqueue neighbors with same starting color
            left, right, down, up = sc - 1, sc + 1, sr + 1, sr - 1
            if 0 <= left and image[sr][left] == starting_color:
                image[sr][left] = color   
                queue.append((sr, left))
            if right < n and image[sr][right] == starting_color:
                image[sr][right] = color
                queue.append((sr, right))
            if down < m and image[down][sc] == starting_color:
                image[down][sc] = color
                queue.append((down, sc))
            if 0 <= up and image[up][sc] == starting_color:
                image[up][sc] = color
                queue.append((up, sc))
            
        return image

class Solution2:
    ## DFS solution
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:  # early exit
            return image

        starting_color = image[sr][sc]  # save starting pixel's color before changing it
        m, n = len(image), len(image[0])  # dimensions (# of rows, # of columns)

        # define the Depth First Search function
        def dfs(root):
            sr, sc = root
            ## Base Cases
            if not (0 <= sr < m and 0 <= sc < n):  # invalid coordinates?
                return
            if image[sr][sc] != starting_color:  # not of same color?
                return

            ## Recursive Case
            image[sr][sc] = color  # mark as visited (change the color)
            # explore neighbors
            dfs((sr - 1, sc))  # up
            dfs((sr + 1, sc))  # down
            dfs((sr, sc - 1))  # left
            dfs((sr, sc + 1))  # right

        # call recursive dfs function
        dfs((sr, sc))

        return image  # return resulting image