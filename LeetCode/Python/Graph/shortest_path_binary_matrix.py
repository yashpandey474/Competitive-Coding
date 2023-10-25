from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        #GET DIMENSIONS
        rows, cols = len(grid), len(grid[0])

        
        queue = deque([(0, 0, 1)])

        if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
            return -1

        while queue:
            #0(1) WHERE POP(0) IS O(N)
            row, col, length = queue.popleft()

            if grid[row][col] == 1:
                continue

            if row == rows - 1 and col == cols - 1:
                return length

            #MARK AS VISITED: SAVE SPACE
            grid[row][col] = 1

            
            next_neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1),
            (row + 1, col + 1), (row - 1, col + 1), (row + 1, col - 1), (row - 1, col - 1)
            ]

            for r, c in next_neighbors:
                if r < 0 or r >= rows or c < 0 or c >= cols:
                    continue
                if grid[r][c] == 0:
                    queue.append((r, c, length + 1))

        return -1

                



            
            
