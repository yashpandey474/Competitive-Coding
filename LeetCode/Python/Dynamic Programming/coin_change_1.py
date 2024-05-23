class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [float('inf') for i in range(amount + 1)]

        dp[0] = 0
        for j in range(amount + 1):
            for i in range(n):
                if coins[i] <= j:
                    if dp[j - coins[i]] != float('inf'):
                        dp[j] = min(1 + dp[j - coins[i]], dp[j])
        
        return dp[amount] if dp[amount] != float('inf') else -1
