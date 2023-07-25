class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        #CACHE THE MAX POINTS UPTO AN INDEX
        cache = {}

        def dfs(index):
            if index >= len(questions):
                return 0

            if index in cache:
                return cache[index]

            cache[index] = 0

            cache[index] = max(
                questions[index][0] + dfs(index + questions[index][1] + 1),
                dfs(index + 1)
            )

            return cache[index]

        return dfs(0)
