import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        
        for x, y in points:
            # We don't need to compute the square root, 
            # as squared distance is sufficient for comparison.
            dist = (x ** 2) + (y ** 2)
            
            # Push negative distance to simulate a max-heap
            heapq.heappush(max_heap, (-dist, x, y))
            
            # If the heap size exceeds k, remove the farthest point
            if len(max_heap) > k:
                heapq.heappop(max_heap)
                
        # Extract the coordinates from the remaining k elements
        return [[x, y] for _, x, y in max_heap]