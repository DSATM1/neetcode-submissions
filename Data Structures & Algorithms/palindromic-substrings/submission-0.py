class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        # Helper function to count palindromes expanding from a center
        def countPali(l, r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count
        
        for i in range(len(s)):
            # Count odd-length palindromes (center is a single character)
            res += countPali(i, i)
            
            # Count even-length palindromes (center is between two characters)
            res += countPali(i, i + 1)
            
        return res