from os import *
from sys import *
from collections import *
from math import *

def numberOfMismatchingBits(first, second):
    # Write your code here
    mis_match = 0

    while first or second:
        mis_match += ((first & 1) ^ (second & 1))
        first >>= 1
        second >>= 1

    return mis_match
    

            
