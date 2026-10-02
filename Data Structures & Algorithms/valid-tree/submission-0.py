class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        # A valid tree must have exactly n - 1 edges. 
        # (This quick check prevents some edge cases, though the DFS will also catch them)
        if len(edges) != n - 1:
            return False

        # Build an adjacency list for the undirected graph
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
            
        visit = set()
        
        # DFS helper function to detect cycles
        def dfs(node, prev):
            if node in visit:
                return False # Cycle detected
            
            visit.add(node)
            
            for neighbor in adj[node]:
                # Skip the previous node to avoid false cycle detection
                if neighbor == prev:
                    continue
                # If a cycle is detected down the line, return False
                if not dfs(neighbor, node):
                    return False
                    
            return True
            
        # 1. Check if the graph has a cycle starting from node 0
        # 2. Check if all nodes were visited (graph is fully connected)
        return dfs(0, -1) and len(visit) == n