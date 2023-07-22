class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #DP ARRAY: DP[I][J] = IF SUBSTRINGS MATCH
        lenText = len(s)
        lenPattern = len(p)

        #INITIALISE THE ARRAY
        cache = {}
        def dfs(i, j):

            if (i, j) in cache:
                return cache[(i, j)]

            #PAR LIMITS
            if i>=len(s) and j>=len(p):
                return True

            if j>=len(p):
                return False

            match = i<len(s) and (s[i] == p[j] or p[j] == '.')

            if j+1 < len(p) and p[j+1] == "*":
                #DON'T USE STAR
                cache[(i, j)] = dfs(i, j+2) or (match and dfs(i+1, j))

                return cache[(i, j)]
                
                
            #ANY CHARACTER
            if match:
                cache[(i, j)] = dfs(i+1, j+1)
                return cache[(i, j)]

            else:
                cache[(i, j)] = False
                return cache[(i, j)]

        return dfs(0, 0)

                
            

