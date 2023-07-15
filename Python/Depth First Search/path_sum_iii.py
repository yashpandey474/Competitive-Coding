# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.res = 0

    def dfs(self, root, targetSum):
        if root is None:
            return
        
        if root.val == targetSum:
            self.res += 1

        self.dfs(root.left, targetSum-root.val)
        self.dfs(root.right, targetSum - root.val)
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        
        if root is None:
            return 0
        
        self.dfs(root, targetSum)
        self.pathSum(root.left, targetSum)
        self.pathSum(root.right, targetSum)

        return self.res


        
