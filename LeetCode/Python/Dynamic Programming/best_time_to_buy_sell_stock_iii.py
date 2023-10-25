class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #CACHE
        cache = {}

        #DFS
        def dfs(index, times, state):
            if index >= len(prices):
                return 0

            if times > 2:
                return 0
                
            if (index, times, state) in cache:
                return cache[(index, times, state)]

            res = 0
            if time == 2:
                #ALREADY BOUGHT AND SOLD TWICE
                if state:
                    return 0

                #HAVE TO SELL
                else:
                    #SELL OR SKIP
                    res = max(
                        dfs(index + 1, times, True) + prices[index],
                        dfs(index + 1, times, False)
                    )
            
            #LESS THAN TWICE
            else:
                #HAVE TO BUY
                if state:
                    #BUY OR SKIP
                    res = max(
                        dfs(index + 1, times + 1, False) - prices[index],
                        dfs(index + 1, times, True)
                    )

                #HAVE TO SELL
                else:
                    #SELL OR SKIP
                    res = max(
                        dfs(index + 1, times, True) + prices[index],
                        dfs(index + 1, times, False)
                    )

            #RETURN THE VALUE
            cache[(index, times, state)] = res
            return res

        #INITIALLY BUYING
        return dfs(0, 0, True)
