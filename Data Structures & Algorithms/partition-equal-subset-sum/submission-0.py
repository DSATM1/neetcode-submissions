class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total_sum = sum(nums)
        
        # If the total sum is odd, it cannot be partitioned into two equal subsets
        if total_sum % 2 != 0:
            return False
            
        target = total_sum // 2
        dp = set([0])
        
        for num in nums:
            next_dp = set()
            for t in dp:
                # If we reach the target sum, we can partition the array
                if t + num == target:
                    return True
                next_dp.add(t + num)
                next_dp.add(t)
            dp = next_dp
            
        return target in dp