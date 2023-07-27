class Solution:
        
    def canPartition(self, nums: List[int]) -> bool:
        #SUBSET WITH SUM == TOTAL SUM /2
        
        total_sum = sum(nums)

        #CANNOT BE PARTITIONED
        if total_sum % 2 != 0:
            return False

        #TARGET SUM TO BE REACHED
        target = total_sum // 2
        
        #CACHE
        cache = {}

        #DFS
        def dfs(index, current):
            if current == target:
                return True

            if index >= len(nums):
                return False

            if (index, current) in cache:
                return cache[(index, current)]

            res = (
                dfs(index + 1, current) or 
                dfs(index + 1, current + nums[index])
            )
            cache[(index, current)] = res
            return res

        return dfs(0, 0)
