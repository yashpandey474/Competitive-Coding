class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #DYNAMIC ARRAY: NO OF WAYS TO GET TO AN AMOUNT J USING COINS FROM INDEX I
        

        cache = {}
        target = amount
        
        #DFS
        def dfs(index, current):
            if index >= len(coins):
                if current == target:
                    return 1
                return 0

            if current == target:
                return 1

            if current > target:
                return 0

            #ALREADY CACHED
            if (index, current) in cache:
                return cache[(index, current)]

            #CALCULATE
            res = 0
            for i in range(index, len(coins)):
                res += (
                    dfs(i, current + coins[i])
                )

            cache[(index, current)] = res
            return res
        
        return dfs(0, 0)
