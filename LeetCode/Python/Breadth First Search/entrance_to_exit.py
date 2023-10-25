class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        queue = []
        visited = set()
        rows = len(maze)
        columns = len(maze[0])

        queue.append(((entrance[0], entrance[1]), 0))

        while queue:
            current, steps = queue.pop(0)
            if current in visited:
                continue
            visited.add(current)
            #REACHED AN EXIT
            if (steps != 0) and ((current[0] == 0 or current[0] == rows-1) or (current[1] == 0 or current[1] == columns-1)):

                return steps

            #HAVENT REACHED AN EXIT
            else:
                #MOVE UP
                if current[0] != 0 and maze[current[0]-1][current[1]] != '+':
                    queue.append(((current[0]-1, current[1]), steps+1))
                    
                #MOVE DOWN
                if current[0] != rows-1 and maze[current[0]+1][current[1]] != '+':
                    queue.append(((current[0]+1, current[1]), steps+1))
                
                #MOVE LEFT
                if current[1] != 0 and maze[current[0]][current[1]-1] != '+':
                    queue.append(((current[0], current[1]-1), steps+1))
                
                #MOVE RIGHT
                if current[1] != columns-1 and maze[current[0]][current[1]+1] != '+':
                    queue.append(((current[0], current[1]+1), steps+1))

        return -1
