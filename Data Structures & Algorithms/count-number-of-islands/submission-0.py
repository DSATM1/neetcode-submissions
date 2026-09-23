class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        num_islands = 0

        def dfs(r, c):
            # Base case: check if out of bounds or at a water cell
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return
            
            # Mark the current land cell as visited by turning it into water
            grid[r][c] = "0"
            
            # Recursively run DFS in all 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Iterate through every cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    num_islands += 1
                    dfs(r, c)

        return num_islands