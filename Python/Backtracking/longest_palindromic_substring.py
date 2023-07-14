class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #DP[I][J] REPRESENTS IF S[I:J+1] IS A PALINDROME
        n = len(s)
        dp = [['' for _ in range(n)] for _ in range(n)]
        ans = ""
        
        #I STARTS FROM END
        #J GOES FROM I TO END
        for i in range(n-1, -1, -1):
            for j in range(i, n, 1):
                dp[i][j] = (s[i] == s[j]) and (j-i < 3 or dp[i+1][j-1])

                if dp[i][j] and (j-i+1 > len(ans)):
                    ans = s[i:j+1]

        return ans

