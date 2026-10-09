class Solution:
    def rob(self, nums: List[int]) -> int:
        # Edge case: If there is only one house, we can only rob that one
        if len(nums) == 1:
            return nums[0]
            
        # Helper function to solve the linear House Robber problem
        def rob_helper(houses):
            rob1, rob2 = 0, 0
            for n in houses:
                temp = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
            
        # Since the houses are in a circle, we cannot rob both the first and the last house.
        # We take the maximum of robbing from house 0 to n-2, or house 1 to n-1.
        return max(rob_helper(nums[:-1]), rob_helper(nums[1:]))