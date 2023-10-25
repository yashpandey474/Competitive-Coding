class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def check(root: TreeNode, max_val: int, min_val: int) -> bool:
    if(root is None):
        return True
    
    if(root.val > max_val or root.val < min_val):
        return False
    
    return check(root.left, root.val, min_val) and check(root.right, max_val, root.val)
def is_valid_bst(root: TreeNode) -> bool:

    return check(root, (float('inf')),(-float('inf')))
