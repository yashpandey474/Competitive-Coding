class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0]*n for i in range(2)]

        dp[1][n - 1] = prices[n - 1]
        dp[0][n - 1] = 0

        for i in range(n - 2, -1, -1):
            for j in range(2):
                if j == 0:
                    dp[j][i] = max(-prices[i] + dp[1][i + 1], dp[j][i + 1])

                else:
                    if i < n - 2:
                        dp[j][i] = max(prices[i] + dp[0][i + 2], dp[j][i + 1])
                    else:
                        dp[j][i] = max(prices[i], dp[j][i + 1])
        
        return dp[0][0]