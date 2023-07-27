class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        #CREATE THE DP ARRAY
        #DP[I] = LENGTH OF LCS AT THAT POINT
        n = len(nums)
        dp = [1 for _ in range(n)]
        dp_1 = [1 for _ in range(n)] 


        #FIND THE LCS
        max_len = 1
        for i in range(0, n):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j]+1
                        dp_1[i] = dp_1[j]
                
                    elif dp[i] == dp[j] + 1:
                        dp_1[i] += dp_1[j]

                max_len = max(max_len, dp[i])

        
        count = 0
        print(dp)
        print(dp_1)
        print(max_len)
        for i in range(n):
            if dp[i] == max_len:
                count += dp_1[i]

        return count
