import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Initialize a min-heap with the first k elements
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        
        # Iterate through the rest of the array
        for num in nums[k:]:
            # If we find a number larger than our smallest number in the heap,
            # push it onto the heap and pop the smallest number
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)
                
        # The root of the min-heap is the kth largest element overall
        return min_heap[0]