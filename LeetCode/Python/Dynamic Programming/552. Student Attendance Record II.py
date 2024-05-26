class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 10**9 + 7

        # INDEX, NUMBER OF TOTAL As, NUMBER OF CONSECUTIVE Ls SO FAR
        dp = [[ [0]*3 for j in range(2)] for i in range(n + 1)]

        for j in range(2):
            for k in range(3):
                dp[0][j][k] = 1

        # LENGTH OF STRING
        for i in range(1, n + 1):
            # NUMBER OF TOTAL As USED ALREADY
            for j in range(2):
                # NUMBER OF CONSECUTIVE Ls SO FAR
                for k in range(3):
                    #  ADD A P
                    dp[i][j][k] = dp[i - 1][j][0]

                    if k < 2:
                        dp[i][j][k] += dp[i - 1][j][k + 1]

                    if j < 1:
                        dp[i][j][k] += dp[i - 1][j + 1][0]

                    dp[i][j][k] %= mod 



        return dp[n][0][0]

