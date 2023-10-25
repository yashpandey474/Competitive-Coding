class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        perimeter = 0
        #CREATE CACHE
        cache = {}

        def dfs(row, column):
            nonlocal perimeter
            if row < 0 or row >= rows or column < 0 or column >= columns or grid[row][column] == 0:
                perimeter += 1
                return

            if grid[row][column] == 2:
                return

            #ADD TO VISITED
            grid[row][column] = 2

            #TRAVERSE NEIGHBORS
            dfs(row + 1, column)
            dfs(row - 1, column)
            dfs(row, column + 1)
            dfs(row, column - 1)
            

            

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    dfs(i, j)
                    break

        return perimeter
