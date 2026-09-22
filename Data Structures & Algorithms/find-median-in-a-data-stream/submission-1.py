import heapq

class MedianFinder:
    def __init__(self):
        # Two heaps: large is a min-heap for the upper half, small is a max-heap for the lower half.
        # Since Python's heapq only supports min-heaps, we multiply values by -1 to simulate a max-heap for 'small'.
        self.small = [] 
        self.large = [] 

    def addNum(self, num: int) -> None:
        # Default to adding into the max-heap (small)
        heapq.heappush(self.small, -num)

        # Ensure all elements in small are <= all elements in large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Balance the sizes so they differ by at most 1
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        # If lengths are unequal, the median is the root of the larger heap
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        if len(self.large) > len(self.small):
            return float(self.large[0])
        
        # If lengths are equal, the median is the average of the two roots
        return (-self.small[0] + self.large[0]) / 2.0