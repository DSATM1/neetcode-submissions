class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # dp[i] represents whether the substring s[:i] can be segmented
        dp = [False] * (len(s) + 1)
        dp[0] = True  # An empty string can always be segmented
        
        for i in range(1, len(s) + 1):
            for w in wordDict:
                # If the current word matches the end of the substring s[:i] 
                # and the rest of the substring s[:i - len(w)] can be segmented
                if i >= len(w) and s[i - len(w):i] == w:
                    if dp[i - len(w)]:
                        dp[i] = True
                        break  # Found a valid word ending at i, move to the next i
                        
        return dp[len(s)]