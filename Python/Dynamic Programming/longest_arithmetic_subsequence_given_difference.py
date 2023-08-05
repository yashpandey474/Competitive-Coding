class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}

        for num in arr:
            prev = num - difference
            if prev in dp:
                dp[num] = dp[prev] + 1
            else:
                dp[num] = 1

        return max(dp.values())

