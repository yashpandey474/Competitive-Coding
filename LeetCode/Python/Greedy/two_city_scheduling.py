class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        #SORT THE COSTS
        costs = sorted(costs)
        n = len(costs)//2

        #CHOOSE CHEAPEST N PEOPLE
        cache = {}
        def dfs(index, a, b):
            if index >= len(costs):
                return 0

            if (index, a, b) in cache:
                return cache[(index, a, b)]

            cache[(index, a)] = float('inf')
            if a == n:
                cache[(index, a,  b)] = dfs(index + 1, a, b + 1) + costs[index][1]
            elif b == n:
                cache[(index, a, b)] = dfs(index + 1, a + 1, b) + costs[index][0]
            else:
                cache[(index, a, b)] = min(
                    dfs(index + 1, a + 1,  b) + costs[index][0],
                    dfs(index + 1, a, b + 1) + costs[index][1]
                )
            return cache[(index, a, b)]

        return dfs(0, 0, 0)
