class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        #DYNAMIC PROGRAMMING

        #FIND LCS; IF EQUAL TO LENGTH OF T: TRUE

        #CACHE TO STORE LCS UPTILL I, J
        cache = {} #INDEX1, INDEX2

        def dfs(index1, index2):
            
            if index2 >= len(t):
                return 1

            if index1 >= len(s):
                return 0

            if (index1, index2) in cache:
                return cache[(index1, index2)]


            cache[(index1, index2)] = 0
            
            #CHARACTERS MATCH
            if s[index1] == t[index2]:
                cache[(index1, index2)]  = dfs(index1 + 1, index2 + 1) + dfs(index1 + 1, index2)

            else:
                cache[(index1, index2)] = dfs(index1 + 1, index2)

            return cache[(index1, index2)]

        return dfs(0, 0)
