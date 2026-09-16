import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums
        # Transform the list into a min-heap in O(N) time
        heapq.heapify(self.min_heap)
        
        # Pop elements until we only have the k largest elements remaining
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        # Push the new value onto the heap
        heapq.heappush(self.min_heap, val)
        
        # If the heap exceeds size k, remove the smallest element
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
            
        # The root of the min-heap is the k-th largest element
        return self.min_heap[0]