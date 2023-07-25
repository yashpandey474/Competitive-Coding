class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        #CACHE
        cache = {} #(INDEX11, INDEX2)

        #FIND THE REVERSE OF STRING
        revString = s[::-1]
        n = len(s)
        
        #FIND THE LCS BETWEEN STRING AND ITS REVERSE
        cache = {}
        
        #RECURSIVE FUNCTION
        def dfs(index1, index2):
            if (index1, index2) in cache:
                return cache[(index1, index2)]

            if index1 >= n or index2 >= n:
                return 0

            cache[(index1, index2)] = 0

            if s[index1] == revString[index2]:
                cache[(index1, index2)] = 1 + dfs(index1 + 1, index2 + 1)

            else:
                cache[(index1, index2)] = max(
                    dfs(index1 + 1, index2),
                    dfs(index1, index2 + 1)
                    )

            return cache[(index1, index2)]
            
        return dfs(0, 0)
