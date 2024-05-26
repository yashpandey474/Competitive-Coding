class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        dp = [0]*(n + 1)

        dp[n] = 1

        wordDict = set(wordDict)

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i:j + 1] in wordDict:
                    dp[i] = max(dp[i], dp[j + 1])

        return dp[0]
