# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''
1. FOR EACH NODE
2. IF LEFT SUBTREE EXISTS
3. CHOOSE THE RIGHTMOST NODE OF THE LEFT SUBTREE
4. CONNECT IT TO THE RIGHT OF CURRENT
5. GO TO NEXT NODE ON RIGHT
'''
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        current = root

        while current:
            if (current.left):
                pred = current.left

                while (pred.right):
                    pred = pred.right

                pred.right = current.right
                current.right = current.left
                current.left = None
            
            current = current.right
        
