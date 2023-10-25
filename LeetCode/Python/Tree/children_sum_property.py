'''
    Following is the class structure of the Node class:

    class Node:
        def __init__(self, data=0, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right
'''

def isLeaf(root):
    if not root.left and not root.right:
        return True

    return False
def isParentSum(root):
    # Write your code here.
    
    #BASE CASE
    if root is None or isLeaf(root):
        return True

    sum = 0
    if root.left:
        sum += root.left.data

    if root.right:
        sum += root.right.data

    if sum == root.data:
        return isParentSum(root.right) and isParentSum(root.left)

    return False
