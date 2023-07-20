"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        #PERFORM LEVEL ORDER TRAVERSAL

        #QUEUE FOR LEVEL ORDER TRAVERSAL
        queue = []

        if root is None:
            return root

        #PUSH ROOT
        queue.append(root)

        while queue:
            #POP ALL THE NODES AT CURRENT LEVEL
            size = len(queue)
            pred = None
            for i in range(size):
                #POP FROM QUEUE
                current = queue.pop(0)
                #POPULATE NEXT
                current.next = pred
                #UPDATE PREVIOUS
                pred = current

                #ADD MORE NODES
                if current.right:
                    queue.append(current.right)
                if current.left:
                    queue.append(current.left)



        return root
