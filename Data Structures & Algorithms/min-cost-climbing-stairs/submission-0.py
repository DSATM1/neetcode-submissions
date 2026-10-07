class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # These variables keep track of the minimum cost to reach the previous two steps
        down_two = cost[0]
        down_one = cost[1]
        
        # Iterate from the 3rd step to the end
        for i in range(2, len(cost)):
            # The cost to reach the current step is the cost of the step itself 
            # plus the minimum cost of the two steps before it
            current = cost[i] + min(down_one, down_two)
            
            # Shift the variables forward for the next iteration
            down_two = down_one
            down_one = current
            
        # The top of the stairs can be reached from either the last step or the second to last step
        return min(down_one, down_two)