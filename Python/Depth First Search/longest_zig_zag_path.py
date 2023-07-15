# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def __init__(self):
        self.max_len = 0

    def dfs(self, root, current_len, right):
        if root is None:
            return
        
        self.max_len = max(self.max_len, current_len)

        if right:
            leftLen = current_len+1
            rightLen = 1
        elif right == False:
            leftLen = 1
            rightLen = current_len + 1

        self.dfs(root.left, leftLen, False)
        self.dfs(root.right, rightLen, True)

    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
    
        self.dfs(root, 0, True)
        self.dfs(root, 0, False)

        return self.max_len

        
