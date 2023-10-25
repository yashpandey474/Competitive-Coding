class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs = sorted(pairs)
        dp = [1 for _ in range(n)]

        for i in range(n):
            for j in range(i):
                if pairs[j][1] < pairs[i][0] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j]+1

        return max(dp)
