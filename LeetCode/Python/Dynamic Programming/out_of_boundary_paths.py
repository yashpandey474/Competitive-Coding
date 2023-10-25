class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        rows = m
        cols = n
        cache = {}
        visited = set()

        def dfs(row, col, moves):
            if (row, col, moves) in cache:
                return cache[(row, col, moves)]

            if row < 0 or col < 0 or row >= rows or col >= cols:
                return 1
            
            if moves == maxMove:
                return 0

            res = (
                dfs(row + 1, col, moves + 1)
                + dfs(row, col + 1, moves + 1)
                + dfs(row, col - 1, moves + 1)
                + dfs(row - 1, col, moves + 1)
            )

            cache[(row, col, moves)] = res
            return res%(10**9 + 7)

        return dfs(startRow, startColumn, 0)

            


            
