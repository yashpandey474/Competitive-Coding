# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:


    def getInorder(self, root, inorder):
        if root is None:
            return
        
        self.getInorder( root.left, inorder)
        inorder.append(root.val)
        self.getInorder(root.right, inorder)

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        inorder1 = []
        inorder2 = []
        self.getInorder(root1, inorder1)
        self.getInorder(root2, inorder2)

        i, j = 0, 0
        result = []
        while i < len(inorder1) and j < len(inorder2):
            if inorder1[i] <= inorder2[j]:
                result.append(inorder1[i])
                i+=1
            
            else:
                result.append(inorder2[j])
                j+=1

        result.extend(inorder1[i:])
        result.extend(inorder2[j:])
        return result

