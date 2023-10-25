'''
1. THE INORDER OF LEFT SUBTREE ENDS AT PREVIOUS INDEX OF ROOT IN INORDER
2. THE PREORDER OF LEFT SUBTREE STARTS AT 1 AND ENDS AT INORDER INDEX OF ROOT
3. THE INORDER OF RIGHT SUBTREE STARTS FROM NEXT INDEX OF ROOT IN INORDER
4. THE PREORDER OF RIGHT SUBTREE STARTS FROM INORDER INDEX OF ROOT +1 AND ENDS AT END OF ARRAY
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    
def build_tree(preorder: list[int], inorder: list[int]) -> TreeNode:
    
    #USE A DICTIONARY TO STORE INDICES IN INORDER
    if not preorder or not inorder:
        return None
        
    root_val = preorder[0]
    root = TreeNode(val = root_val)
    
    inorder_index = inorder.index(root.val)
    
    root.left = build_tree(
        preorder[1:inorder_index+1],
        inorder[:inorder_index]
        )
        
    root.right = build_tree(
        preorder[inorder_index+1:],
        inorder[inorder_index+1:]
        )
        
    return root
