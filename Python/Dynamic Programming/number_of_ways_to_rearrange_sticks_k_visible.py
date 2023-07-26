class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:

        #CACHE
        cache = {}

        def dfs(nHere, addVisible):
            #EXCEPT THE LARGEST; PLACING ANY AT LAST MAKES IT UNVISIBLE [REDUCING N AND KEEPING K SAME]
            #ONLY ONE WAY: INCREASING ORDER
            if nHere == addVisible:
                return 1

            if nHere == 0 or addVisible == 0:
                return 0

            if (nHere, addVisible) in cache:
                return cache[(nHere, addVisible)]

            res = 0

            #PLACE LARGEST AT LAST OR
            #PLACE ANOTHER AT LAST
            res = dfs(nHere - 1, addVisible - 1) +  (nHere - 1)*dfs(nHere - 1, addVisible)

            cache[(nHere, addVisible)] = res
            return res%(10**9 + 7)

        return dfs(n, k)
