from os import *
from sys import *
from collections import *
from math import *


def recursion(root1, root2):
    if (not root1 and root2) or (root1 and not root2):
        return False

    if not root1 and not root2:
        return True

    if root1.data != root2.data:
        return False

    return recursion(root1.right, root2.left) and recursion(root1.left, root2.right)
def isSymmetric(root):
    
    #Your code goes here
    if root is None:
        return True

    return recursion(root.left, root.right)
