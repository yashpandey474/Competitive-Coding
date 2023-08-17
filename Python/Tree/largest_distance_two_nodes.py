from os import *
from sys import *
from collections import *
from math import *

def largestDistance(n, edges):
    #CREATE THE GRAPH
    graph = {}

    for a, b in edges:
        if a not in graph:
            graph[a] = []

        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    
    #DIAMETER OF TREE

    #PERFORM A BFS FROM ANY NODE
    def bfs(node):
        queue = [(node, 0)]
        visited = set()
        max_dist = 0
        max_dist_node = node

        while queue:
            curr, dist = queue.pop(0)
            if dist > max_dist:
                max_dist_node = curr
                max_dist = dist

            visited.add(curr)

            for v in graph[curr]:
                if v not in visited:
                    queue.append((v, dist + 1))

        return max_dist, max_dist_node

    #PERFORM A BFS FROM FARTHEST NODE
    _, farthest_1 = bfs(0)
    dist,_ = bfs(farthest_1)

    return dist

            


        
