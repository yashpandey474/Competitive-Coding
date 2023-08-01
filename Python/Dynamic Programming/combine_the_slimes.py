from typing import *

def minCost(n: int, slimes) -> int:
    # write your code here
    arr = [i for i in range(100)]
    cache = {}

    def computeSize(left, right):
        ans = 0
        for i in range(left, min(n, right + 1)):
            ans += slimes[i]

        return ans%100

    def dfs(left, right):
        if left == right:
            return 0

        if (left, right) in cache:
            return cache[(left, right)]

        #STORE MINIMUM COST TO COMBINE
        ans = float('inf')
        for i in range(left, right):
            ans = min(
                ans,
                dfs(left, i) + dfs(i + 1, right) + computeSize(left, i)*computeSize(i + 1, right)
            )
        cache[(left, right)] = ans
        return ans

    return dfs(0, n - 1)
        
