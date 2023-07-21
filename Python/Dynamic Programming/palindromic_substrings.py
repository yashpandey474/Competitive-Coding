class Solution:
    def countSubstrings(self, s: str) -> int:
        #DYNAMIC PROGRAMMING APPROACH

        #DP[I][J] IS TRUE IF SUBSTRING FROM I TO J IS A PALINDROME
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        count = 0
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                dp[i][j] = (s[i]==s[j]) and ((j-i<3) or dp[i+1][j-1])

                if dp[i][j]:
                    count += 1

        return count

        
