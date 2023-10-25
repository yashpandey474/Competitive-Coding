# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root):
        if root is None:
            return 0
        
        return 1 + max(self.height(root.left), self.height(root.right))
    def recursion(self, root):
        if root is None:
            return
        
        curr_dia = self.height(root.left) + self.height(root.right)
        self.diameter = max(self.diameter, curr_dia)

        if root.left:
            self.recursion(root.left)
        if root.right:
            self.recursion(root.right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #UNTIL SUM OF HEIGHTS OF LEFT AND RIGHT IS NOT MAXIMAL
        self.diameter = 0
        self.recursion(root)
        return self.diameter
