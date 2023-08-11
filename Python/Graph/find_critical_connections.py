class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        #CREATE THE GRAPH
        graph = {}

        for a, b in connections:
            if a not in graph:
                graph[a] = []

            if b not in graph:
                graph[b] = []

            graph[a].append(b)
            graph[b].append(a)

        #FIND THE CRITICAL CONNECTIONS
        #USE TARJAN'S ALGORITHM
        parents = [-1]*n
        disc = [-1]*n
        low = [-1]*n
        #CRITICAL EDGES
        result = []
        time = 0
        #START A DFS FROM 0
        def dfs(node):
            nonlocal time
            #MARK THE DISCOVERY TIME
            disc[node] = time

            #MARK LOW TIME
            low[node] = time

            #INCREMENT TIME
            time += 1

            #EXPLORE NEIGHBORS
            for v in graph[node]:
                #UNVISITED NODE
                if disc[v] == -1:
                    parents[v] = node
                    dfs(v)
                    low[node] = min(low[node], low[v])

                    #CRITICAL CONNECTION
                    if low[v] > disc[node]:
                        result.append([node, v])


                #BACK EDGE
                elif v != parents[node]:
                    low[node] = min(low[node], low[v])

        dfs(0)

        return result
