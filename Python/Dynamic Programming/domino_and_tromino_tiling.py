class Solution:
    def numTilings(self, n: int) -> int:

        cache = {}

        #STATE 0 -> BOTH ROWS UNTILED
        #STATE 1 -> TOP ROW UNTILED
        #STATE 2 -> BOTTOM ROW UNTILED
        #STATE 4 -> BOTH TILED

        def dfs(index, t1, t2):
            if index == n:
                return 1

            if (index, t1, t2) in cache:
                return cache[(index, t1, t2)]

            #DO WE HAVE MORE THAN ONE COLUMN
            t3, t4 = index + 1 < n, index + 1 <n
            res = 0
            #BOTH ROWS TILED
            if not t1 and not t2:
                res += dfs(index + 1, True, True)

            #TOP ROW TILED
            if not t1 and t2 and t3 and t4:
                res += dfs(index + 1, False, False)

            if not t1 and t2 and t4:
                res += dfs(index + 1, True, False)

            if not t2 and t1 and t3 and t4:
                res += dfs(index + 1, False, False)

            if not t2 and t1 and t3:
                res += dfs(index + 1, False, True)

            if t1 and t2:
                res += dfs(index + 1, True, True)
            
            if t1 and t2 and t3:
                res += dfs(index + 1, False, True)
                
            if t1 and t2 and t4:
                res += dfs(index + 1, True, False)

            if t1 and t2 and t3 and t4:
                res += dfs(index + 1, False, False)

            
            cache[(index, t1, t2)] = res
            return res%(10**9 + 7)
                

        return dfs(0, True, True)
