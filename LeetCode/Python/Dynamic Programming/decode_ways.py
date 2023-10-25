class Solution:
    def numDecodings(self, s: str) -> int:

        #SINGLE DIGIT OR DOUBLE DIGIT

        #DP ARRAY: NUMBER OF WAYS TO DECODE UPTILL ITH INDEC
        cache = {}
        def dfs(index):
            if index in cache:
                return cache[index]

            if index >= len(s):
                return 1
                
            if s[index] == '0':
                return 0

            if index == len(s)-1:
                return 1

            
            else:
                cache[index] = 0
                if s[index] == '1':
                    cache[index] += dfs(index + 2)

                elif s[index] == '2':
                    if s[index + 1] >= '0' and s[index + 1] <= '6':         
                        cache[(index)] += dfs(index + 2)


                cache[index] += dfs(index + 1)
                return cache[index]

        return dfs(0)


                    

                
