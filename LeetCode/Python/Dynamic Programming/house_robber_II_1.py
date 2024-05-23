class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]

        if n == 2 or n == 3:
            return max(nums)
        
        def exec(flag):
            dp = [0]*n

            dp[0] = nums[flag]
            dp[1] = max(nums[0], nums[1]) if flag == 0 else dp[0] + nums[1]

            m = n - 1 if flag == 0 else n - 2
            for i in range(2, m):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

            return max(dp)

        return max(exec(0), exec(n - 1))
