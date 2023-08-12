from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)
import heapq


# Wormhole class
class Wormhole:

    def __init__(self, startX, startY, endX, endY, weight) :

        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY
        self.weight = weight


def minTimeInWormholeNetwork(n, sx, sy, dx, dy, wormhole) :

	# Your code goes here
    def calculateTime(start, end):
        return abs(start[0] - end[0]) + abs(start[1] - end[1])

    #CREATE GRAPH
    points = set()

    for i in wormhole:
        points.add((i.startX, i.startY))
        points.add((i.endX, i.endY))

    points.add((sx, sy))
    points.add((dx, dy))
    
    graph = {i: [] for i in points}
    for i in wormhole:
        st = (i.startX, i.startY)
        en = (i.endX, i.endY)
        graph[st].append((en, i.weight))
        graph[en].append((st, i.weight))
    
    for i in points:
        for j in points:
            if i != j:
                time = calculateTime(i, j)
                graph[i].append((j, time))
                graph[j].append((i, time))

    #DJISKTRA'S SHORTEST PATH ALGORITHM
    distances = {i: float('inf') for i in points}
    start = (sx, sy)
    end = (dx, dy)
    distances[start] = 0

    pq = [(0, start)]

    while pq:
        dist, curr = heapq.heappop(pq)
        #ALREADY SHORTER PATH FOUND
        if dist > distances[curr]:
            continue

        for neighbor, weight in graph[curr]:
            #LESS THAN CURRENT
            if distances[curr] + weight < distances[neighbor]:
                heapq.heappush(pq, (distances[curr] + weight, neighbor))
                distances[neighbor] = distances[curr] + weight

    return distances[end]
    

    

































#taking inpit using fast I/O
def takeInput() :

    sr_ds = stdin.readline().strip().split(" ")
    sx = int(sr_ds[0].strip())
    sy = int(sr_ds[1].strip())
    dx = int(sr_ds[2].strip())
    dy = int(sr_ds[3].strip())

    n = int(input())

    wormhole = []

    for i in range(n) :

        arr = list(map(int, stdin.readline().strip().split(" ")))
        wormhole.append(Wormhole(arr[0], arr[1], arr[2], arr[3], arr[4]))

    return wormhole, n, sx, sy, dx, dy


#main
wormhole, n, sx, sy, dx, dy = takeInput()
print(minTimeInWormholeNetwork(n, sx, sy, dx, dy, wormhole))
