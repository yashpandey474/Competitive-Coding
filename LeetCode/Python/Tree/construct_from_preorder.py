# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recursion(self, preorder):
        if len(preorder) == 0:
            return None
        
        root = TreeNode(val = preorder[0])
        i = 1
        while i < len(preorder):
            if preorder[i]>root.val:
                break
            i+=1
        
        root.left = self.recursion(preorder[1:i])
        root.right = self.recursion(preorder[i:])
        return root

    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        return self.recursion(preorder)
