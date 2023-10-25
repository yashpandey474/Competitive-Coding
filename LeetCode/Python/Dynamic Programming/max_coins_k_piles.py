class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:

        #CACHE
        cache = {}
        n = len(piles)

        #DFS
        def dfs(numberCoins, index):
            if numberCoins == 0:
                return 0

            if index >= len(piles):
                return 0

            if (numberCoins, index) in cache:
                return cache[(numberCoins, index)]

            #SKIP CURRENT PILE
            res = dfs(numberCoins, index + 1)
            #COLLECT FROM CURRENT PILE
            curPile = 0
            
            for j in range(min(numberCoins, len(piles[index]))):
                curPile += piles[index][j]
                #MAX COINS ON TAKING 1 COIN FROM CURRENT
                res = max(
                    res,
                    curPile + dfs(numberCoins - j - 1, index + 1))
            cache[(numberCoins, index)] = res
            return res

        return dfs(k, 0)
