class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)

        # DP ARRAY
        dp = [[0]*(n2 + 1) for i in range(n1 + 1)]

        # LCS IS OF 0 LENGTH WHEN EITHER STRING IS EMPTY
        for i in range(n1 + 1):
            dp[i][0] = 0

        for i in range(n2 + 1):
            dp[0][i] = 0

        # BOTTOM-UP DP
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i-1][j-1] + 1

                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        for i in range(n1 + 1):
            print(dp[i])
        return dp[n1][n2]
        