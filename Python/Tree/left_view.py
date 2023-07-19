from os import *
from sys import *
from collections import *
from math import *

# Binary tree node class for reference
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def getLeftView(root)->list:
    # Write your code here
    # Return a list
    result = []
    queue = []

    if not root:
        return result
        
    queue.append((root, 1))
    current_level = 1

    while queue:
        current, level = queue.pop(0)
        if level == current_level:
            result.append(current.data)
            current_level += 1
        
        if current.left:
            queue.append((current.left, level+1))
        if current.right:
            queue.append((current.right, level+1))


    return result

    
