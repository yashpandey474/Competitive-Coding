class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        #GRAPH OF DIRECTED EDGES
        graph = defaultdict(list)
        for i in range(len(equations)):
            a, b = equations[i]
            val = values[i]

            graph[a].append((b, 1/val))
            graph[b].append((a, val))

        answers = []

        def bfs(start, target):
            visited = set()
            queue = []

            queue.append((start, 1))
            while queue:
                current, dist = queue.pop(0)
                if current == target:
                    return dist

                visited.add(current)

                for i, d in graph[current]:
                    if i not in visited:
                        queue.append((i, d*dist))

            return -1
        

        #EVALUATE EACH QUERY   
        for a, b in queries:
            #DOES NOT EXIST
            if a not in graph or b not in graph:
                answers.append(-1)

            else:
                answers.append(bfs(b, a))   
        return answers
