class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        #RUN A DFS STARTING AT EVERY NODE

        #TRACK THE VISITED NODES AND THE FREQUENCY OF EACH COLOR NODE


        #CREATE THE ADJACENCY LIST
        adj = defaultdict(list)

        for a, b in edges:
            adj[a].append(b)


        #DEPTH FIRST SEARCH
        visited = set()
        #DETECT CYCLES [RETURN -1]
        path = set()
        count = [[0] * 26 for i in range(len(colors))] #MAP COUNT[NODE][COLOR] -> MAXIMUM FREQUENCY

        def dfs(node: int) -> int: #RETURN MAX FREQ
            if node in path:
                return float('inf')

            if node in visited:
                return 0

            visited.add(node)
            path.add(node)
            
            #ITS OWN COLOR
            color = ord(colors[node]) - ord('a')
            count[node][color] = 1

            #GO THROUGH NEIGHBORS
            for v in adj[node]:
                #POPULATE THE COUNT ARRAY
                if dfs(v) == float('inf'):
                    return float('inf')
                #ITERATE THROUGH COLOUMNS
                for c in range(26):
                    if c == color:
                        count[node][c] = max(count[node][c], 1 + count[v][c])

                    else:
                        count[node][c] = max(count[node][c], count[v][c])

            

            path.remove(node)

            return max(count[node])

        res = 0
        for i in range(len(colors)):
            res = max(dfs(i), res)

        return (-1 if res == float('inf') else res)
