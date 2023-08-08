import heapq
def findShortestDistance(n, edges, src, dst):
    # Write your code here.
    
    #CREATE THE GRAPH
    graph = {}
    for a, b, n, s in edges:
        if a not in graph:
            graph[a] = []

        if b not in graph:
            graph[b] = []

        #0 -> NORMAL EDGE
        #1 -> SPECIAL EDGE
        graph[a].append((b, n, 0))
        graph[a].append((b, s, 1))

    #0 -> SPECIAL EDGE NOT USED
    #1 -> SPECIAL EDGE USED
    queue = [(0, 0, src)]
    visited = set()

    while queue:
        dist, state, curr = heapq.heappop(queue)

        if curr == dst:
            return dist

        visited.add(curr)

        for v, w, ty in graph[curr]:
            if v not in visited:
                if ty == 1 and state == 1:
                    continue
                if ty == 1:
                    heapq.heappush(queue, (dist + w, 1, v))

                else:
                    heapq.heappush(queue, (dist + w, state, v))
         

    return -1
