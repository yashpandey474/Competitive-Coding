class Solution:
    def numTrees(self, n: int) -> int:

        cache = {}


        def dfs(n):
            if n == 2:
                return 2

            if n <= 1:
                return 1

            if n in cache:
                return cache[n]

            res = 0
            for i in range(1, n+1):
                res += dfs(n-i) * dfs(i-1)

            cache[n] = res
            return res
        
        return dfs(n)
        
        
