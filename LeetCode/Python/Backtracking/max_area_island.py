class Solution:

    

        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        #VARIABLE FOR MAXMIMUM LENGTH
        self.max_len = 0

        #ITERATE THROUGH ALL ONES
        rows = len(grid)
        columns = len(grid[0])

        

        def dfs(row, column):
            #CHECK FOR OUT OF BOUNDS
            if row < 0 or column < 0 or row >= rows or column >= columns or grid[row][column] != 1:
                return 0
            
            #SET THE ONES TO 2S
            grid[row][column] = 2

            return (
                1 + dfs(row+1, column) +
                dfs(row-1, column)+
                dfs(row, column + 1)+
                dfs(row, column - 1)
            )

        area = 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    area = max(area,dfs(i, j))

        return area
        
