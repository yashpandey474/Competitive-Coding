#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        self.result = []
        stack = []
        result = []
        visited = set()
        stack.append(0)
        
        while stack:
            current = stack.pop()
            result.append(current)
            visited.add(current)
            
            for i in range(len(adj[current])-1, -1, -1):
                if adj[current][i] not in visited:
                    stack.append(adj[current][i])
                    
        return result
            
