class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:

        #CACHE
        cache = {} #INDEX, PREVIOUS

        def dfs(index, previous):

            if index >= len(nums):
                return 0

            if (index, previous) in cache:
                return cache[(index, previous)]

            #PREVIOUS WAS SKIP
            res = 0
            if previous == "":
                #SKIP OR ADD
                res = max(
                    nums[index] + dfs(index + 1, "+"),
                    dfs(index + 1, "")
                )
                
            #PREVIOUS WAS ADD
            elif previous == "+":
                #SKIP OR SUBTRACT
                res = max(
                    dfs(index+1, "-") - nums[index],
                    dfs(index + 1, "+")
                )

            #PREVIOUS WAS SUBTRACT
            else:
                #ADD OR SKIP
                res = max(
                    dfs(index + 1, "+") + nums[index],
                    dfs(index + 1,  "-") 
                )

            cache[(index, previous)] = res
            return res

        return dfs(0, "")


