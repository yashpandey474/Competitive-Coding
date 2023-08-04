class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        #CREATE THE GRAPH
        graph = defaultdict(list)
        for i in range(len(edges)):
            edge = edges[i]
            graph[edge[0]].append([edge[1], succProb[i]])
            graph[edge[1]].append([edge[0], succProb[i]])

        #DJISKTRA'S ALGOROITHM
        pq = [(-1, start_node)]
        visited = set()

        while pq:
            prob, current = heapq.heappop(pq)
            visited.add(current)
            if current == end_node:
                return -prob

            for vertex, probability in graph[current]:
                if vertex not in visited:
                    heapq.heappush(pq,
                        (prob*(probability),
                        vertex
                        )
                        )
        return 0
