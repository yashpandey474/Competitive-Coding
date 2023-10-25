class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        #CONVERT TO A GRAPH
        graph = {i: [] for i in range(n)}

        for a, b in edges:

            graph[a].append(b)
            graph[b].append(a)

        #FIND THE APPLES
        def dfs(current, parent):
            time = 0

            for child in graph[current]:
                if child != parent:
                    childTime = dfs(child, current)
                    if childTime > 0 or hasApple[child]:
                        time += 2 + childTime
            
            return time

        return dfs( 0, -1 )

            
