class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        #DEFINE A CACHE
        cache = {}

        #DEFINE A DFS FUNCTION
        def dfs(start, end):
            if start == end:
                return nums[start]

            if (start, end) in cache:
                return cache[(start, end)]

            #SUBTRACT NEXT SCORE TO GET DIFF BETWEEN SCORES
            score1 = nums[start] - dfs(start + 1, end)
            score2 = nums[end] - dfs(start, end - 1)

            res = max(score1, score2)

            cache[(start, end)] = res
            return res

        score = dfs(0, len(nums)-1)
        return score >= 0
