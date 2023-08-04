class Solution:
    def maxScore(self, nums: List[int]) -> int:
        cache = {}

        def dfs(mask, op):
            if mask in cache:
                return cache[mask]

            cache[mask] = 0
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    if (1 << i) & mask or (1 << j) & mask:
                        continue

                    newMask = mask | (1 << i) | (1 << j)
                    score = (op * math.gcd(nums[i], nums[j])) + dfs(newMask, op + 1)
                    cache[mask] = max(cache[mask], score)


            return cache[mask]

        return dfs(0, 1)
                
