class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])  # dimensions as number of rows, number of columns
        # define helper Depth-First Search function
        def dfs(i, j, idx):  # coordinates i and j, idx the current index of word
            if idx == len(word):  # found all matching letters including last index (len-1)
                return True
            if not (0 <= i < m and 0 <= j < n):  # array boundary check
                return False
            if board[i][j] != word[idx]:  # standard pruning due to different letter
                return False
            
            board[i][j] = None  # here the letter matches so mark it to visited
            # explore neighbors recursively for remaining letters matches
            res = (dfs(i - 1, j, idx + 1) 
                   or dfs(i + 1, j, idx + 1)
                   or dfs(i, j - 1, idx + 1) 
                   or dfs(i, j + 1, idx + 1))
                
            board[i][j] = word[idx]  # undo step of backtracking

            return res  # return result

        for i in range(m):  # for every row
            for j in range(n):  # for every column
                if dfs(i, j, 0):  # immediately return True if word found
                    return True
        
        return False  # if here the word NOT FOUND
