class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #CREATE A MINIMUM SPANNING TREE
        n = len(points)

        def manHattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        #ADJACENCY LIST
        adj = {i: [] for i in range(n)}
        for i in range(n):
            for j in range(i + 1, n):
                dist = manHattan(points[i], points[j])
                adj[i].append([dist, j])
                adj[j].append([dist, i])

         #PRIM'S ALGORITHM
        res = 0
        visited = set()
        pq = [[0, 0]] #COST, POINT INDEX


        while len(visited) < n:
            weight, point = heapq.heappop(pq)
            if point in visited:
                continue
            res += weight
            visited.add(point)

            for cost, neighbor in adj[point]:
                if neighbor not in visited:
                    heapq.heappush(pq, [cost, neighbor])

        return res


