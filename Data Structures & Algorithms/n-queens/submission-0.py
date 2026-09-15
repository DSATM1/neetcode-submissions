class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set() # (r + c)
        negDiag = set() # (r - c)
        
        res = []
        board = [["."] * n for _ in range(n)]
        
        def backtrack(r):
            # Base case: If we've successfully placed n queens (reached row n)
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            # Try placing a queen in each column of the current row 'r'
            for c in range(n):
                # Check if the column or diagonals are already under attack
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                
                # Place the queen and mark the column and diagonals as attacked
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"
                
                # Move to the next row
                backtrack(r + 1)
                
                # Backtrack: Remove the queen and unmark the attacked zones
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
        
        backtrack(0)
        return res