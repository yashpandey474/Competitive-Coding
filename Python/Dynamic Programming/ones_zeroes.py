class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        #CREATE DP ARRAY
        cache = {}

        #DFS FUNCTION ON INDEX AND NUMBER OF 1S
        def dfs(index, zeroes, ones):
            if index >= len(strs):
                return 0
            if (index, zeroes, ones) in cache:
                return cache[(index, zeroes, ones)]

            else:
                zeroCount = strs[index].count("0")
                oneCount = strs[index].count("1")
                cache[(index, zeroes, ones)] = dfs(index + 1, zeroes, ones)
                if zeroCount <= zeroes and oneCount <= ones:
                    cache[(index, zeroes, ones)] = max(
                        cache[(index, zeroes, ones)],
                        1 + dfs(index + 1, zeroes - zeroCount , ones - oneCount )
                        )
                

                return cache[(index, zeroes, ones)]

        return dfs(0, m, n)
