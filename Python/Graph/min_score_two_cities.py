class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        #CREATE THE GRAPH
        graph = defaultdict(list)
        for a, b, dist in roads:
            graph[a].append((b, dist))
            graph[b].append((a, dist))

        road_length = float('inf')
        visited = set()

        #DEPTH FIRST SEARCH TO FIND MINIMUM ROAD LENGTH
        def dfs(start):
            nonlocal road_length
            if start in visited:
                return
            visited.add(start)
            
            for v, dist in graph[start]:
                road_length = min(road_length, dist)
                dfs(v)
            return
        dfs(1)
        return road_length

            
