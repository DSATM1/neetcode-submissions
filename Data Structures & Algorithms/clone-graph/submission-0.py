"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Map to store the original node as the key and the cloned node as the value
        oldToNew = {}

        def dfs(node):
            if not node:
                return None
            
            # If the node has already been cloned, return the clone
            if node in oldToNew:
                return oldToNew[node]

            # Create a clone for the current node and add it to our map
            copy = Node(node.val)
            oldToNew[node] = copy

            # Recursively clone all neighbors and add them to the cloned node's neighbors list
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
                
            return copy

        return dfs(node)