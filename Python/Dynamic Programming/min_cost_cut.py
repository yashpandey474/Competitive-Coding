class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        #USE CACHING FOR LENGTH OF STICK AND CUT POSITION
        cache = {}


        def dfs(left, right):
            #BASE CASE: NONE OF THE CUTS APPLY
            if right - left == 1:
                return 0

            if (left, right) in cache:
                return cache[(left, right)]

            cache[(left, right)] = float('inf')
            for cut in cuts:
                #CUT APPLIES
                if left < cut < right:
                    cache[(left, right)] = min(cache[(left, right)],
                    dfs(left, cut) + dfs(cut, right) + (right - left)
                    )
            cache[(left, right)] = (0 if cache[(left, right)] == float('inf') else cache[(left, right)])
            
            return cache[(left, right)]


        return dfs(0, n)
            
