class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        n = len(graph)
        visited = set()
        def backtrack(current, path):
            #REACHED TARGET NODE
            if current == n-1:
                result.append(path + [current])
                return

            #VISITED
            visited.add(current)
            for i in graph[current]:
                if i not in visited:
                    backtrack(i, path + [current])

            #REMOVE FROM VISITED
            visited.remove(current)

            return

        backtrack(0, [])
        return result


             
