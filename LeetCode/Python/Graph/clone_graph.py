"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def dfs(self, node, copy, visited):
        visited[node] = copy

        for neighbor in node.neighbors:
            if neighbor not in visited:
                newNode = Node(neighbor.val)
                copy.neighbors.append(newNode)
                self.dfs(neighbor, newNode, visited)
            else:
                copy.neighbors.append(visited[neighbor])
            
    
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node is None:
            return node

        copy = Node(node.val)
        visited = {}
        self.dfs(node, copy, visited)
        return copy

        
        
        
        
