class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        part = []

        def dfs(i):
            # Base case: if we've reached the end of the string, add the partition
            if i >= len(s):
                res.append(part.copy())
                return
            
            # Explore all possible substrings starting from index i
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.pop() # Backtrack

        dfs(0)
        return res

    def isPali(self, s, l, r):
        # Helper function to check if a substring is a palindrome
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True