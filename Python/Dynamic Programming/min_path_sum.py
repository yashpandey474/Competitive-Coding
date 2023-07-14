class Solution:

    def recMin(self, a, b, grid, map_cost):
        #BASE CASE
        if(map_cost[a][b] != -1):
            return map_cost[a][b]

        #EDGE CASES
        if(a == len(grid)-1):
            map_cost[a][b] = self.recMin(a, b+1, grid, map_cost) + grid[a][b]
            return map_cost[a][b]
        if(b == len(grid[0])-1):
            map_cost[a][b] = self.recMin(a+1, b, grid, map_cost) + grid[a][b]
            return map_cost[a][b]
        
        map_cost[a][b] = grid[a][b] + min(
            self.recMin(a+1, b, grid, map_cost),
            self.recMin(a, b+1, grid, map_cost)
            )

        return map_cost[a][b]

    def minPathSum(self, grid: List[List[int]]) -> int:
        #INITIALISE THE DP ARRAY
        map_cost = []
        a = len(grid)
        b = len(grid[0])
        for i in range(a):
            row = [-1]*b
            map_cost.append(row)

        #BASE CASE
        map_cost[a-1][b-1] = grid[a-1][b-1]
        return self.recMin( 0, 0, grid, map_cost)
