# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        #INORDER TRAVERSAL

        min_diff = float('inf')
        def inorder(curr, prev):
            nonlocal min_diff
            if curr is None:
                return prev
            prev = inorder(curr.left, prev)
            min_diff = min(min_diff, abs(prev - curr.val))
            return inorder(curr.right, curr.val)

        inorder(root, float('inf'))
        return min_diff
