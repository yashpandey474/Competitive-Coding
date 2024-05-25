class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)

        if total % 2 != 0:
            return 0

        total = total // 2
        dp = [[0]*(total+1) for i in range(n)]

        for i in range(n):
            for j in range(total + 1):
                dp[i][j] = dp[i - 1][j]
                if nums[i] <= j:
                    dp[i][j] = max(dp[i - 1][j], nums[i] + dp[i - 1][j - nums[i]])

        return dp[n - 1][total] == total