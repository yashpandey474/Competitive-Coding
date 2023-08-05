from os import *
from sys import *
from collections import *
from math import *

def wallsAndGates(a, n, m): 
    # Write your Code here.

    
    # inf = 214783647

    #QUEUE FOR BFS
    queue = []
    visited = set()
    #RUN A DFS FOR EACH ROOM
    for i in range(n):
        for j in range(m):
            if a[i][j] == 0:
                queue.append((i, j, 0))

    while queue:
        row, col, dist = queue.pop(0)
        if row < 0 or row >= n or col < 0 or col >= m:
            continue
        if a[row][col] == -1:
            continue

        if (row, col) in visited:
            continue

        # if a[row][col] == 2147483647:
        a[row][col] = min(a[row][col], dist)
        visited.add((row, col))

        queue.append((row + 1, col, dist + 1))
        queue.append((row - 1, col, dist + 1))
        queue.append((row, col + 1, dist + 1))
        queue.append((row, col - 1, dist + 1))
    

    return a

