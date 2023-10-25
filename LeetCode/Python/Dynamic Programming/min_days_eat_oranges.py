class Solution:
    def minDays(self, n: int) -> int:
        cache = {0: 0, 1:1}

        def dfs(oranges):
            if oranges in cache:
                return cache[oranges]

            two = 1 + (oranges % 2) + dfs(oranges // 2)
            three = 1 + (oranges % 3) + dfs(oranges // 3)
            res = min(two, three)

            cache[oranges] = res
            return res

        return dfs(n)

            
