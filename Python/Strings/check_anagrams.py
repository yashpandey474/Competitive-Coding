from os import *
from sys import *
from collections import *
from math import *

def areAnagram(str1, str2):
    # Write your code here.
    
    #SORT THE STRINGS AND CONVERT TO LISTS
    l1 = sorted(str1)
    l2 = sorted(str2)

    if len(l1) != len(l2):
        return False

    for i in range(len(l1)):
        if l1[i] != l2[i]:
            return False

    return True
    
