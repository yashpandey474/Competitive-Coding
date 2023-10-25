# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return [0, 0]
            leftPair = dfs(node.left)
            rightPair = dfs(node.right)

            withRoot = node.val + leftPair[1] + rightPair[1]
            withoutRoot = max(leftPair) + max(rightPair)
            res = [withRoot, withoutRoot]
            return res
        
        result = dfs(root)
        return max(result)
