class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        #CREATE A CACHE
        cache = {}


        #A RECURSIVE DFS FUNCTION
        def dfs(index1, index2):
            if index1 == len(s1) and index2 == len(s2):
                return 0

            if index1 >= len(s1):
                res = 0
                for i in range(index2, len(s2)):
                    res += ord(s2[i])
                return res

            if index2 >= len(s2):
                res = 0
                for i in range(index1, len(s1)):
                    res += ord(s1[i])
                return res

            #ALREADY COMPUTED
            if (index1, index2) in cache:
                return cache[(index1, index2)]

            #EQUAL CHARACTER
            res = float('inf')
            if s1[index1] == s2[index2]:
                res = dfs(index1 + 1, index2 + 1)

            #UNEQUAL CHARACTERS
            else:
                res = min(
                    ord(s1[index1]) + dfs(index1 + 1, index2),
                    ord(s2[index2]) + dfs(index1, index2 + 1)
                )

            cache[(index1, index2)] = res
            return res
        return dfs(0, 0)

            
