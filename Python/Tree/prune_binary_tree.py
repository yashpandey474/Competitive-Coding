from os import *
from sys import *
from collections import *
from math import *
from queue import Queue

# Binary tree node class for reference
class BinaryTreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


def binaryTreePruning(node):

    #   Write your code here
    def prune(root):
        if not root:
            return root

        leftRes = prune(root.left)
        rightRes = prune(root.right)
        if root.val == 1 or (leftRes or rightRes):
            root.left = leftRes
            root.right = rightRes
            return root

        return None

    return prune(node)
            

