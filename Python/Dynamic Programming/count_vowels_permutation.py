class Solution:
    def countVowelPermutation(self, n: int) -> int:

        #DFS FUNCTION
        cache = {}
        def dfs(length, previous):

            if (length, previous) in cache:
                return cache[(length, previous)]

            if length == n:
                return 1
            
            if length > n:
                return 0

            res = 0
            if previous == "":
                res += (dfs(length + 1, "a")
                + dfs(length + 1, "e")
                + dfs(length + 1, "i")
                + dfs(length + 1, "o")
                + dfs(length + 1, "u"))

            elif previous == "a":
                res += dfs(length + 1, "e")

            elif previous == "e":
                res += (dfs(length + 1, "a")
                + dfs(length + 1, "i"))
            elif previous == "i":
                res += (dfs(length + 1, "a")
                + dfs(length + 1, "e")
                + dfs(length + 1, "o")
                + dfs(length + 1, "u"))

            elif previous == "o":
                res += (dfs(length + 1, "u")
                + dfs(length + 1, "i"))

            elif previous == "u":
                res += dfs(length + 1, "a")

            cache[(length, previous)] = res %(10**9 + 7)
            return cache[(length, previous)]
                
        return dfs(0, "")
