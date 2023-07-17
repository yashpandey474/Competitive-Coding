class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        #COUNT TOTAL ORANGES
        rows = len(grid)
        columns = len(grid[0])
        fresh_oranges = 0
        queue = []
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                if grid[i][j] == 2:
                    queue.append((i, j, 1))
        
        #FOR EACH ROTTEN ORANGE
        current_time = 0

        while fresh_oranges > 0 and queue:
            row, col, current_time = queue.pop(0)

            #CHECK ALL 4 NEIGHBOURS
            if row > 0 and grid[row-1][col] == 1:
                grid[row-1][col] = 2
                queue.append((row-1, col, current_time+1))
                fresh_oranges -= 1
            
            if row < rows - 1 and grid[row+1][col] == 1:
                grid[row+1][col] = 2
                queue.append((row+1, col, current_time+1))
                fresh_oranges -= 1
            
            if col > 0 and grid[row][col-1] == 1:
                grid[row][col-1] = 2
                queue.append((row, col-1, current_time+1))
                fresh_oranges -= 1
            
            if col < columns - 1 and grid[row][col+1] == 1:
                grid[row][col+1] = 2
                queue.append((row, col+1, current_time+1))
                fresh_oranges -= 1

        if fresh_oranges > 0:
            return -1
        return current_time
