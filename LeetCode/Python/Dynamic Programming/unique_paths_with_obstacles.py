class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #INITIALISE THE CONSTANTS
        rows, columns = len(obstacleGrid), len(obstacleGrid[0])
        #INITIALISE DP ARRAY
        dp = [[-1 for _ in range(columns)] for _ in range(rows)]

        #DP[I][J] = NUMBER OF UNIQUE PATHS TO M-1N-1
        #BASE CASE
        dp[rows-1][columns-1] = 1

        def dfs(row, column):
            if row<0 or column < 0 or row >= rows or column >= columns or obstacleGrid[row][column] == 1:
                return 0
            
            if dp[row][column] != -1:
                return dp[row][column]

            else:
                dp[row][column] = 0
                dp[row][column] += dfs(row, column+1)
                dp[row][column] += dfs(row+1, column)
                return dp[row][column]

        #INITIAL POSITION IS 0, 0
        return dfs(0, 0)
        
