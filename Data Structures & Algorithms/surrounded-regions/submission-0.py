class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        ROWS, COLS = len(board), len(board[0])
        
        def capture(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return
            
            # Mark the unsurrounded 'O' as 'T'
            board[r][c] = "T"
            
            # Check all 4 adjacent directions
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)
            
        # 1. Capture unsurrounded regions (O -> T)
        for r in range(ROWS):
            for c in range(COLS):
                # If on the border and is an 'O', run DFS
                if board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
                    capture(r, c)
                    
        # 2. Capture surrounded regions (O -> X)
        # 3. Uncapture unsurrounded regions (T -> O)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"