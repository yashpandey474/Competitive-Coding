from os import *
from sys import *
from collections import *
from math import *
# Following is the Binary Tree node structure:
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isLeaf(root):
    if not root:
        return False
    if not root.left and not root.right:
        return True
    return False

def addLeft(root, result):
    if root is None:
        return
    if (not isLeaf(root)):
        result.append(root.data)

    if root.left:
        addLeft(root.left, result)

    else:
        addLeft(root.right, result)

def addLeaves(root, result):
    if root is None:
        return
    if (isLeaf(root)):
        result.append(root.data)

    addLeaves(root.left, result)
    addLeaves(root.right, result)

def addRight(root, result):
    if root is None or isLeaf(root):
        return
    if (not isLeaf(root)):
        result.append(root.data)
    
    if root.right:
        addRight(root.right, result)

    else:
        addRight(root.left, result)
    

def traverseBoundary(root):
    # Write your code here.

    
    result = []
    if root is None:
        return result
    result.append(root.data)
    #ADD LEFT BOUNDARY
    addLeft(root.left, result)
    #ADD LEAVES
    addLeaves(root.left, result)
    addLeaves(root.right, result)
    #ADD RIGHT BOUNDARY IN REVERS
    stack = []
    addRight(root.right, stack)
    while stack:
        result.append(stack.pop())

    return result
    
