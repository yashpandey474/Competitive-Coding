class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        #FIND THE LONGEST COMMON SUBSEQUENCE
        cache = {} #INDEX1, INDEX2


        def dfs(index1, index2):
            if index1 >= len(str1) or index2 >= len(str2):
                return ""
            #CHECK IF IN CACHE
            if (index1, index2) in cache:
                return cache[(index1, index2)]

            
            #SAME CHARACTER
            cache[(index1, index2)] = ""
            if str1[index1] == str2[index2]:
                cache[(index1, index2)] = (
                    str1[index1] + dfs(index1 + 1, index2 + 1)
                )

            else:
                res1 = dfs(index1 + 1, index2)
                res2 = dfs(index1, index2 + 1)

                if len(res1) > len(res2):
                    cache[(index1, index2)] = res1

                else:
                    cache[(index1, index2)] = res2

            return cache[(index1, index2)]

        lcs = dfs(0, 0)
        i, j, result = 0, 0, ""
        #FOR EACH CHARACTER IN LCS
        for c in lcs:
            #WHILE STRING 1 DOESNT REACH CHARACTER
            while str1[i] != c:
                #ADD TO RESULT; NEXT INDEX
                result += str1[i]
                i += 1
        
            while str2[j] != c:
                result += str2[j]
                j += 1

            result += c
            i += 1
            j += 1
        return result + str1[i: ] + str2[j: ]

            
