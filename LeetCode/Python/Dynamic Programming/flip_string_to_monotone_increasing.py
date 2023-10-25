class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:

        #CACHE
        cache = {} #INDEX, PREVIOUS

        def dfs(index, previous):
            #BASE CASE
            if index >= len(s):
                return 0

            if (index, previous) in cache:
                return cache[(index, previous)]

            #0S AND CURRENT IS 0
            res = 0
            if previous == "0" and s[index] == "0":
                #FLIP OR KEEP SAME
                res = min(
                    1 + dfs(index + 1,  "1"),
                    dfs(index + 1, "0")
                )

            if previous == "0" and s[index] == "1":
                #FLIP OR KEEP SAME
                res = min(
                    1 + dfs(index + 1, "0"),
                    dfs(index + 1, "1")
                )

            if previous == "1" and s[index] == "0":
                #HAVE TO FLIP
                res = 1 + dfs(index + 1, "1")
            
            if previous == "1" and s[index] == "1":
                #CANNOT FLIP
                res = dfs(index + 1, "1")

            cache[(index, previous)] = res
            return res

        return dfs(0, "0")
        

