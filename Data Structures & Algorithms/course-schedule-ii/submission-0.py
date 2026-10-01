from collections import deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create an adjacency list and indegree array
        adj = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses
        
        # Populate the graph and indegrees (edge goes from prerequisite -> course)
        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs] += 1
            
        # Initialize queue with courses that have no prerequisites (indegree == 0)
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        order = []
        
        while queue:
            current = queue.popleft()
            order.append(current)
            
            # Decrease indegree for all neighbors (dependent courses)
            for neighbor in adj[current]:
                indegree[neighbor] -= 1
                # If indegree reaches 0, the course can now be taken
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    
        # If order length matches numCourses, a valid topological sort exists.
        # Otherwise, there is a cycle and we return an empty array.
        return order if len(order) == numCourses else []