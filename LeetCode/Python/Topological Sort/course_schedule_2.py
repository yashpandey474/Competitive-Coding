class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        indegrees = [0]*numCourses

        for i in range(numCourses):
            graph[i] = []
        #CREATE THE GRAPH
        for i in prerequisites:
            graph[i[1]].append(i[0])

        for i in range(numCourses):
            for j in graph[i]:
                indegrees[j]+=1
        print(graph)
        print("INDEGREES = ", indegrees)
        #QUEUE FOR TOPOLOGICAL SORTING
        queue = []
        #RESULT FOR SORTING
        result = []

        #ADD ALL WITH 0 INDEGREE
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)


        while queue:
            current = queue.pop(0)
            result.append(current)
            for i in graph[current]:
                indegrees[i] -= 1
                if indegrees[i] == 0:
                    queue.append(i)

        #IF INDEGREE NOT 0
        for i in range(numCourses):
            if indegrees[i] != 0:
                return []

        return result

