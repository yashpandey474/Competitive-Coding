class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #STORE MAX PROFIT DEPENDING ON INDEX AND STATE
        cache = {}

        def dfs(index, state):
            if index >= len(prices):
                return 0

            
            if (index, state) in cache:
                return cache[(index, state)]

            
            cache[(index, state)] = 0
            #BUYING: BUY OR DON'T
            if state:
                cache[(index, state)] = max(
                    dfs(index + 1, False) - prices[index],
                    dfs(index + 1, True)
                )

            #NOT BUYING
            else:
                cache[(index,state)] = max(
                    dfs(index + 1, True) + prices[index],
                    dfs(index + 1, False)
                ) 

            return cache[(index, state)]

        return dfs(0, True)
