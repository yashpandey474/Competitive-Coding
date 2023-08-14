class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        #RETURN IF BIPARTITION IS POSSIBLE

        #CREATE GRAPH
        graph = {i: [] for i in range(n + 1)}

        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)


        #RUN BFS CHECKING IF BIPARTITION IS POSSIBLE
        colors = [0]*(n + 1)


        def bfs(node):
            #CREATE QUEUE
            queue = deque([node])

            #ASSIGN A COLOR TO NODE
            colors[node] = 1

            while queue:
                #POP AN ELEMENT
                curr = queue.popleft()

                #CHECK ON NEIGHBORS
                for i in graph[curr]:
                    if colors[i] == 0:
                        colors[i] = -colors[curr]
                        queue.append(i)
                    
                    elif colors[i] == colors[curr]:
                        return False

            #BIPARTITION POSSIBLE
            return True

        for i in range(1, n + 1):
            if colors[i] == 0:
                if not bfs(i):
                    return False

        return True

