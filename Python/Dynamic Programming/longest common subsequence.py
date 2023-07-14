class Solution(object):

    def recursion(self, text1, text2, dp,  i, j, n, m):

        if dp[i][j] < 0:
            if i == m or j == n:
                dp[i][j] = 0

            elif text1[i] == text2[j]:
                dp[i][j] =  1 + self.recursion(text1, text2,dp, i+1, j+1, n, m)
            
            else:
                dp[i][j] =  max(
                    self.recursion(text1, text2,dp, i+1, j, n, m),
                    self.recursion(text1, text2,dp,  i, j+1, n, m)
                )

        return dp[i][j]
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        #RECURSIVE SOLUTION
        #OPTIMIZE USING MEMOIZATION
        m = len(text1)
        n = len(text2)
        dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
        return self.recursion(text1, text2, dp,  0, 0, n, m)
