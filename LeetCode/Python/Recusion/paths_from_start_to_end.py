class Solution:
    
    def recursion(self, current_row, current_column, current_path,  m, n, dp, visited):
        if current_row >= n or current_column >= n or current_row < 0 or current_column < 0:
            return 0
        
        if current_row == n-1 and current_column == n-1:
            self.ans.append(current_path)
            return 1
        if visited[current_row][current_column]:
            return 0
        
        if dp[current_row][current_column] == 0:
            visited[current_row][current_column] = True
            dp[current_row][current_column] = (
            self.recursion(current_row, current_column + 1, current_path + "R", m, n, dp, visited) + 
            self.recursion(current_row, current_column - 1, current_path + "L", m, n, dp, visited) + 
            self.recursion(current_row + 1, current_column, current_path + "U", m, n, dp, visited) + 
            self.recursion(current_row - 1, current_column, current_path + "D", m, n, dp, visited))
            visited[current_row][current_column] = False
        
        return dp[current_row][current_column]
        
    def findPath(self, m, n):
        # code here
        dp = [[0 for _ in range(n)] for _ in range(n)]
        visited = [[False for _ in range(n)] for _ in range(n)]
        
        dp[n-1][n-1] = 1
        self.ans = []
        self.recursion(0, 0, "",  m, n, dp, visited)
        return self.ans
