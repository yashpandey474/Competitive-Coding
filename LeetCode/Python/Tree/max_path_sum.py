# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursion(self, root):
        #BASE CASE
        if root is None:
            return 0

        #RECURSE ON LEFT SUBTREE
        leftSum = max(0, self.recursion(root.left))
        #RECURSE ON RIGHT SUBTREE
        rightSum = max(0, self.recursion(root.right))

        #NOTE: DON'T CONSIDER NEGATIVE SUMS FROM LEFT AND RIGHT [STOP HERE]
        
        #UPDATE MAX PATH
        self.max_path = max(self.max_path, leftSum+rightSum+root.val)

        #RETURN THE PATH SUM POSSIBLE FOR PARENT NODE
        return root.val + max(leftSum, rightSum)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        #VARIABLE TO STORE MAXIMUM PATH SUM
        self.max_path = -float('inf')
        #RECURSE ON ROOT
        self.recursion(root)
        return self.max_path
