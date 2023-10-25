# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMin(self, root):
        while root.left is not None:
            root = root.left
        
        return root
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root is None:
            return None

        if key<root.val:
            root.left = self.deleteNode(root.left, key)
        
        elif key>root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            #FOUND NODE WITH KEY
            if root.left is None:
                return root.right

            if root.right is None:
                return root.left
            
            minNode = self.findMin(root.right)
            #EXCHANGE WITH SUCCESSOR
            root.val = minNode.val
            #DELETE THE SUCCESSOR NODE
            root.right = self.deleteNode(root.right, minNode.val)
        
        return root


            
        return root
