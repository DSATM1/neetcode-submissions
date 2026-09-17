import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # Convert all stones to negative values to simulate a Max-Heap
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        # Process until there is 1 or 0 stones left
        while len(stones) > 1:
            # Pop the two heaviest stones (which are the most negative numbers)
            y = heapq.heappop(stones) 
            x = heapq.heappop(stones)
            
            # If they are not equal, push the remaining weight back into the heap
            if y != x:
                # Since y is more negative, y - x will give us the correct negative difference
                heapq.heappush(stones, y - x)
                
        # Return the absolute value of the remaining stone, or 0 if the heap is empty
        return -stones[0] if stones else 0