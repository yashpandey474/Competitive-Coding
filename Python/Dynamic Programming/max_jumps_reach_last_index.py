class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        cache = {}

        def dfs(index):
            if index >= len(nums)-1:
                return 0

            if index in cache:
                return cache[index]

            res = -1
            for i in range(index + 1, len(nums)):
                if abs(nums[i] - nums[index]) <= target:
                    current = dfs(i)
                    if current == -1:
                        continue
                    else:
                        res = max(
                            res, current + 1
                        )

            cache[index] = res
            return res

        return dfs(0)
