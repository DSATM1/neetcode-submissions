from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        ROWS, COLS = len(matrix), len(matrix[0])
        
        # Treat the 2D matrix as a 1D array for binary search
        left, right = 0, ROWS * COLS - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Convert 1D index back into 2D row and column indices
            row = mid // COLS
            col = mid % COLS
            
            mid_val = matrix[row][col]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False