'''
GRAPH M-COLORING PROBLEM
'''
class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:

        #COLORING OF GRAPH
        graph = {i: [] for i in range(n + 1)}
        #CREATE THE GRAPH
        for a, b in paths:
            graph[a].append(b)
            graph[b].append(a)

        #COLORS
        colors = [0]*(n)

        #FIND IF NODE CAN BE COLORED WITH A PARTICULAR COLOR
        def canColor(node, color):
            for v in graph[node]:
                if colors[v - 1] == color:
                    return False

            return True

        #BFS FUNCTION
        def bfs(node):
            if node == n + 1:
                return True

            for i in range(1, 5):
                colors[node - 1] = i
                if canColor(node, i) and bfs(node + 1):
                    return True
                colors[node - 1] = 0

            return False
                    

        #TRY TO COLOR ALL NODES
        bfs(1)
        
        #RETURN FINAL COLORS
        return colors

        
