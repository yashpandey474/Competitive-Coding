from os import *
from sys import *
from collections import *
from math import *
import heapq

def dijkstra(vec, vertices, edges, source):
    # Write your code here.
    #ARRAY TO STORE SHORTEST DISTANCES
    distances = [2147483647 for _ in range(vertices)]

    #SET DISTANCE FROM START
    distances[source] = 0

    #CREATE GRAPH
    graph = {}
    for a, b, w in vec:
        if a not in graph:
            graph[a] = []

        if b not in graph:
            graph[b] = []

        graph[a].append((b, w))
        graph[b].append((a, w))

    #PRIORITY QUEUE TO STORE EDGES
    pq = []
    pq.append((0, source))

    while pq:
        dist, curr = heapq.heappop(pq)

        #IF LONGER PATH: DON'T CONSIDER
        if dist > distances[curr] or curr not in graph:
            continue

        #SHORTER DISTANCE: CONSIDER NEIGHBORS
        for a, w in graph[curr]:
            if w + dist < distances[a]:
                distances[a] = w + dist
                heapq.heappush(pq, (w + dist, a))

    return distances
