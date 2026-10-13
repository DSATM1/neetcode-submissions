class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # Initialize an array to store the minimum coins for each amount.
        # (amount + 1) acts as an "infinity" placeholder.
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        # Build the DP table bottom-up
        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - c])
                    
        # If the amount hasn't changed from our "infinity" placeholder, it's impossible.
        return dp[amount] if dp[amount] != amount + 1 else -1