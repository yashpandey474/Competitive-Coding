class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        

        parents1 = [i for i in range(n + 1)]
        parents2 = [i for i in range(n + 1)]

        comp1 = n
        comp2 = n
        rank1 = [1 for i in range(n + 1)]
        rank2 = [1 for i in range(n + 1)]


        def union(x1, x2, parents, rank):
            p1, p2 = find(x1, parents), find(x2, parents)

            if p1 == p2:
                return False

            if rank[p1] >= rank[p2]:
                parents[p2] = p1
                rank[p1] += rank[p2]

            else:
                parents[p1] = p2
                rank[p2] += rank[p1]

            return True

        def find(x1, parents):
            while x1 != parents[x1]:
                parents[x1] = parents[parents[x1]]
                x1 = parents[x1]

            return x1

        #ADD THE TYPE3 EDGES TO UNION FIND DATA STRUCTURS
        count = 0
        for ty, a, b in edges:
            if ty == 3:
                if union(a, b, parents1, rank1):
                    if union(a, b, parents2, rank2):
                        comp2 -= 1
                    count += 1
                    comp1 -= 1

                elif union(a, b, parents1, rank1):
                    comp2 -= 1
                    count += 1

                
        
        #ADD OTHER EDGES
        for ty, a, b in edges:
            if ty == 1:
                if union(a, b, parents1, rank1):
                    count += 1
                    comp1 -= 1

            elif ty == 2:
                if union(a, b, parents2, rank2):
                    count += 1
                    comp2 -= 1

        #BOTH GRAPHS ARE CONNECTED
        if comp1 == 1 and comp2 == 1:
            return len(edges) - count
        return -1
                
