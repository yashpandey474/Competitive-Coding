class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        #DP ARRAY: STORE PATH SUM FROM THIS ROW AND COLUMN
        rows = len(triangle)
        cache = {}

        def dfs(row, column):
            if row == rows:
                return 0

            if (row, column) in cache:
                return cache[(row, column)]

            cache[(row, column)] = float('inf')

            cache[(row, column)] = min(
                cache[(row, column)],
                triangle[row][column] + dfs(row + 1, column),
                triangle[row][column] + dfs(row + 1, column + 1)
            )
            
            if cache[(row, column)] == float('inf'):
                return 0
            
            return cache[(row, column)]

        return dfs(0, 0)
