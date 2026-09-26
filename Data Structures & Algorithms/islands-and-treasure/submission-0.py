from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        
        # Step 1: Find all treasure chests and add them to the queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Step 2: Perform Multi-Source BFS
        while queue:
            r, c = queue.popleft()
            
            for dr, dc in directions:
                row, col = r + dr, c + dc
                
                # Check if the neighbor is in bounds and is an unvisited land cell (INF)
                if (0 <= row < ROWS and 
                    0 <= col < COLS and 
                    grid[row][col] == 2147483647):
                    
                    # Update distance and add to queue for further exploration
                    grid[row][col] = grid[r][c] + 1
                    queue.append((row, col))