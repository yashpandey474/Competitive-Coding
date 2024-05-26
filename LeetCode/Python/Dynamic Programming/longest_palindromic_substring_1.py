class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        dp = [[0]*n for i in range(n)]

        for i in range(n):
            dp[i][i] = 1

            if i < (n - 1):
                dp[i][i + 1] = 0 if s[i] != s[i + 1] else 1

        maxstr = s[0]
        maxval = 0
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1

                if s[i] == s[j]:
                    dp[i][j] = 1 if dp[i + 1][j - 1] or j - i < 3 else 0

                    if dp[i][j] and (j - i + 1) > maxval:
                        maxval = j - i + 1
                        maxstr = s[i:j + 1]

                
        return maxstr