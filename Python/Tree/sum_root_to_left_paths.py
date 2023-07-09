# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recSum(self, root, current_sum, total_sum):

        #NON-NULL NODE
        if(root is not None):

            #REACHED LEAF NODE
            if(root.left is None and root.right is None):
                current_sum = current_sum*10 + root.val
                total_sum.append(current_sum)
                return

            #NOT A LEAF NODE
            current_sum = current_sum*10 + root.val
            self.recSum( root.left, current_sum, total_sum)
            self.recSum( root.right, current_sum, total_sum)
        else:
            return
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        total_sum = []
        self.recSum(root, 0, total_sum)
        return sum(total_sum)
