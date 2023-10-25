class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegrees = [0]*n
        result = []
        for i in edges:
            indegrees[i[1]] +=1

        for i in range(n):
            if indegrees[i] == 0:
                result.append(i)
        
        return result
