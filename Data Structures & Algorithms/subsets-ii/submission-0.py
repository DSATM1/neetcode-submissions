class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Sort the array first so duplicates are adjacent
        nums.sort()
        res = []
        
        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return
            
            # Decision 1: Include the current element
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            
            # Decision 2: Exclude the current element
            # Skip all adjacent duplicates to avoid duplicate subsets
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
                
            backtrack(i + 1, subset)
            
        backtrack(0, [])
        return res