class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                word[i] != board[r][c]):
                return False
            
            # Mark the cell as visited to prevent reuse in the current path
            temp = board[r][c]
            board[r][c] = '#'
            
            # Explore all 4 adjacent directions
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            
            # Backtrack and restore the original character
            board[r][c] = temp
            return res

        for r in range(ROWS):
            for c in range(COLS):
                # Start DFS if the first character matches
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
                    
        return False