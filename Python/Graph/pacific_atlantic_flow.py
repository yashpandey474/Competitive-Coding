class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, columns = len(heights), len(heights[0])

        map_pacific = set()
        map_atlantic = set()

        #GO TO EVERY CELL BORDERING PACIFIC OCEAN 

        def dfs(row, col, visited, previous, map1):

            #OUT OF BOUNDS OR LESS
            if row < 0 or col < 0 or row >= rows or col >= columns or (row, col) in visited or (row, col) in map1 or heights[row][col] < previous:
                return

            #ADD TO MAP
            map1.add((row, col))
            visited.add((row, col))

            #ITERATE ON NEIGHBORS
            dfs(row + 1, col, visited, heights[row][col], map1)
            dfs(row - 1, col, visited, heights[row][col], map1)
            dfs(row, col + 1, visited, heights[row][col], map1)
            dfs(row, col - 1, visited, heights[row][col], map1)


            
        for i in range(rows):
            for j in range(columns):
                if i == 0 or j == 0:
                    dfs(i, j, set(), -float('inf'), map_pacific)

                if i == rows - 1 or j == columns - 1:
                    dfs(i, j, set(), -float('inf'), map_atlantic)
        result = []
        for i in range(rows):
            for j in range(columns):
                if (i, j) in map_pacific and (i, j) in map_atlantic:
                    result.append([i, j])

        return result

                
