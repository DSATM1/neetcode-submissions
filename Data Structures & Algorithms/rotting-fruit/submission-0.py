from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        
        # Step 1: Initialize queue with rotten fruits and count fresh fruits
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_count += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))
        
        # If there are no fresh fruits initially, 0 minutes are needed
        if fresh_count == 0:
            return 0
            
        minutes_passed = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Step 2: Multi-source BFS traversal
        while queue and fresh_count > 0:
            minutes_passed += 1
            # Process all rotting fruits at the current minute
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    
                    # Check bounds and if the adjacent cell is a fresh fruit
                    if 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == 1:
                        # Rot the fruit
                        grid[row][col] = 2
                        fresh_count -= 1
                        queue.append((row, col))
                        
        # Step 3: Check if all fresh fruits have rotted
        return minutes_passed if fresh_count == 0 else -1