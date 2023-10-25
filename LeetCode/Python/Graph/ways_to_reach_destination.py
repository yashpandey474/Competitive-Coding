class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:

        #CREATE THE GRAPH
        graph = {i: [] for i in range(n)}

        for a, b, t in roads:
            graph[a].append((b, t))
            graph[b].append((a, t))

        #DJISKTA'S ALGORITHM

        #PQ TO HOLD VERTICES AND TIME
        pq = [(0, 0)]

        #STORE DISTANCES
        distances = [float('inf') for i in range(n)]

        #STORE WAYS TO REACH WITH LOWEST DISTANCE
        ways = [0 for i in range(n)]

        #FOR START NODE
        distances[0] = 0
        ways[0] = 1


        #ITERATE
        while pq:
            time, curr = heapq.heappop(pq)

            #IF GREATER
            if time > distances[curr]:
                continue


            for neigh, t in graph[curr]:
                newTime = time + t

                if newTime < distances[neigh]:
                    #UPDATE DISTANCE AND WAYS
                    distances[neigh] = newTime
                    ways[neigh] = ways[curr]

                    #ADD TO QUEUE
                    heapq.heappush(pq, (newTime, neigh))

                elif newTime == distances[neigh]:
                    ways[neigh] = (ways[neigh] + ways[curr]) % (10**9 + 7)

        return ways[n - 1]
