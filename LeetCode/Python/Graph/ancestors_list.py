class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        graph = {i: [] for i in range(n)}

        for a, b in edges:
            graph[a].append(b)

        ancestors = [set() for i in range(n)]
        
        print(graph)
        def dfs(node, start, visited):
            visited.add(node)
            if node != start:
                ancestors[node].add(start)

            for v in graph[node]:
                if v not in visited:
                    dfs(v, start, visited)



        #DFS ON EVERY NODE
        for i in range(n):
            dfs(i, i, set())


        return [sorted(a) for a in ancestors]
