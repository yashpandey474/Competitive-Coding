class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        #CACHE
        cache = {}

        def dfs(index):
            if index >= len(days):
                return 0

            if index in cache:
                return cache[index]

            cache[index] = float('inf')

            for d, c in zip([1, 7, 30], costs):
                j = index
                while j<len(days) and days[j] < days[index] + d:
                    j+=1

                cache[index] = min(cache[index], c + dfs(j))

            return cache[index]

        return dfs(0) 
