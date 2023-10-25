class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:

        #LENGTH BETWEEN LOW OR HIGH
        count = 0
        cache = {}
        def dfs(length):
            nonlocal count
            if length == high:
                return 1
            if length > high:
                return 0
            
            if length in cache:
                return cache[length]

            cache[length] = 0
            if low <= length <= high:
                cache[length] = 1
            
            cache[length] += dfs(length + zero) + dfs(length + one)

            return cache[length]%(10**9 + 7)

        return dfs(0)
                
