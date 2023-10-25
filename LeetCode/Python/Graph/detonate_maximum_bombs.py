class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        #build a graph
        #directed edges: from bomb to bombs it can detonate (distance<=radius)

        adj = defaultdict(list) #bomb -> list of bombs it can detonate
        for i in range(len(bombs)):
            for j in range( i +1, len(bombs)):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]

                d = sqrt((x1 - x2)**2 + (y1 - y2)**2)

                #ADD EDGES
                if d <= r1:
                    adj[i].append(j)

                if d <= r2:
                    adj[j].append(i)



        #DFS: NUMBER OF BOMBS THAT CAN BE DETONATED
        # visited = set()
        def dfs(start, visited):
            if start in visited:
                return 0

            visited.add(start)
            if start in adj:
                for v in adj[start]:
                    dfs(v, visited)
            return len(visited)

        #RUN DFS FOR EVERY BOMB
        res = 0
        for i in range(len(bombs)):
            res = max(res, dfs(i, set()))

        return res
            
            
