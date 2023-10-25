# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #CHECK IF ROOT IS THE LCA
        if (root == p or root == q or root is None):
            return root
        
        #CHECK IN LEFT SUBTREE
        leftLCA = self.lowestCommonAncestor(root.left, p, q)
        #CHECK IN RIGHT SUBTREE
        rightLCA = self.lowestCommonAncestor(root.right, p, q)

        #RETURN THE NON NULL ONE
        if leftLCA is None:
            return rightLCA
        
        if rightLCA is None:
            return leftLCA
        
        return root
