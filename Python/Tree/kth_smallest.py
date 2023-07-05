class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kth_smallest_element(root: TreeNode, k: int) -> int:
    #ITERATIVE SOLUTION
    current = root
    stack = []
    count = 0
    #EXACT SAME AS INORDER TRAVERSAL
    while current  or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        count += 1
        if(count == k):
            return current.val
        current = current.right
        
