class Solution:
    def rob1(self, nums, low, hi):
        if low>=len(nums):
            return 0
        dp = [0 for _ in range(hi-low+1)]
        dp[0] = nums[low]
        dp[1] = max(nums[low], nums[low+1])

        for i in range(2, hi-low+1):
            dp[i] = max(dp[i-2]+nums[i+low], dp[i-1])
        
        return dp[hi-low]
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums:
            return 0

        return max(self.rob1(nums, 0, n-2), self.rob1(nums, 1, n-1))
