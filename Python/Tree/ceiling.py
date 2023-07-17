from os import *
from sys import *
from collections import *
from math import *

'''
    Following is the TreeNode class structure

    class TreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
'''

def findCeil(root, x):
    # Write your code here.

    current = root
    ans = None

    while current is not None:
        if current.data < x:
            current = current.right

        elif current.data > x:
            ans = current
            current = current.left
        
        else:
            return current.data

    if ans is None:
        return -1
    return ans.data
