# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:

        #LEVEL ORDER TRAVERSAL
        queue = []
        #IF NON NULL AFTER NULL: return false
        nullEnc = False

        queue.append(root)

        while queue:
            current = queue.pop(0)
            if not current and not nullEnc:
                nullEnc = True

            if current and nullEnc:
                return False

            if current:
                queue.append(current.left)
                queue.append(current.right)

        return True
                
