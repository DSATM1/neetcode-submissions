class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        # Initialize result to the max number in the array to handle single negative element edge cases
        res = max(nums)
        curMin, curMax = 1, 1
        
        for n in nums:
            # Store curMax * n in a temporary variable before mutating curMax
            tmp = curMax * n
            
            # The new max could come from multiplying the current number by the previous max, 
            # by the previous min (if both are negative), or just the current number itself.
            curMax = max(tmp, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            
            res = max(res, curMax)
            
        return res