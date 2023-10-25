class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        #MARK ALL REGIONS HAVING A BOUNDARY 1
        rows, columns = len(grid), len(grid[0])

        def dfs(row, column):
            if row < 0 or row >= rows or column < 0 or column >= columns or grid[row][column] != 1:
                return

            grid[row][column] = 2

            dfs(row + 1, column)
            dfs(row - 1, column)
            dfs(row, column + 1)
            dfs(row, column - 1)

            return

        for i in range(rows):
            for j in range(columns):
                #BOUNDARY ONE: MARK AS 2
                if grid[i][j] == 1 and i == 0 or i == rows-1 or j == 0 or j == columns - 1:
                    dfs(i, j) 

        #COUNT NUMBER OF ONES
        count = 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    count += 1

        return count


        
