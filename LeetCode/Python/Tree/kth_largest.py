#User function Template for python3

# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

# return the Kth largest element in the given BST rooted at 'root'
class Solution:
    def kthLargest(self,root, k):
        #your code here
        
        stack = []
        current = root
        
        while current is not None or stack:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            if k == 1:
                
