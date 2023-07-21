# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sameTree(self, root1, root2):
        if root1 is None and root2 is None:
            return True

        if root1 is not None and root2 is None:
            return False

        if root1 is None and root2 is not None:
            return False

        

        if root1.val != root2.val:
            return False

        return self.sameTree(root1.left, root2.left) and self.sameTree(root1.right, root2.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        
        if subRoot is None:
            return True

        if root is None:
            return False
        
        if root.val == subRoot.val and self.sameTree(root, subRoot):
            print("FOUND MATCHING VALUE")
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
