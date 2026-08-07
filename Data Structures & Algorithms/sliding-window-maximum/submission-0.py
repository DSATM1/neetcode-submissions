from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # stores indices
        
        for i, val in enumerate(nums):
            # 1. Pop smaller elements from the back of the deque
            while q and nums[q[-1]] < val:
                q.pop()
            
            # 2. Append current index
            q.append(i)
            
            # 3. Remove indices from front if they are outside the current window
            if q[0] <= i - k:
                q.popleft()
            
            # 4. Add the max (front of deque) to output once first window is reached
            if i >= k - 1:
                output.append(nums[q[0]])
                
        return output