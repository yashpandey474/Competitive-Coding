class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        #ISLANDS SURROUNDED BY WATER

        #MARK ALL REGIONS CONNETED TO BODER
        rows, columns = len(grid), len(grid[0])

        def dfs(row, column):
            if row < 0 or row >= rows or column < 0 or column >= columns or grid[row][column] != 0:
                return

            grid[row][column] = 2

            dfs(row + 1, column)
            dfs(row - 1, column)
            dfs(row, column + 1)
            dfs(row, column - 1)

            return
        #MARK THE UNSURROUNDED REGIONS  
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 0 and (i == 0 or i == rows-1 or j == 0 or j == columns -  1):
                    dfs(i, j)

        #COUNT SURROUNDED REGIONS
        count = 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 0:
                    count += 1
                    dfs(i, j)

        return count
