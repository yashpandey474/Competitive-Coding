from os import *
from sys import *
from collections import *
from math import *


def floorInBST(root, X):

    # Write your Code here.
    current = root
    ans = None

    while current is not None:
        if current.data < X:
            ans = current
            current = current.right
        
        elif current.data > X:
            current = current.left
        
        else:
            return current.data


    if ans is None:
        return -1

    return ans.data
