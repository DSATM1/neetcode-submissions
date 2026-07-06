class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for item in nums:
            if item in seen:
                return True
            seen.add(item)
        return False