from os import *
from sys import *
from collections import *
from math import *

'''
    Following is the class structure of the BinaryTreeNode class:

    class BinaryTreeNode:
        def __init__(self, data):

            self.data = data
            self.left = None
            self.right = None

'''

def recursion(root, answer, result):
    if not root.left and not root.right:
        result.append(answer)
        return

    if root.left:
        recursion(root.left, answer + " " + str(root.left.data), result)

    if root.right:
        recursion(root.right, answer + " " + str(root.right.data), result)

def allRootToLeaf(root):
    # Write your code here.
    result = []
    if not root:
        return result
    recursion(root, str(root.data), result)
    return result

