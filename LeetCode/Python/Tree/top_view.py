class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        # code here
        
        #STORE NODES FOR LEVEL ORDER
        queue = []
        #STORE LINES VISITED
        map_lines = {}
        #RESULT
        result = []
        
        queue.append((root,0))

        while queue:
            current, line = queue.pop(0)
            #FIRST NODE ON LINE
            if line not in map_lines:
                map_lines[line] = current
            
            if current.left:
                queue.append((root.left, line-1))
            
            if current.right:
                queue.append((root.right, line+1))
            
        l = (sorted(map_lines.items()))
        for line, node in l:
            result.append(node.data)
        return result
