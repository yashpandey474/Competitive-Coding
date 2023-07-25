class Solution:
    def integerBreak(self, n: int) -> int:
        #BREAKING DOWN A NUMBER
        cache = {}
        def dfs(number):
            if number in cache:
                return cache[number]
            #BASE CASE
            if number == 1:
                #MAX PRODUCT
                return 1

            #CURRENT
            result = 0 if number == n else number
            for i in range(1, number):
                val = dfs(i) * dfs(number - i)
                result = max(result, val)
            cache[number] = result
            return result

        
        return dfs(n)
           

            

            
