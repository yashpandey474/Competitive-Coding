class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        #GET DIMENSIONS
        rows, columns = len(matrix), len(matrix[0])
        #STORE MAXIMAL SQUARE FROM A POSITION
        cache = {}

        def dfs(row, column):

            if row < 0 or column < 0 or row >= rows or column >= columns:
                return 0

            if (row, column) in cache:
                return cache[(row, column)]

            down = dfs(row + 1, column)
            right = dfs(row, column + 1)
            diagonal = dfs(row + 1, column + 1)
            
            res = 0
            #ATLEAST A 1 AREA SQUARE
            if matrix[row][column] == "1":
                res += 1 + min(right, down, diagonal)
            
            cache[(row, column)] = res
            return res

        dfs(0, 0)
        return max(cache.values())**2


