import heapq
from collections import Counter, deque
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequencies of each task
        count = Counter(tasks)
        
        # Create a max heap (using negative values since Python has min-heap)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        
        time = 0
        # Queue will store pairs of [remaining_count, available_time]
        q = deque()
        
        while maxHeap or q:
            time += 1
            
            # Fast-forward time if the heap is empty but tasks are waiting in the queue
            if not maxHeap:
                time = max(time, q[0][1])
                
            if maxHeap:
                # Pop the most frequent task and decrement its frequency
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    # If the task still needs to be run, add it to the queue with its next available time
                    q.append([cnt, time + n])
                    
            # If the task at the front of the queue is ready, push it back to the heap
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
                
        return time