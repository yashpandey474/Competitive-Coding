class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:

        #CREATE A GRAPH
        graph = {}
        for a, b in richer:
            if a not in graph:
                graph[a] = []

            if b not in graph:
                graph[b] = []

            #B HAS LESS MONEY THAN A
            graph[b].append(a)

        #RESULT ARRAY
        result = [-1]*len(quiet)

        #DFS FUNCTION
        def dfs(node):
            #IF VALUE ALREADY ASSIGNED
            if result[node] >= 0:
                return result[node]

            #ASSIGN AS OWN VALUE [EQUAL VALUE]
            result[node] = node

            #FOR EVERY NODE WITH MORE MONEY
            if node in graph:
                for j in graph[node]:
                    #IF MORE QUIET
                    if quiet[result[node]] > quiet[dfs(j)]:
                        #UPDATE RESULT VALUE
                        result[node] = result[j]

            #RETURN RESULT VALUE
            return result[node] 

        for i in range(len(quiet)):
            dfs(i)

        return result
