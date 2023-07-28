class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        

        #EMPLOYEES: 0 TO N-1
        graph = {}

        for i in range(0, n):
                #FROM MANAGER I TO I: EDGE
            if manager[i] not in graph:
                graph[manager[i]] = []
            graph[manager[i]].append(i)

        
        #LEVEL ORDER TRAVERSAL
        queue = []
        queue.append((headID,  0))
        time = 0
        print("GRAPH = ", graph)
        while queue:
            #POP FROM THE QUEUE
            curr, ti = queue.pop(0)
            time = max(time,ti)

            print("CURR = ", curr)

            #CHECK THE CHILDREN
            if curr not in graph:
                continue
            
            for j in graph[curr]:
                queue.append((j, ti + informTime[curr]))
        return time
