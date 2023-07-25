class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        #GET NEIIGHBORS
        neighbors = defaultdict(list)
        edges_set = { (a, b) for a, b in connections}
        visited = set()
        changes = 0

        for u, v in connections:
            #ADD TO NEIGHBORS
            neighbors[u].append(v)
            neighbors[v].append(u)

        #START FROM GOAL AND RECURSIVELY CHECK IF NEIGHBORS CAN REACH IT
        def dfs(city):
            nonlocal changes
            visited.add(city)
            for neighbor in neighbors[city]:
                #ALREADY VISITED
                if neighbor in visited:
                    continue

                #CHECK IF IT CAN REACH CITY
                if (neighbor, city) not in edges_set:
                    changes+=1
                
                #CHECK IF NEIGHBOR'S NEIGHBORS CAN REACH IT
                dfs(neighbor)

        
        dfs(0)
        return changes
