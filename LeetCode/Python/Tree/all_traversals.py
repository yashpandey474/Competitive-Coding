from os import *
from sys import *
from collections import *
from math import *

# Following is the Binary Tree node structure:
class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None



def getTreeTraversal(root):
    # Write your code here.
    inorder, preorder, postorder = [], [], []
    stack = []

    if not root:
        return [inorder, preorder, postorder]
    
    #NODE AND NUMBER OF VISIT
    stack.append((root, 1))
    while stack:
        current, visit = stack.pop()
        #FIRST VISIT
        if visit == 1:
            preorder.append(current.data)
            stack.append((current, 2))

            if current.left:
                stack.append((current.left, 1))
            
        #SECOND VISIT
        if visit == 2:
            inorder.append(current.data)
            stack.append((current, 3))

            if current.right:
                stack.append((current.right, 1))
        
        #THIRD VISIT
        if visit == 3:
            postorder.append(current.data)
            
    return [inorder, preorder, postorder]

