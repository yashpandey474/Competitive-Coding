class Solution(object):
    
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        #USE DYNAMIC PROGRAMMING
        dp = [float('inf')]*(amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            for j in coins:
                if j <= i:
                    dp[i] = min(dp[i], 1 + dp[i-j])

        print(dp)
        if dp[amount] == float('inf'):
            return -1
        
        return dp[amount]
