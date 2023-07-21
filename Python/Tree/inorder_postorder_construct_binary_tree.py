# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        #BASE CASE OF RECURSION
        if not inorder or not postorder:
            return None
        #LAST VALUE IN PREORDER IS THE ROOT
        root_val = postorder[-1]
        root = TreeNode(val = root_val)

        #GET THE INDEX OF ROOT
        inorder_index = inorder.index(root_val)

        #LEFT AND RIGHT
        root.left = self.buildTree(
            inorder[:inorder_index],
            postorder[:inorder_index]
        )
        root.right = self.buildTree(
            inorder[inorder_index+1:],
            postorder[inorder_index:-1]
        )
        return root
