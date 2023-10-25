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
    def connect(self, root: 'Node') -> 'Node':
        #LEVEL ORDER TRAVERSAL
        q = []
        q.append(root)
        current_level = 1
        if not root:
            return root

        while q:
            size = len(q)
            prev = None

            for i in range(size):
                current = q.pop(0)
                current.next = prev
                prev = current
                if current.right:
                    q.append(current.right)
                
                if current.left:
                    q.append(current.left)

        return root
