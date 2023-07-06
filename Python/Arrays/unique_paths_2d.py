class Solution:

    def recPaths(self, m, n, map_path):
        if(m<=1 or n<=1 ):
            return 1

        if(map_path[m-1][n-1] != -1):
            return map_path[m-1][n-1]

        map_path[m-1][n-1] = self.recPaths(m-1, n, map_path) + self.recPaths(m, n-1, map_path)
        return map_path[m-1][n-1]

    def uniquePaths(self, m: int, n: int) -> int:
        #INITIALISE 2D ARRAY
        map_path = []
        for i in range (m):
            row = [-1] * n
            map_path.append(row)
        
        return self.recPaths(m, n, map_path)
