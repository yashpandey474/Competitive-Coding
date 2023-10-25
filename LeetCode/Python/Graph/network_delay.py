class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = {}

        for u, v, w in times:
            if u not in graph:
                graph[u] = []

            graph[u].append((v, w))

        distances = [float('inf')]*(n + 1)
        distances[k] = 0

        pq = [(0, k)]
        visited = set()

        while pq:
            time, node = heapq.heappop(pq)
            if node in visited:
                continue
            distances[node] = time
            visited.add(node)

            if node in graph:
                for v, w in graph[node]:
                    if v not in visited:
                        heapq.heappush(pq, (time + w, v))

        res = max(distances[1:])
        # print(distances)
        if res == float('inf'):
            return -1
        return res



