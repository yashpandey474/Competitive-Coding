class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        #DP ARRAY: DP[I][J] = LENGTH OF LONGEST INCREASING PATH FROM CELL (I, J)

        cache = {}
        rows, columns = len(matrix), len(matrix[0])

        def dfs(row, column, previous):
            
            if row < 0 or column <0 or row >= rows or column >= columns or matrix[row][column] <= previous:
                return 0
            if (row, column, previous) in cache:
                return cache[(row, column, previous)]

        
            res = 1 + max(
                    dfs(row+1, column, matrix[row][column]),
                    dfs(row-1, column, matrix[row][column]),
                    dfs(row, column+1, matrix[row][column]),
                    dfs(row, column-1, matrix[row][column])
            )

            cache[(row, column, previous)] = res
            return res

        max_len = 0
        for row in range(rows):
            for column in range(columns):
                max_len = max(
                    max_len,
                    dfs(row, column, -float('inf'))
                )
                
        return max_len
