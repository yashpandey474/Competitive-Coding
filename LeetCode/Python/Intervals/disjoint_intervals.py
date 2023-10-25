from os import *
from sys import *
from collections import *
from math import *

def disjointIntervals(arr, n):
    # Write your code here

    arr = sorted(arr, key = lambda x: x[1])

    maxInt = 1
    lastInt = 0

    for i in range(1, n):
        if arr[lastInt][1] < arr[i][0]:
            maxInt += 1
            lastInt = i

    return maxInt
