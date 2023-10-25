class Solution:
    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        #CONVERT THE GRAPH TO A TREE BY REMOVING ONE EDGE

        #USE UNION FIND
        parent = [i for i in range(len(edges)+1)]
        rank = [1]*(len(parent)+1)

        def find(n):
            p = parent[n]

            while p != parent[p]:
                #PATH COMPRESSION
                parent[p] = parent[parent[p]]
                p = parent[p]

            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

            return True

        #GO THROUGH ALL THE EDGES
        for edge in edges:
            u, v = edge[0], edge[1]
            #SEE IF ALREADY SAME PARENT
            if not union(u, v):
                return edge
        return []
