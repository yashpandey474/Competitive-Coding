class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        #GET DIMENSIONS
        rows, columns = len(matrix), len(matrix[0])

        #CACHE
        cache = {}


        #DFS
        def dfs(row, column):
            #OUT OF BOUNDS
            if row < 0 or column < 0 or row >= rows or column >= columns:
                return float('inf')

            #ALREADY DONE
            if (row, column) in cache:
                return cache[(row, column)]

            #LAST ROW
            if row == rows - 1:
                return matrix[row][column]

            res = float('inf')

            res = matrix[row][column] + min(
                 dfs(row + 1, column),
                 dfs(row + 1, column + 1),
                 dfs(row + 1, column - 1)
            )

            #CACHE THE RESULT
            cache[(row, column)] = res
            return res

        #START AT ALL IN FIRST ROW
        res = float('inf')
        for i in range(columns):
            res = min(
                res, 
                dfs(0, i)
            )

        return res
