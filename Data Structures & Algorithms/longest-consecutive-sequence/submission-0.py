class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest = 0
        
        for n in num_set:
            # Check if this number is the start of a sequence
            if (n - 1) not in num_set:
                length = 1
                
                # Continuously check for the next consecutive numbers
                while (n + length) in num_set:
                    length += 1
                    
                # Update the longest sequence found so far
                longest = max(longest, length)
                
        return longest