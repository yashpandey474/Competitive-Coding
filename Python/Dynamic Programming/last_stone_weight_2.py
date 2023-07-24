class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        #TOTAL SUM
        stoneSum  = sum(stones)
        #TARGET VALUE OF 2 GROUPS
        target = ceil(stoneSum / 2)
        #DP ARRAY
        cache = {}

        def dfs(index, total):
            if total >= target or index == len(stones):
                return abs(total - (stoneSum - total))
            
            if (index, total) in cache:
                return cache[(index, total)]
            else:
                cache[(index, total)] = min(
                dfs(index + 1, total),
                dfs(index + 1, total + stones[index]))
                return cache[(index, total)]

        return dfs(0, 0)
            
        
