class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        # dp2 represents dp[i-2], dp1 represents dp[i-1]
        dp2, dp1 = 1, 1
        
        for i in range(1, len(s)):
            current = 0
            
            # 1. Single digit decode check
            if s[i] != '0':
                current += dp1
                
            # 2. Two digit decode check
            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <= 26:
                current += dp2
                
            # Move sliding window forward
            dp2 = dp1
            dp1 = current
            
        return dp1