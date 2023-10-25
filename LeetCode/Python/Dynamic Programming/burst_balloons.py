class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        #ADD 1S AT STARTING AND ENDING
        nums = [1] + nums + [1]

        #DP ARRAY
        cache = {}

        def dfs(L, R):
            if (L, R) in cache:
                return cache[(L, R)]

            if L > R:
                return 0

            #DETERMINE MAX COINS BY ITERATION
            cache[(L, R)] = 0
            for i in range(L, R+1):
                #IF CURRENT WAS LAST TO BE POPPED
                coins = nums[L-1]*nums[i]*nums[R+1]
                coins += dfs(L, i-1) + dfs(i+1, R)
                cache[(L, R)] = max(cache[(L, R)], coins)           
            return cache[(L, R)]
        return dfs(1, len(nums)-2)
