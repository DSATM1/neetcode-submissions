from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Initialize parents and ranks for nodes 1 to n
        # We use len(edges) + 1 because nodes are 1-indexed
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            p = parent[n]
            while p != parent[p]:
                # Path compression to flatten the tree
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            # If they share the same parent, a cycle is detected
            if p1 == p2:
                return False

            # Union by rank to keep the tree balanced
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True

        # Iterate through edges and find the first one that creates a cycle
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]