class Solution:
    
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        def rob1(low, hi):
            if low>=len(nums):
                return 0
            dp = [0 for _ in range(hi-low+1)]
            dp[0] = nums[low]

            if low == hi:
                return dp[0]
            dp[1] = max(nums[low], nums[low+1])

            for i in range(2, hi-low+1):
                dp[i] = max(dp[i-2]+nums[i+low], dp[i-1])
            
            return dp[hi-low]

        return max(rob1(0, n-2),rob1(1, n-1))
