class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parents = [i for i in range(n + 1)]
        rank = [1 for i in range(n + 1)]
        
        def find(x1):
            while parents[x1] != x1:
                parents[x1] = parents[parents[x1]]
                x1 = parents[x1]
            return x1
        
        def union(x1, x2):
            p1, p2 = find(x1), find(x2)
            
            if p1 == p2:
                return False
            
            if rank[p1] >= rank[p2]:
                parents[p2] = p1
                rank[p1] += rank[p2]
                
            else:
                parents[p1] = p2
                rank[p2] += rank[p1]
                
            return True
        
        components = n
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    if union(i, j):
                        components -= 1
                        
        return components
