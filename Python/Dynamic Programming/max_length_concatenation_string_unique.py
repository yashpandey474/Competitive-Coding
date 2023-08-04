class Solution:
    def maxLength(self, arr: List[str]) -> int:
        max_len = 0
        cache = {}

        def isUnique(string):
            return len(set(string)) == len(string)

        def dfs(index, current):
            #NON UNIQUE
            if not isUnique(current):
                return 0
            #ALL EXHAUSTED
            if index >= len(arr):
                return (len(current) if isUnique(current) else 0)

            #CACHE
            if (index, current) in cache:
                print("CACHE USED")
                return cache[(index, current)]

            #CALCULATE
            res = max(
                #CURRENT
                len(current),
                #NOT TAKE AND GO
                dfs(index + 1, current),
                #TAKE AND GO
                dfs(index + 1, current + arr[index])
            )
            cache[(index, current)] = res
            return res

        return dfs(0, "")
            

            

