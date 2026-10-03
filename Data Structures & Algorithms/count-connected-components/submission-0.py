class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n
        components = n
        
        def find(node):
            # Path compression: point the node directly to its grandparent
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
            
        def union(node1, node2):
            root1, root2 = find(node1), find(node2)
            
            # If they are already in the same component, no components are merged
            if root1 == root2:
                return 0
                
            # Union by rank: attach the smaller tree under the larger tree
            if rank[root2] > rank[root1]:
                parent[root1] = root2
                rank[root2] += rank[root1]
            else:
                parent[root2] = root1
                rank[root1] += rank[root2]
                
            # Successfully merged two components into one
            return 1
            
        for n1, n2 in edges:
            components -= union(n1, n2)
            
        return components