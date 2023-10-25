# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def findInorder(self, root):
        if root is None:
            return
        self.findInorder(root.left)
        self.inorder.append(root.val)
        self.findInorder(root.right)
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.inorder =[]
        self.findInorder(root)

        i = 0
        j = len(self.inorder)-1

        while i < j:
            if self.inorder[i] + self.inorder[j] == k:
                return True
            if self.inorder[i] + self.inorder[j] > k:
                j-=1
            else:
                i+=1
        return False
