class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:


        #CACHE
        cache = {}


        #DFS
        def dfs(index, state):
            #OUT OF BOUNDS
            if index >= len(prices):
                return 0

            #ALREADY PROCESSED
            if (index, state) in cache:
                return cache[(index, state)]

            cache[(index, state)] = 0
            #BUYING
            if state:
                #BUY OR SKIP
                cache[(index, state)] = max(
                    dfs(index + 1, False) - prices[index] - fee,

                    dfs(index + 1, True)
                )
            #SELLING
            else:
                #SELL OR SKIP
                cache[(index, state)] = max(
                    dfs(index + 1, True) + prices[index],
                    dfs(index + 1, False)
                )

            #RETURN
            return cache[(index, state)]

        #INITIALLY BUYING
        return dfs(0, True)

                
