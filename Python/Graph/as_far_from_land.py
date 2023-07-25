class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        queue = []
        #ADD ALL ONES TO THE QUEUE
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    queue.append((i, j, 0))

        #BFS
        maxDist = -1
        visited = set()
        while queue:
            row, column, dist = queue.pop(0)

            #OUT OF BOUNDS
            if row < 0 or row >= rows or column < 0 or column >= columns or (row, column) in visited:
                continue

            #WATER CELL
            if grid[row][column] == 0:
                maxDist = max(maxDist, dist)
            
            #ADD TO VISITED
            visited.add((row, column))

            queue.append((row + 1, column, dist + 1))
            queue.append((row - 1, column, dist + 1))
            queue.append((row, column + 1, dist + 1))
            queue.append((row, column - 1, dist + 1))

        return maxDist

                
