class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        m = max(nums)
        dp = [0 for i in range(10001)]

        for i in range(n):
            dp[nums[i]] += nums[i]

        for i in range(2, max(nums) + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + dp[i])

        print(dp[:max(nums) + 1])
        return dp[max(nums)]