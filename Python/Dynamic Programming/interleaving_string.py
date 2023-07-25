class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)

        if (n1 + n2) != n3:
            return False

        #CACHE IF POSSIBLE
        cache = {} #INDEX1, INDEX2

        def dfs(index1, index2):
            if (index1, index2) in cache:
                return cache[(index1, index2)]

            if index1 >= n1 and index2 >= n2:
                return True

            #SET DEFAULT VALUE
            cache[(index1, index2)] = False
                
            #NUMBER OF CHARACTERS PROCESSED = POINTER IN THIRD STRING: INDEX1 + INDEX2 == INDEX3
            if index1 < n1 and s1[index1] == s3[index1 + index2]:
                cache[(index1, index2)]  = cache[(index1, index2)] or dfs(index1 + 1, index2)

            if index2 < n2 and s2[index2] == s3[index1 + index2]:
                cache[(index1, index2)] = cache[(index1, index2)] or dfs(index1, index2 + 1)

            return cache[(index1, index2)]

        return dfs(0, 0)
