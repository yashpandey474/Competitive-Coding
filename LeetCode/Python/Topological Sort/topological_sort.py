class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        result = []
        #CALCULATE INDEGREES
        indegrees = [0]*V
        for i in adj:
            for j in i:
                indegrees[j]+=1
                
        #ADD ALL EITH 0 INDEGREE TO QUEUE
        queue = []
        for i in range(V):
            if indegrees[i] == 0:
                queue.append(i)
                
        while queue:
            current = queue.pop(0)
            result.append(current)
            #REDUCE INDEGREES OF NEIGHBOURS
            for i in adj[current]:
                indegrees[i]-=1
                #ADD TO QUEUE IF 0
                if indegrees[i] == 0:
                    queue.append(i)

        return result
        

