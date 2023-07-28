# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        #LEVEL ORDER TRAVERSAL
        queue = []
        queue.append(root)
        val = root.val

        while queue:
            curr = queue.pop(0)
            val = curr.val
            if curr.right:
                queue.append(curr.right)
            if curr.left:
                queue.append(curr.left)

        return val

